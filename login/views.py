from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView

# def index(request):
#     # template = loader.get_template('index.html')
#     # return HttpResponse(template.render(request))
#     return render(request,'index.html')

class Index(APIView):
    def get(self,request):
        print("get业务")
        return 1
    def post(self,request):
        print("post业务")
        return 2




