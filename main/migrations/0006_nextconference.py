# Generated by Django 5.1 on 2024-08-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_carouselimage_remove_message_discussion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NextConference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('inscription_open', models.BooleanField(default=False)),
            ],
        ),
    ]