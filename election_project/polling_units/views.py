from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from . models import AnnouncedPuResults
from polling_units.forms import UserInfoForm, PollingResultForm
from . filters import ResultFilter
from django.db.models import Sum, Count

# Create your views here.
def index(request):
    polls_filter = ResultFilter(request.GET, queryset=AnnouncedPuResults.objects.all())
    
    context = {
        'form': polls_filter.form,
        'polls': polls_filter.qs,
        
        #'polls': AnnouncedPuResults.objects.all()
        }
    return render(request, 'index.html', context)


def create(request):
    form = UserInfoForm()
    if request.method == 'POST':
        form= UserInfoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit = True)
            return form(request)
        else:
            print("Invalid Form")
    return render(request,'create.html', {'form':form})
   

def results(request):
    party = AnnouncedPuResults.objects.values('party_abbreviation').annotate(total_no_of_units=Count('party_abbreviation'), total_votes=Sum('party_score'))
    score = AnnouncedPuResults.objects.aggregate(Sum('party_score'))
    context = {
        'score': score,
        'party': party
    }
    return render(request, 'results.html', context)



