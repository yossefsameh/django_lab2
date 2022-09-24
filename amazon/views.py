from django.shortcuts import render
from amazon.models import Cars
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from amazon.forms import CarModelForm
# Create your views here.
def carIndex(request):
    allcars = Cars.get_all_cars()
    return render(request,"amazon\index.html",context={"cars":allcars})


class CarDetails(DetailView):
    model = Cars
    template_name = "amazon/show.html"

class CreateCarView(CreateView):
    template_name = "amazon/create.html"
    form_class = CarModelForm
    success_url = '/amazon/index'

class EditCarView(UpdateView):
    template_name = "amazon/edit.html"
    form_class = CarModelForm
    success_url = '/amazon/index'
    model = Cars

class DeleteCarView(DeleteView):
    template_name = "amazon/delete.html"
    success_url = '/amazon/index'
    model = Cars