from django.urls import path,include
from . import views
urlpatterns = [
    path('addpage',views.employeePage,name='employeePage'),
    path('viewall',views.employee_list,name='employee_list'),
    path('viewemployee/<fetchid>',views.employee_details,name='employee_details'),
    path('register',views.register,name='register'),
    path('update_search_api',views.update_search_api,name='update_search_api'),
    path('update_api',views.update_data_read,name='update_data_read'),
    path('update',views.update,name='update'),
    path('home',views.home,name='home'),
    path('header',views.header,name='header'),
    path('login_check',views.login_check,name='login_check'),
    path('login',views.login,name='login'),
    path('view',views.viewall,name="viewall"),
    path('update/',views.update,name='update'),
]