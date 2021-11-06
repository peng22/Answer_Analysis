# Generated by Django 3.2.9 on 2021-11-06 01:36

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Responder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999-999-9999'.", regex='^\\+?1?\\d{4}-\\d{3}-\\d{4}$')])),
                ('address', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('DOB', models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('answered_questions', models.ManyToManyField(related_name='responders', to='api.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api.question')),
                ('responders', models.ManyToManyField(related_name='answers', to='api.Responder')),
            ],
        ),
    ]