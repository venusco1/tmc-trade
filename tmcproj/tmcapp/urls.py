from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.signup, name='register'),
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    # path('contact/', views.contact, name='contact'),
    # path('useradmin/', views.useradmin, name='useradmin'),
    # path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    # path('toggle-course/<int:user_id>', views.toggle_course, name='toggle_course'),

    # path('videos/', views.videos, name='videos'),
    # path('videos/unlock/<int:video_id>/', views.unlock_video, name='unlock_video'),

]

