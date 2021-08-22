import library
from django.shortcuts import render
from .models import Book



def index(request):

    books = Book.objects.all()
    context = {"books":books}
    return render(request, 'library/index.html',context)