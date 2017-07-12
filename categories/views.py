from django.shortcuts import render, get_object_or_404
from .models import Category
from books.models import Book


# Create your views here.
def root_categories(request):
    categories = Category.objects.filter(parent=None)

    args = { 'categories': categories, 'subcategories': {}, 'books': {}}
    return render(request, 'categories.html', args)


def get_category(request, id):
    this_category = get_object_or_404(Category, pk=id)

    crumbs = []

    crumb = this_category
    while crumb != None:
        crumbs.insert(0, crumb)
        crumb = crumb.parent

    subcategories = Category.objects.filter(parent=this_category)

    books = this_category.books.all()

    args = { 'categories': subcategories, 'books': books, 'crumbs': crumbs}
    return render(request, 'categories.html', args)


def root_categories_context(request):
    categories = Category.objects.filter(parent=None)
    return {'root_categories': categories}
