# Generated by Django 3.2.3 on 2021-07-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='core.UserProfile'),
        ),
    ]
