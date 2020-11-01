from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICES = (
        ("MAIL", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    )
    LANGUAGE_CHOICES = (
        ("EN", "english"),
        ("KR", "korean"),
    )
    CURRENCY_CHOICES = (
        ("usd", "USD"),
        ("krw", "KRW"),
    )
    LOGIN_CHOICES = (
        ("email", "Email"),
        ("github", "Github"),
        ("kako", "Kakao"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=50, blank=True, choices=GENDER_CHOICES)
    bio = models.TextField()
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, blank=True)
    superhost = models.BooleanField(default=False)
    login_method = models.CharField(
        max_length=10, choices=LOGIN_CHOICES, default="Email"
    )
