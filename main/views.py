from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import *
from .models import *

def index(request):
    listings = Listing.objects.filter(sold = False)
    return render(request, 'index.html', {'listings': listings})

class SubmitView(CreateView):
    form_class = ListingForm
    template_name = 'submit.html'

class ListingDetail(DetailView):
    model = Listing
    template_name = 'listing.html'

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_string = form.cleaned_data['query']
            words = search_string.lower().split(' ')
            vector = SearchVector('title', 'category', 'location', 'condition',
                    'description', 'op')

            query = SearchQuery(words[0])
            for word in words[1:]:
                query = query | SearchQuery(word)

            listings = Listing.objects.annotate(rank=SearchRank(vector,
                query)).order_by('-rank')

            return render(request, 'results.html',
                    {'search_string': search_string, 'listings': listings})

    return HttpResponseRedirect('/')
