from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('todolist', views.UserTodoListViewSet)

urlpatterns = [
  
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
