from django.urls import path, include

urlpatterns = [

    path('site/', include('api.v1.site.urls'))

]
