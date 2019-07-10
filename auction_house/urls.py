
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name='home'),
    # path('search/',views.search, name='q'),
    path('login/',views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('allproduct/',views.allproducts, name='allproducts'),
    path('bid/', views.Bid, name='bid'),
    path('about_us/', views.about_us, name='about_us'),
    path('drawingdetails/<int:drawing_product_id>/', views.drawing_details, name='drawingdetails'),
    path('paintingdetails/<int:painting_product_id>/', views.painting_details, name='paintingdetails'),
    path('carvingdetails/<int:carving_product_id>/', views.carving_details, name='carvingdetails'),
    path('photographicdetails/<int:photographic_product_id>/', views.photographic_details, name='photographicdetails'),
    path('sculpturedetails/<int:sculpture_product_id>/', views.sculpture_details, name='sculpturedetails'),
]