from django.urls import path,include
from .views import  add_order, index,delete_order

urlpatterns = [
    path('',index,name='index'),
    path('add/order/',add_order, name='add_order'),
    path('delete/<int:pk>/',delete_order,name='delete_order'),
    path('__debug__/', include('debug_toolbar.urls')),
    

]