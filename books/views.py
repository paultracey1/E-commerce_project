from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from django.template.context_processors import csrf


# Create your views here.
def all_books(request):
    books = Book.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "books.html", {"books": books}, args)

def book_detail(request, id):
    book  = get_object_or_404(Book, pk=id)
    return render(request, "bookdetail.html", {'book': book})




class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer