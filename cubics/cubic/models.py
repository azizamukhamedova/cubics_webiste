from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
from PIL import Image


#class User(AbstractUser):
    #pass

class Cubes(models.Model):
    name_en = models.CharField(max_length=100)
    text_en = models.TextField(null=True, blank=True)
    congra_text_en = models.TextField(null=True, blank=True)

    name_uz = models.CharField(max_length=100)
    text_uz = models.TextField(null=True, blank=True)
    congra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_en}"


class RubicsCubeProcess(models.Model):
    img1 = models.ImageField(upload_to='rubics_cube')
    img2 = models.ImageField(upload_to='rubics_cube')
    img3 = models.ImageField(upload_to='rubics_cube')
    img4 = models.ImageField(upload_to='rubics_cube')
    img5 = models.ImageField(upload_to='rubics_cube')
    img6 = models.ImageField(upload_to='rubics_cube')
    img7 = models.ImageField(upload_to='rubics_cube')


class Steps(models.Model):
    cube = models.ForeignKey(Cubes, related_name="steps", on_delete=models.CASCADE)
    step_name_en = models.CharField(max_length=100)
    congra_text_en = models.TextField(null=True, blank=True)

    step_name_uz = models.CharField(max_length=100)
    congra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.cube} - {self.step_name_en}"

class StepsStep(models.Model):
    main_step = models.ForeignKey(Steps, related_name="step", on_delete=models.CASCADE)

    step_name_en = models.CharField(max_length=100)
    extra_text_en = models.TextField(null=True, blank=True)

    step_name_uz = models.CharField(max_length=100)
    extra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.main_step} - {self.step_name_en}"


class Card(models.Model):
    step = models.ForeignKey(StepsStep, related_name="cards", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='cubes/solution')
    solution = models.CharField(max_length=100)
    saved = models.ManyToManyField(User, related_name="saved_solution_card", blank=True)

    name_en = models.CharField(max_length=100)
    extra_text_en = models.TextField(null=True, blank=True)

    name_uz = models.CharField(max_length=100)
    extra_text_uz = models.TextField(null=True, blank=True)
    solution_uz = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.solution}"



class About(models.Model):
    cube = models.ForeignKey(Cubes, related_name="about", on_delete=models.CASCADE)


class MainAboutBox(models.Model):
    about = models.ForeignKey(About, related_name="main_about_box", on_delete=models.CASCADE)

    name_en = models.CharField(max_length=100)
    extra_text_en = models.TextField(null=True, blank=True)

    name_uz = models.CharField(max_length=100)
    extra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_en}"


class AboutBox(models.Model):
    about = models.ForeignKey(MainAboutBox, related_name="about_box", on_delete=models.CASCADE, null=True, blank=True)
    saved = models.ManyToManyField(User, related_name="saved_about_box", blank=True)

    name_en = models.CharField(max_length=100)
    extra_text_en = models.TextField(null=True, blank=True)

    name_uz = models.CharField(max_length=100)
    extra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_en}"


class AboutCard(models.Model):
    about_box = models.ForeignKey(AboutBox, related_name="about_cards", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='cubes/about')

    name_en = models.CharField(max_length=100)
    extra_text_en = models.TextField(null=True, blank=True)

    name_uz = models.CharField(max_length=100)
    extra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_en}"

class PartsOfCube(models.Model):
    cube = models.ForeignKey(Cubes, related_name="parts_of_cube", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='rubics_cube/parts_of_cube')

    name_en = models.CharField(max_length=100)
    extra_text_en = models.TextField(null=True, blank=True)

    name_uz = models.CharField(max_length=100)
    extra_text_uz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_en}"

class Time(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=100)

class DiaryNote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()






    

    