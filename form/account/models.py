from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,Email,Image=None,First_name=None,Last_name=None,Age=None,Unique_id=None,password=None):
        if not Email:
            raise ValueError("Must have Email")

        if not password:
            raise ValueError("Must have Password")

        user=self.model(
            Email=self.normalize_email(Email),
            Image=Image,
            First_name=First_name,
            Last_name=Last_name,
            Age=Age,
            Unique_id=Unique_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,Email,Image=None,First_name=None,Last_name=None,Age=None,Unique_id=None,password=None):
        user=self.create_user(
            Email=self.normalize_email(Email),
            Image=Image,
            First_name=First_name,
            Last_name=Last_name,
            Age=Age,
            Unique_id=Unique_id,
            password=password,
        )
        user.staff=True
        user.save(using=self._db)
        return user

    def create_superuser(self,Email,Image=None,First_name=None,Last_name=None,Age=None,Unique_id=None,password=None):
        user=self.create_user(
            Email=self.normalize_email(Email),
            Image=Image,
            First_name=First_name,
            Last_name=Last_name,
            Age=Age,
            Unique_id=Unique_id,
            password=password,
        )
        user.staff=True
        user.admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    Image=models.ImageField(upload_to='Images',default="",blank=True,null=True)
    First_name=models.CharField(max_length=255,blank=True,null=True)
    Last_name=models.CharField(max_length=255,blank=True,null=True)
    Age=models.IntegerField(blank=True,null=True)
    Unique_id=models.CharField(max_length=6,default=get_random_string(length=6))
    Email=models.EmailField(max_length=255,unique=True)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='Email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.Email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
