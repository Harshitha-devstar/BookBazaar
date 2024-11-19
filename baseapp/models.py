from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser,books_sold, books_bought,phone, gender, dob,  **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        books_sold = 0
        books_bought = 0
        


        user = self.model(
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now,
            books_sold = 0,
            books_bought = 0,
            phone = '',
            gender = 'N',
            dob = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_user(self, email, password,phone,gender, dob, **extra_fields):
        return self._create_user(email, password, False, False,0,0,'','N',dob ,**extra_fields)
    def create_superuser(self, email, password,**extra_fields):
        return self._create_user(email, password, True, True,0,0,'','N', timezone.now, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 254, unique = True)
    name = models.CharField(max_length=254)
    phone = PhoneNumberField(region = 'IN', null=True, blank = True)
    gender = models.CharField(max_length=1, choices = {'F':'Female', 'M':'Male', 'N':'Prefer Not Say'}, null=True, blank = True)
    dob = models.DateField(timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True,null=True, blank = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    books_sold = models.IntegerField(default=0)
    books_bought = models.IntegerField(default = 0)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def get_absolute_url(self):
        return "/users/%i/" %(self.pk)
    

# creating a model for genre of books
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering = ['name']
        indexes =[  models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_url(self):
        return reverse('book_list_by_category', args = [self.slug])
    
    def __str__(self):
        return self.name

# creating a model for product-books (on sale)
class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    edition = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    condition = models.CharField(max_length=2, choices = {'N':'Almost New', 'U':'Used', 'R':'Readable'}, null=True, blank = True)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to="books/%Y/%m/%d", blank=True, null=True
    )
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    # seller_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    # seller_email = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields = ['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def get_absolute_url(self):
        return reverse('book_detail', args = [self.id, self.slug])
    
    
    
    def __str__(self):
        return self.name
