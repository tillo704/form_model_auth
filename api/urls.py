from .views import ProductViewSet,ProductModelViewset,CategoryModelViewset
from django.urls import path
from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()
router.register(r"product",ProductModelViewset,basename='product')
router.register(r"category",CategoryModelViewset,basename='category')

urlpatterns = router.urls


# urlpatterns =[
#     path('products/',ProductModelViewset.as_view({"get":'list','post':'create'})),
#     path('product/<int:pk>/',ProductModelViewset.as_view({"get":"retrieve", 'put':'update','patch':'partial_update','delete':'destroy'}))
# ]