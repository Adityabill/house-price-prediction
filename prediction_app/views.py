from django.shortcuts import render
from  django.http import HttpResponse
from django.template import loader
from datetime import date

current_date = date.today()

# Create your views here.
def homePage(request):
    # return render(request, 'home.html')
    template = loader.get_template('home.html')
    today_date = {
        'year':current_date.year,
        'month':current_date.month,
    }

    return HttpResponse(template.render(today_date, request))
