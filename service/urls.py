from django.urls import path

from . import views

app_label = 'Moti'

urlpatterns = [
    path(r'member/', views.MemberList.as_view()),
    path(r'member/<int:pk>/', views.MemberDetail.as_view())
]
