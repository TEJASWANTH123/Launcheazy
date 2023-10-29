from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Store the hashed password

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
