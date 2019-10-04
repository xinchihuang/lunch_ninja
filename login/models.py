from django.db import models

class User(models.Model):

    gender = (
        ('male','male'),
        ('female','female'),
        ('nonbinary','nonbinary'),
        ('keep secret','keep secret'),
    )
    username = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="keep secret")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "users"
        verbose_name_plural = "users"

# Create your models here.
