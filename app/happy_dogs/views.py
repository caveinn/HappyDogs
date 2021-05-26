import math

from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.generic import FormView
from .models import Dog, BoardingVisit
from .forms import DogCreateForm, BoardingVisitForm, QueryDatesForm

# Create your views here.

class CreateDogView(FormView):
    model = Dog
    form_class = DogCreateForm
    template_name = 'happy_dogs/add-dog.html'

    def post(self, request):
        """
        Overide the default post()
        """
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        form.save()
        return render(request, self.template_name, {"form": form, "message": "Dog created successfully"})


class BoardingVisitView(FormView):
    model = BoardingVisit
    form_class = BoardingVisitForm
    template_name = 'happy_dogs/add_visit.html'

    def post(self, request):
        """
        Overide the default post()
        """
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        form.save()
        return render(request, self.template_name, {"form": form, "message": "visit created successfully"})

class QueryDatesView(FormView):
    form_class = QueryDatesForm
    template_name = 'happy_dogs/home.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        data = form.cleaned_data
        start_date = data['start_date']
        end_date = data['end_date']
        delta = end_date - start_date
        visits_data = [[]]
        start_day =  start_date.weekday()
        end_day =end_date.weekday()
        days_to_weekend = 6-end_day
        number_of_weeks = math.ceil((delta.days+start_day)/7)
        days_added = 0
        weeks_added= 0

        #padding date:
        for i in range(start_day):
            visits_data[weeks_added].append({"count": None,  "visits":None, "day_of_week": None, "date" : None})
            days_added += 1
            if days_added % 7 == 0:
                days_added =0
                weeks_added +=1
                visits_data.append([])
        for i in range(delta.days+1):
            curr_date  = start_date + timedelta(days=i)
            visits = BoardingVisit.objects.filter(start_date__lte =curr_date, end_date__gte=curr_date)
            visits_data[weeks_added].append({"count": visits.count(), 'visits': visits, 'day_of_week': curr_date.weekday(), 'date':curr_date})
            days_added += 1
            if days_added % 7 == 0:
                days_added =0
                weeks_added +=1
                visits_data.append([])
        for i in range(days_to_weekend):
            visits_data[weeks_added].append({"count": None,  "visits":None, "day_of_week": None, "date" : None})
            days_added += 1
            if days_added % 7 == 0:
                days_added =0
                weeks_added +=1
                visits_data.append([])

        print(weeks_added)
        return render(request, self.template_name, {"form": form, "visits_data": visits_data, })
