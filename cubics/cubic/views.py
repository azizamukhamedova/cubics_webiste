from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import (User, Cubes, RubicsCubeProcess, Steps, StepsStep, Card, About, AboutBox, AboutCard, Time, DiaryNote)
from django import forms
from django.forms import ModelForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import SingleObjectMixin

from django.views import View
from django import forms

class CubeDetailView(DetailView):
    model = Cubes
    template_name = "cubic/cube.html"
    context_object_name = "cube"

    def get_context_data(self, *args, **kwargs):
        context = super(CubeDetailView, self).get_context_data(*args, **kwargs)

        cube = get_object_or_404(Cubes, id=self.kwargs['pk'])
        cubes = Cubes.objects.all()

        if cube.id == 1:
            process = RubicsCubeProcess.objects.first()

        context["process"] = process
        context["cubes"] = cubes
        context["cube"] = cube
        return context


class StepDetailView(DetailView):
    model = Steps
    template_name = "cubic/step.html"
    context_object_name = "step"

    def get_context_data(self, *args, **kwargs):
    
        context = super(StepDetailView, self).get_context_data(*args, **kwargs)
        step = get_object_or_404(Steps, id=self.kwargs['pk'])
        cube = step.cube
        cubes = Cubes.objects.all()

        cards = Card.objects.all()

        saved_cards = []

        for item in cards:
            if item.saved.filter(id=self.request.user.id).exists():
                    saved_cards.append(item)

        context['saved_cards'] = saved_cards
        context["cubes"] = cubes
        context["cube"] = cube
        return context


class AboutDetailView(DetailView):
    model = About
    template_name = "cubic/about.html"
    context_object_name = "about"

    def get_context_data(self, *args, **kwargs):
    
        context = super(AboutDetailView, self).get_context_data(*args, **kwargs)
        about = get_object_or_404(About, id=self.kwargs['pk'])
        cube = about.cube
        cubes = Cubes.objects.all()

        context["cubes"] = cubes
        context["cube"] = cube
        return context

class profileSavedCards(LoginRequiredMixin, ListView):
    model = Card
    template_name = "cubic/profile_saved_cards.html"
    context_object_name = "cards"

    def get_context_data(self, *args, **kwargs):
    
        context = super(profileSavedCards, self).get_context_data(*args, **kwargs)
        about = get_object_or_404(About, id=self.kwargs['pk'])
        cube = about.cube
        cubes = Cubes.objects.all()

        cards = Card.objects.all()

        saved_cards = []

        for item in cards:
            if item.saved.filter(id=self.request.user.id).exists():
                    saved_cards.append(item)

        context['saved_cards'] = saved_cards

        context["cubes"] = cubes
        context["cube"] = cube
        return context


class profileProgress(LoginRequiredMixin, ListView):
    model = Time
    template_name = "cubic/profile_progress.html"
    context_object_name = "times"

    def get_context_data(self, *args, **kwargs):
    
        context = super(profileProgress, self).get_context_data(*args, **kwargs)
        about = get_object_or_404(About, id=self.kwargs['pk'])
        cube = about.cube
        cubes = Cubes.objects.all()
        times = Time.objects.filter(author=self.request.user.id)

        context["time_form"] = ProgressTimeForm()
        context["cubes"] = cubes
        context["cube"] = cube
        context["times"] = times
        return context

class ProgressTimeForm(forms.ModelForm):
    time = forms.CharField(max_length=100) 
    class Meta:
        model = Time
        fields = ['time']

class DiaryNoteForm(forms.ModelForm):
    text = forms.TextInput
    class Meta:
        model = DiaryNote
        fields = ['text']


class profileDiary(LoginRequiredMixin, ListView):
    model = DiaryNote
    template_name = "cubic/profile_diary.html"
    context_object_name = "notes"

    def get_context_data(self, *args, **kwargs):
    
        context = super(profileDiary, self).get_context_data(*args, **kwargs)
        about = get_object_or_404(About, id=self.kwargs['pk'])
        cube = about.cube
        cubes = Cubes.objects.all()

        context["note_form"] = DiaryNoteForm()
        context["cubes"] = cubes
        context["cube"] = cube
        return context


#def save(request, pk):
    #card = get_object_or_404(Card, id=request.POST.get('card_id'))
    #step_page = card.step.main_step.id

    #saved = False
    #if card.saved.filter(id=request.user.id).exists():
        #card.saved.remove(request.user)
        #saved = False
    #else:
        #card.saved.add(request.user)
        #saved = True

    #return redirect('step-detail', pk=step_page)


class save(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'cubic/profile_saved_cards.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'cards'

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        cards = Card.objects.all()
        saved_cards = []

        for item in cards:
            if item.saved.filter(id=user.id).exists():
                saved_cards.append(item)

        return saved_cards

    #def get_context_data(self, *args, **kwargs):
    
        #context = super(save, self).get_context_data(*args, **kwargs)
        #user = get_object_or_404(User, username = self.kwargs.get("username"))
        #cubes = Cubes.objects.all()
        #cards = Card.objects.all()
        #saved_cards = []

        #for item in cards:
           # if item.saved.filter(id=user.id).exists():
               # saved_cards.append(item)

        #context["note_form"] = DiaryNoteForm()
        #context["cubes"] = cubes
        #context["cube"] = cube
        #context["saved_cards"] = saved_cards
        #return context



def mainProfile(request, pk):

    return render(request, 'cubic/profile.html',{
        'cubes' : Cubes.objects.all(),
    })


def index(request):
    return render(request, 'cubic/index.html',{
        'cubes' : Cubes.objects.all(),
    }) 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cubic/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "cubic/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "cubic/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "cubic/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "cubic/register.html")
