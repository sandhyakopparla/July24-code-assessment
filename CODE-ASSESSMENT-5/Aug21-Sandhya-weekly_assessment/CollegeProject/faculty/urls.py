from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.facultyPage,name="facultyPage"),
    path('viewall/',views.faculty_list,name="faculty_list"),
    path('view/<fetchid>',views.faculty_details,name="faculty_details"),
    path('fcode/<fetchfaculty_code>',views.faculty_search,name="faculty_search"),
    path('register',views.facultyregister_view,name="facultyregister_view"),
    path('login',views.facultylogin_view,name="facultylogin_view"),
    
]
