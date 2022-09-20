from django.urls import path
from .views import *
from .apiviews import *
app_name = "product"

urlpatterns = [
    path('home/', homepage, name='home'),
    path('', login_page, name='login'),
    path('login/login_view/', login_view, name='login_view'),
    path('logout/', logout_view, name="logout"),
    path('produto/sell/<int:id>/', sell_product, name="sell_product"),
    path('produto/info/', history_info,name="history_info"),
    path('produto/create_view/', create_product_view, name="create_product_view"),
    path('produto/delete/<int:id>/', delete_product, name="delete_product"),
    path('produto/delete_regs/<int:id>/', delete_regs , name="delete_regs"),
    path('produto/add/<int:id>/', add_product, name="add_product"),
    path('produto/dashboard/',dashboard, name="dashboard"),
    #Apis views
    path('produto/api/v1/<int:pk>/',product_view_api_v1,name="produto_api_v1"),
    path('produto/api/v2/<int:pk>/',product_view_api_v2,name="produto_api_v2"),
    path('produto/api/v1/',product_list_views_api_v1,name="produto_api_list_v1"),
    path('produto/api/v2/',product_list_views_api_v2,name="produto_api_list_v2"),



]