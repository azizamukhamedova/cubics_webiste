from django.contrib import admin
from .models import (
    Cubes, RubicsCubeProcess, Steps, StepsStep,
    Card, About, MainAboutBox, AboutBox, AboutCard,
    PartsOfCube, DiaryNote, Time)

# Register your models here.
admin.site.register(Cubes)
admin.site.register(PartsOfCube)
admin.site.register(RubicsCubeProcess)
admin.site.register(Steps)
admin.site.register(StepsStep)
admin.site.register(Card)
admin.site.register(About)
admin.site.register(MainAboutBox)
admin.site.register(AboutBox)
admin.site.register(AboutCard)
admin.site.register(DiaryNote)
admin.site.register(Time)

