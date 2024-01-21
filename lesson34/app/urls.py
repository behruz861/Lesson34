from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:slug>/add-comment/', add_comment, name='add_comment'),

    path('product/<slug:slug>/like/', like_product, name='like_product'),
    path('comment/<int:pk>/like/', like_comment, name='like_comment'),

    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('profile/', UserProfileView.as_view(), name='profile'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('cart/buy/', buy_products, name='buy'),
    path('cart/buy-history/', BuyHistoryListView.as_view(), name='buy_history'),

    path('add_product/<int:product_id>/', add_product, name='add_product'),
]


