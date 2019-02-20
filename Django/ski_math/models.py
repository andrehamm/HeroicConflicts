from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate    
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Game(models.Model):
    level_id = models.PositiveSmallIntegerField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Section(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_student_profiel(sender, instance, **kwargs):
    instance.student.save()

@receiver(post_save, sender=User)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        Teacher.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_teacher_profiel(sender, instance, **kwargs):
    instance.teacher.save()