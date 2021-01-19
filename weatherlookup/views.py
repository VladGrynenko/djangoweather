
from django.shortcuts import render

# Create your views here.

#this is my home page view
def home(request):
    import json
    import requests
    #
    API_Key = '1820D642-4FF4-4172-A747-6051D0DC5C19'
    zipCode = '20002'
    if request.method == "POST":
        zipCode = request.POST.get('zipcode_enter','')
    distance = '25'
    api_url = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={}&distance={}&API_KEY={}'.format(zipCode,distance,API_Key)

    aqi_groups = {'Good':'Air quality is satisfactory, and air pollution poses little or no risk.',
    'Moderate':'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.',
    'Unhealthy for Sensitive Groups':'Members of sensitive groups may experience health effects. The general public is less likely to be affected.',
    'Unhealthy':'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.',
    'Very Unhealthy':'Health alert: The risk of health effects is increased for everyone.',
    'Hazardous':'Health warning of emergency conditions: everyone is more likely to be affected.'}
    cat_colors = {'Good':'good', 'Moderate': 'moderate', 'Unhealthy for Sensitive Groups' : 'usg', 'Unhealthy':'unhealthy', 'Very Unhealthy':'veryunhealthy', 'Hazardous': 'hazardous' }


    try:
        api = requests.get(api_url).json()
        #api = api_request
        aqi_name = api[0]["Category"]["Name"]
        #aqi_name = 'Unhealthy for Sensitive Groups'
        aqi_descr = aqi_groups.get(aqi_name, '')
        category_color = cat_colors.get(aqi_name, '')

    except Exception as e:
        api = 'Error with response converting to json'
        aqi_descr = ''
        category_color = ''

    ctx = { 'api': api, 'zipCode': zipCode, 'aqi_descr': aqi_descr, 'category_color': category_color }
    #print(ctx)

    return render(request, 'home.html', ctx )

def about(request):
    return render(request, 'about.html', {})
