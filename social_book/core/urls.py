from django.urls import path
from.import views


urlpatterns = [
    # ... your other URL patterns here ...
    path('',views.index, name='index')
] 
