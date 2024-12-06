from django.urls import path
from .views import home, doston, ali, cars, ota, ona, aka, uka, opa, me

urlpatterns = [
    path('', home),
    path('doston/', doston),
    path('ali/', ali),
    path('cars/', cars),
    path('ota/', ota),
    path('ona/', ona),
    path('aka/', aka),
    path('uka/', uka),
    path('opa/', opa),
    path('me/', me)



]