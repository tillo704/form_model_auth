from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status,decorators
from .serializer import ProductSerializer,CategorySerializer
from connect.models import Product,Category
from rest_framework.response import Response




class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer =ProductSerializer(instance= products, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        product = get_object_or_404(Product,id=pk)
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    


    def update(self,request,pk=None):
        pass

    def partial_update(self,request,pk=None):
        pass

    def destroy(self,request,pk=None):
        pass




class ProductModelViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    @decorators.action(methods=['put','patch'],detail=True)
    def update_stock(self,request,pk=None):
        product= get_object_or_404(Product,id=pk)
        if product.in_stock:
            product.in_stock = False
        else:
            product.in_stock=False

        product.save()
        return Response({'detail':"Product in_stock Updated!"})






class CategoryModelViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer