# Generated by Django 5.1.4 on 2024-12-11 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('business_name', models.CharField(max_length=300)),
                ('business_brand', models.CharField(max_length=300)),
                ('mobile_number', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('tech_school_you_graduated_from', models.CharField(max_length=300)),
                ('tech_skill', models.CharField(max_length=300)),
                ('why_should_we_onboard_you', models.CharField(max_length=300)),
                ('what_can_we_offer', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
