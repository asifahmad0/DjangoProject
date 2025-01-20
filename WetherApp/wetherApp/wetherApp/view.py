from django.shortcuts import render
import requests
import datetime


def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'pakur'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d1684d03f3f1220d7e466dae6e412588'
    PARAMS = {'units':'metric'}

    data =requests.get(url,PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()
    return render(request, 'index.html',{'city':city, 'description':description, 'icon':icon, 'temp': temp, 'day':day})