from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Main Book Model
class Book(models.Model):
  isbn = models.CharField(max_length=15, primary_key=True)
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  stock = models.IntegerField(default=5)
  is_available = models.BooleanField()

  def __str__(self):
    return self.isbn



#Sub Book Model 
class Book_sub(models.Model):
  isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
  subscribed_by = models.ForeignKey(User, on_delete=models.CASCADE)
  subscribed_at = models.DateField(auto_now_add=True)
  due_date = models.DateField()

  def __str__(self):
    return self.isbn.isbn
