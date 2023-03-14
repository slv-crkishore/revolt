from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100, verbose_name="School")

    def __str__(self) -> str:
        return self.name


class Classes(models.Model):
    name = models.CharField(max_length=10, verbose_name="Class Name")
    school = models.ForeignKey(
        to=School, on_delete=models.CASCADE, related_name="school_name")

    def __str__(self) -> str:
        return self.name


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_user(self, email, password=None, **extra_fields):

#         if not email:
#             raise ValueError("Email is required")

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         # if extra_fields.get("is_staff") is not True:
#         #     raise ValueError("superuser must have is_staff as True")

#         return self.create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
    class_name = models.ForeignKey(
        to=Classes, on_delete=models.CASCADE, null=True, related_name="class_name")

    gender = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)

    # USERNAME_FIELD = "email"

    class Meta:
        db_table = "USERS"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return self.last_name
