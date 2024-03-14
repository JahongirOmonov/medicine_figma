from django.urls import path
from users import views
from shop import views as shop_view

urlpatterns = [
    path('users/', views.UserListApiView.as_view()),
    path('user-detail/<int:pk>', views.UserDetailApiView.as_view()), #👌
    path('user-update/<int:pk>', views.UserUpdateApiView.as_view()), #👌
    path('product/', shop_view.ProductListApiView.as_view()),
    path('product/<int:pk>', shop_view.ProductDetailApiView.as_view()),
    path('cart/', shop_view.CartApiView.as_view()), #👌
    path('cart-remove/<str:id>', shop_view.RemoveFromCartApiView.as_view()), #👌
    path('cart-clear/', shop_view.ClearCartApiView.as_view()), #👌
    path('cart-total-sum/', shop_view.Total_sum.as_view()), #👌
    path('categories/', shop_view.CategoryListApiView.as_view()),
]
