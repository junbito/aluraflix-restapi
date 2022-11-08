# Generated by Django 4.1.2 on 2022-11-09 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='videos', to='restapi.category'),
        ),
    ]
