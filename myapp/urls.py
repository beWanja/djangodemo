''' 
This URL page is specific to this app and must do some routing in the root directory
'''
from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.myview, name='myview'),
    # connecting the details url to the correct view 
    # with id as the parameter
    path('myapp/details/<int:id>', views.details, name='details'),
]