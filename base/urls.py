from django.urls import path
from .views import TaskList ,TaskDetail,TaskCreateView,TaskUpdateView,DeleteView,CustumLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',RegisterPage.as_view(), name='register'),
    path('login/',CustumLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>',TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreateView.as_view(), name='create-task'),
    path('edit-task/<int:pk>',TaskUpdateView.as_view(), name='edit-task'),
    path('delete-task/<int:pk>',DeleteView.as_view(), name='delete-task'),
]
 