from django.urls import path
from . import views
app_name='ShoppingApp'
urlpatterns = [

    path('',views.AllProductCat,name='AllProductCat'),
    path('<slug:c_slug>/',views.AllProductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetail,name='product_Detail'),
]