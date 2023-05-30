from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, city,password=None):
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            city = city,
        )
        user.set_password(password)
        user.save(using=self._db) ## use the default Db as set up in setting.py
        return user
    
    def create_superuser(self, first_name, last_name, username, email, city, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            city = city,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    STUDENT = 1
    TEACHER = 2
    ROLE_CHOICE = {
       (STUDENT, 'Student'),
       (TEACHER, 'Teacher'), 
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100, unique=True)
    city = models.CharField(max_length=50, blank=True,null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True, null=True)
    
    #required fields
    date_joined =models.DateTimeField(auto_now_add=True)
    last_login =models.DateTimeField(auto_now_add=True)
    created_date =models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name','city'] 
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    
    
        
    

    
    
    

