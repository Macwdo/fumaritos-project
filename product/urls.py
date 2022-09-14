from django.urls import path
from .views import *
app_name = "product"

urlpatterns = [
    path('home/', homepage, name='home'),
    path('', login_page, name='login'),
    path('login/login_view/', login_view, name='login_view'),
    path('logout/', logout_view, name="logout"),
    path('produto/sell/<int:id>/', sell_product, name="sell_product"),
    path('produto/info/', history_info,name="history_info"),
    path('produto/create/', create_product,name="create_product"),
    path('produto/create_view/', create_product_view, name="create_product_view"),
    path('produto/delete/<int:id>/', delete_product, name="delete_product"),
    path('produto/delete_regs/<int:id>/', delete_regs , name="delete_regs"),
    path('produto/add/<int:id>/', add_product, name="add_product")
]