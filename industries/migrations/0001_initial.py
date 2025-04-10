# Generated by Django 5.2 on 2025-04-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='industries/')),
                ('use_cases', models.TextField(help_text='Explain how AI helps this industry.')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
