from django.urls import path

from users.views import UserView


urlpatterns = [
        path('get-all/', UserView.as_view(), name='get-users'),
    ]