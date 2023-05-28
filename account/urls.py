from django.urls import path
from. import views

app_name='account'

urlpatterns = [
    path('user/list/', views.AccountList.as_view()),
]
