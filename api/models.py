from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator
from datetime import date

# Create your models here.

class Question(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Responder(models.Model):
    name=models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{5}-\d{3}-\d{4}$',
                     message="Phone number must be entered in the format: '+99999-999-9999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    address=models.CharField(max_length=255)
    nationality=models.CharField(max_length=255)
    DOB=models.DateField(validators=[MaxValueValidator(limit_value=date.today)])
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    answered_questions=models.ManyToManyField(Question,blank=True,related_name='responders')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['name', 'phone_number']]




class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,
                                    related_name='answers')
    choice=models.CharField(max_length=255)
    responders=models.ManyToManyField(Responder,blank=True,related_name='answers')
    def __str__(self):
        return self.choice
