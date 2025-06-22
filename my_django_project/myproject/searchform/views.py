from django.shortcuts import render
from .forms import BookSearchForm
from .models import Book

def book_search(request):
    form = BookSearchForm()
    query = request.GET.get('q')
    results = []

    if query:
        results = Book.objects.filter(title__icontains=query)

    context = {
        'form': form,
        'query': query,
        'results': results,
    }
    return render(request, 'book_search.html', context)
