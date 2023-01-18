from django.shortcuts import render
from .models import Quiz
from .serializers import QuizSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator
import requests 


# Create your views here.
def details(request):
    if request.method == 'GET':
        posts = Quiz.objects.all()  #queryset
        serializer = QuizSerializer(posts,many=True)  #converting queryset into native python datatype
        return JsonResponse(serializer.data,safe=False)

def single_details(request,pk):
    try:
        posts= Quiz.objects.get(id=pk)
    except posts.DoesNotExist:
        return HttpResponse(status= 404) #data does not exist

    if request.method=='GET':
        serializer =QuizSerializer(posts)  #serializing just an instance
        return JsonResponse(serializer.data)





def index(request):
    response = requests.get("http://127.0.0.1:8000/details/").json()  #api endpoint,fetching data from this endpoint from database
    paginator= Paginator(response,3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj  
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))
