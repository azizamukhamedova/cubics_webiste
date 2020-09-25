from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("account/<int:pk>/", views.mainProfile, name="profile-main"),
    path("account/<int:pk>/cards/", views.profileSavedCards.as_view(), name="profile-saved-cards"),
    path("account/<int:pk>/progress/", views.profileProgress.as_view(), name="profile-progress"),
    path("account/<int:pk>/diary/", views.profileDiary.as_view(), name="profile-diary"),

    path("about/<int:pk>/", views.AboutDetailView.as_view(), name="cube-about"),
    path("cube/<int:pk>/", views.CubeDetailView.as_view(), name="cube-detail"),
    path("step/<int:pk>/", views.StepDetailView.as_view(), name="step-detail"),

    path("save/<int:pk>/", views.save, name="save-remove"),
    path("save/profile/<int:pk>/", views.saveProfile, name="save-remove-profile"),
    #path("save/about/<int:pk>/", views.saveAboutBox, name="save-remove-about-box"),

    path("progress/set/", views.ProgressView, name="progress-time"),
    path("diary/note/", views.DiaryNoteView, name="diary-note-create"),
]