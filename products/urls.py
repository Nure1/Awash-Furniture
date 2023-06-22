from django.urls import path
from . import views
from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet,CategoryViewSet, OrderViewSet, ProductImageViewSet, ProductImagesAPIView, ProductImagesDetailAPIView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'product_images', ProductImageViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('api/products/<int:product_id>/images/', ProductImagesAPIView.as_view(), name='product-images'),
    path('api/products/<int:product_id>/images/<int:image_id>/', ProductImagesDetailAPIView.as_view(), name='product-image-detail'),
]

