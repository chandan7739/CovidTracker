from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "1026fe9172msh8a7b7d5cefe6cedp1ee4f2jsnd42e03de4cd9",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.

def home(request):
    return render(request,'home.html')
    
def index(request):
    no_results = int(response['results'])
    mylist=[]

    for x in range(0,no_results):
        mylist.append(response['response'][x]['country'])

    if request.method=="POST":
        selected_country = request.POST['selected_country']
        for x in range(0,no_results):
            if selected_country == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)

        context = {'selected_country':selected_country,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'index.html',context)

    context = {'mylist':mylist}
    return render(request,'index.html',context)
