from django.urls import path,include
from . import views
urlpatterns =[
    path('add/',views.studentPage,name="studentPage"),
    path('viewall/',views.student_list,name="student_list"),
    path('view/<fetchid>',views.student_details,name="student_details"),
    path('admno/<fetchadmission_number>',views.student_search,name="student_search"),
    path('',views.studentregister_view,name="studentregister_view"),
    
]
