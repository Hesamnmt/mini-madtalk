from django.urls import path
from . import views


app_name='home'
urlpatterns = [
    path('section/list/', views.ListSection.as_view()),
    path('section/detail/', views.DetailSection.as_view()),
    path('school/list/', views.ListSchool.as_view()),
    path('school/detail/', views.DetailSchool.as_view()),
    path('subject/list/', views.ListSubject.as_view()),
    path('subject/detail/', views.DetailSubject.as_view()),
    path('article/list/', views.ListArticle.as_view()),
    path('article/detail/', views.DetailArticle.as_view()),
    path('homework/list/', views.ListHomework.as_view()),
    path('homework/detail/', views.DetailHomework.as_view()),
    
    # path('student/list/', views.ListStudent.as_view()),
    # path('student/detail/', views.DetailStudent.as_view()),
    # path('manager/list/', views.ListManager.as_view()),
    # path('manager/detail/', views.DetailManager.as_view()),
    # path('teacher/list/', views.ListTeacher.as_view()),
    # path('teacher/detail/', views.DetailTeacher.as_view()),
]
