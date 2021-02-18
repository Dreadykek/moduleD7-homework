from django.shortcuts import render, redirect
from .models import Book, Publisher, Author
from .forms import AuthorForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        qs =super().get_queryset()
        get_params = self.request.GET.dict()

        if get_params.get('q'):
            qs = qs.filter(name__icontains = get_params.get('q'))

        return qs

class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher_list.html'


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:book_list')
    template_name = 'author_edit.html'
