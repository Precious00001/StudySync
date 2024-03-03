from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.loginPage, name="login"),       # URL for login page
    path('logout/', views.logoutUser, name="logout"),    # URL for logout page
    path('register/', views.registerPage, name="register"),  # URL for registration page
    
    # Main application URLs
    path('', views.home,  name="home"),                  # URL for home page
    path('room/<str:pk>/', views.room, name="room"),     # URL for individual room page
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),  # URL for user profile page
    
    # Room management URLs
    path('create-room/', views.createRoom, name="create-room"),  # URL for creating a new room
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),  # URL for updating a room
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),  # URL for deleting a room
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),  # URL for deleting a message
    
    # User profile management URL
    path('update-user/', views.updateUser, name="update-user"),  # URL for updating user profile
    
    # Other URLs
    path('topics/', views.topicsPage, name="topics"),    # URL for displaying topics
    path('activity/', views.activityPage, name="activity"),  # URL for displaying activity
]
