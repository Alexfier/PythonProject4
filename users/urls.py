from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreteAPIView, UserDestroyAPIView,
                         UserUpdateAPIView, UserRetrieveAPIView,
                         UserListAPIView)

# Описание маршрутизации для User

app_name = UsersConfig.name

urlpatterns = [
    path('user/crete/', UserCreteAPIView.as_view(), name='user_crete'),
    path('user/list/', UserListAPIView.as_view(), name='user_list'),
    path('user/retriv/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retriv'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='user_destroy'),
]
