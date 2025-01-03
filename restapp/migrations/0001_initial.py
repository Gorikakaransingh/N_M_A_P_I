# Generated by Django 5.0.3 on 2024-03-11 10:09

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
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=10)),
                ('addedBy', models.CharField(default='', max_length=20)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(db_column='uid', default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
