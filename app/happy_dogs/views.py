from django.shortcuts import render
from django.views.generic import FormView
from .models import Dog, BoardingVisit
from .forms import DogCreateForm, BoardingVisitForm

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
    form_class = BoardingVisitForm
    template_name = 'happy_dogs/home.html'

    def post(self, request):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {"form": form,})
