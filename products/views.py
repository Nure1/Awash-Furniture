from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets, routers
from .serializers import ProductSerializer, ProductImageSerializer,CategorySerializer, OrderSerializer
from .models import Product,Category, Order, ProductImage

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    

class ProductImagesAPIView(APIView):
    def get_object(self, product_id, image_id):
        try:
            return ProductImage.objects.get(product_id=product_id, id=image_id)
        except ProductImage.DoesNotExist:
            return None

    def get(self, request, product_id):
        product_images = ProductImage.objects.filter(product=product_id)
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        request.data['product'] = product_id
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductImagesDetailAPIView(APIView):
    def get_object(self, product_id, image_id):
        try:
            return ProductImage.objects.get(product_id=product_id, id=image_id)
        except ProductImage.DoesNotExist:
            return None
    
    def get(self, request, product_id, image_id):
        product_image = self.get_object(product_id, image_id)
        serializer = ProductImageSerializer(product_image)
        return Response(serializer.data)

    def put(self, request, product_id, image_id):
        product_image = self.get_object(product_id, image_id)
        if not product_image:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductImageSerializer(product_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id, image_id):
        product_image = self.get_object(product_id, image_id)
        if not product_image:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        product_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



   

# class ProductAPIView(APIView):
#     def post(self, request):
#         product_serializer = ProductSerializer(data=request.data)
#         if product_serializer.is_valid():
#             product = product_serializer.save()
#             images_serializer = ProductImageSerializer(data=request.data.getlist('images'), many=True)
#             if images_serializer.is_valid():
#                 images_serializer.save(product=product)
#                 return Response(product_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         product_serializer = ProductSerializer(data=request.data)
#         if product_serializer.is_valid():
#             product = product_serializer.save()
#             images_serializer = ProductImageSerializer(data=request.data.getlist('images'), many=True)
#             if images_serializer.is_valid():
#                 images_serializer.save(product=product)
#                 return Response(product_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer








def home(request):
    return HttpResponse("Hello world!")