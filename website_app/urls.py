from website import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from website_app import views

urlpatterns = [
    path('home/',views.home),
    path('menu',views.menu),
    path('about',views.about),
    path('contact',views.contact),
    path('booktable',views.book_table),
    path('register',views.user_register,name='register'),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('cdetails/<cid>',views.coffee_details),
    path('gallery',views.gallery),
    path('addtocart/<cid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    # path('index',views.index),
    path('showtable',views.showtable)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

