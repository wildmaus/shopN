from django.urls import path

from .views import (
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    ProfileView
)


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
<<<<<<< HEAD
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('profile/', ProfileView.as_view(), name='profile')
=======
    #path('cart/', CartView.as_view(), name='cart'),
    #path('add-to-cart/<str:ct_model>/<str:slug>', AddToCartView.as_view(), name='add_to_cart'),
    #path('remove-from-cart/<str:ct_model>/<str:slug>', DeleteFromCartView.as_view(), name='remove_from_cart'),
    #path('change-quantity/<str:ct_model>/<str:slug>', ChangeQuantityView.as_view(), name='change_quantity'),
    #path('checkout/', CheckoutView.as_view(), name='checkout'),
    #path('make-order/', MakeOrderView.as_view(), name='make_order'),
    #path('profile/', ProfileView.as_view(), name='profile')
>>>>>>> e33fc53af65886b854dda08f4dac1d9c42e2358e
]
