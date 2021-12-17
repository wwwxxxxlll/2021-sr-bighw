#返回一个html页面
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Index(View):
    def get(self,request):
        return render(request,'index.html')

class aboutus(View):
    def get(self,request):
        return render(request,'about-us.html')

class Error(View):
    def get(self,request):
        return render(request,'404.html')

class Explain(View):
    def get(self,request):
        return render(request,'说明.html')

#class Contribution(View):
#    def get(self,request):
#        contribute_data = []
#        conact = {}
#        if request.POST:
#            conact = request.POST.get('urn')
#            print(conact)
#            print("1")
#            contribute_data = {'value': 0, 'name': '0'}
#        else:
#            contribute_data = {'value': 0, 'name': ''}
#        return render(request,'contribution.html', {"contribute_data": contribute_data} )
