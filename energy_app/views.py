from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Data, Annual_Data
from .forms import DataForm
from .eia_app import get_data

# Create your views here.

class NewState(View):

    def get(self, request, *args, **kwargs):
        form = DataForm()
        return render(request,'new.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = DataForm(request.POST)
        if form.is_valid():
            statename = request.POST['state']
            data = get_data(statename)
            data_instance = Data()
            data_instance.state = statename
            data_instance.slope = data['slope']
            data_instance.intercept = data['intercept']
            data_instance.save()
            for i in range(len(data['year'])):
                annual_instance = Annual_Data()
                annual_instance.state = data_instance
                annual_instance.year = data['year'][i]
                annual_instance.price = data['price'][i]
                annual_instance.save()

        return render(request,'new.html', {'form':form})
