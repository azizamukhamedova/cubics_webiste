# Generated by Django 3.0.8 on 2020-09-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cubic', '0004_auto_20200920_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutbox',
            name='about',
        ),
        migrations.CreateModel(
            name='MainAboutBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100)),
                ('extra_text_en', models.TextField(blank=True, null=True)),
                ('name_uz', models.CharField(max_length=100)),
                ('extra_text_uz', models.TextField(blank=True, null=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_about_box', to='cubic.About')),
            ],
        ),
    ]
