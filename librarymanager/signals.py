from .models import Book, Book_sub

#import the signals 
from django.db.models.signals import post_save, post_delete
#Import receiver decorator
from django.dispatch import receiver

#This signal will listen to the Book_sub model for subscription
#If any book is subscribed then Book.stock would be decrement by 1
@receiver(post_save, sender=Book_sub)
def remove_from_stock(sender, instance, created, **kwargs):
  if created:
    book = Book.objects.get(pk=instance.isbn.isbn)
    book.stock -= 1
    if book.stock == 0:
      book.is_available = False
    book.is_available = True
    #save the changes to the book model
    book.save()

#This signal will listen to the Book_sub model for unsubscription
#If any book is subscribed then Book.stock would be increment by 1
@receiver(post_delete, sender=Book_sub)
def add_to_stock(sender, instance, using, **kwargs):
  book = Book.objects.get(pk=instance.isbn.isbn)
  book.stock += 1
  book.is_available = True
  #save the changes to the book model
  book.save()

# @receiver(post_save, sender=Book_sub)
# def update_stock(sender, instance, created, **kwargs):

