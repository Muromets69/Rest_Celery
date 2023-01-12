from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from CeleryWithAPI import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = routers.DefaultRouter().urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path("home/<pk>/",views.home, name="home"),
    path("car/",views.gg),
    path('api/cars/',views.CarViewSet.as_view({"get":"list",'post':'create'})),
    path('api/<pk>/get_car/',views.CarViewSet.as_view({'get':"get_photo"})),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token-auth/', include('djoser.urls')),          
    re_path(r'^token-auth/', include('djoser.urls.authtoken')),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
