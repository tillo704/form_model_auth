from .views import index,sign_up,registr,add_user,update_user,delete_user,add_student,studentlist,delete_student,registration
from django.urls import path
from connect.views import add_order,orderlist,product,delete_order,product_detail,add_product


urlpatterns =[
    path('', index, name='index'),
    path('sign_up/',sign_up, name="sign_up"),
    path('registr/',registr, name= 'registr'),
    path('add/user/',add_user,name= 'add_user'),
    path('delete/<int:pk>/',delete_user,name='delete_user'),
    path('update_user/<int:pk>/',update_user,name= 'update_user'),
    path('add/order/',add_order, name='add_order'),
    path('orderlist/',orderlist,name="orderlist"),
    path('product/',product,name='product' ),
    path('slug:cat_slug/',product,name='cat_detail' ),
    path('delete/<customer>/',delete_order,name='delete_order'),
    path('product_detail/<int:pk>/', product_detail,name='product_detail'),
    path('add/product',add_product,name='add_product'),
    path('add/student/',add_student,name="add_student"),
    path('studentlist/',studentlist,name='studentlist'),
    path('delete/<int:pk>/',delete_student,name='delete_student'),
    path('registration/',registration,name='registration')
   

]