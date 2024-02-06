from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


def validate_title(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')



class News(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(2), validate_title])
    content = models.TextField(validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    categories =  models.ManyToManyField(Category)

    def __str__(self):
        return self.title
