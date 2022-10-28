from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:user_uuid>', views.User.as_view()),
]