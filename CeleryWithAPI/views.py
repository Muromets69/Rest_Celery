from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .tasks import some_task
import requests

class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class = CarSerializer

    @action(methods=['post'],detail=True)
    def get_photo(self,request,*args, **kwargs):
        pk = kwargs['pk']
        try:
            car = Car.objects.get(name=pk)
            data = {'id':car.pk,"name":car.name,"image":"http://"+request.META['HTTP_HOST']+car.img.url}
            some_task.delay(car.img.url)
        except Car.DoesNotExist:
            return Response({"Error":"Not Found!"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"data":data},status=status.HTTP_200_OK)
    
def home(request,pk):    
    m = {"data":Car.objects.get(name=pk)}
    return render(request=request, template_name="t.html",context=m) 

def gg(req):
    data = requests.get("http://127.0.0.1:8000/api/BMW/get_car/")
    return render(request=req, template_name="t.html",context=data.json()) 
    
def downl(request,path):
    file_p = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_p):
        with open(file_p,"rb")as file:
            res = HttpResponse(file.read(),content_type="application/adminupload")
            res["Content-Disposition"] = 'inline;filename='+os.path.basename(file_p)
            return res
