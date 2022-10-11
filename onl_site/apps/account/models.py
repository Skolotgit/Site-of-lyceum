from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField('ім\'я', max_length = 20, null=True)
    surname = models.CharField('прізвище', max_length = 20, null=True)
    roli_ho_ua = models.EmailField('ролі.хо.юа', max_length=70, null=True, unique=True)


    type_of_user_tuple = (
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('PERSONNEL', 'Personnel')
    )
    type_of_user = models.CharField('тип користувача', max_length=10, choices=type_of_user_tuple, default='STUDENT', null=True)

    def __str__(self):
        email = str(self.roli_ho_ua)
        return email

    