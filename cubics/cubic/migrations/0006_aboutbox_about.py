# Generated by Django 3.0.8 on 2020-09-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cubic', '0005_auto_20200920_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutbox',
            name='about',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_box', to='cubic.MainAboutBox'),
        ),
    ]