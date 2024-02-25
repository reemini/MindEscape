# Generated by Django 5.0.2 on 2024-02-15 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userEmail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('password', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('role', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.user')),
                ('adminID', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.user')),
                ('educatorID', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=100)),
                ('professional_title', models.CharField(max_length=100)),
                ('linkedIn_account', models.URLField()),
                ('isOfficialReviewer', models.BooleanField(default=False)),
                ('areas_of_specialization', models.TextField()),
            ],
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.user')),
                ('stdID', models.AutoField(primary_key=True, serialize=False)),
                ('areas_of_interest', models.TextField()),
            ],
            bases=('users.user',),
        ),
    ]
