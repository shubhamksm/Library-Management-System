from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Book, Book_sub
from django.db.models import Q

from .forms import SearchForm

# Create your views here.

@login_required
def dashboard(request):
  content = {}
  #If POST is request is made
  if request.method == 'POST':
    search_form = SearchForm(request.POST)
    if search_form.is_valid():
      data = search_form.cleaned_data['search_field']
      #First try if input data matches with any ISBN then only show that specific entry
      try:
        book = Book.objects.get(pk=data)
        content = {
          'book': book,
          'search_form': search_form
        }
      #If not found ISBN then search in the database with simillar books available from given input data
      except Book.DoesNotExist:
        # Old query to search out Data based on title only
        # books = Book.objects.filter(title__contains=data)
        # New query to search out data based on Q object with or condition. 
        books = Book.objects.filter(Q(title__contains=data)|Q(author__contains=data))
        print(books)
        content = {
          'books': books,
          'search_form': search_form
        }
      return render(request, 'dashboard.html', content)
      

  else:
    search_form = SearchForm()
    content = {
      'search_form': search_form
    }
    return render(request, 'dashboard.html', content)