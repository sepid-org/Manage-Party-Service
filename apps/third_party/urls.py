from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.third_party.views.public_third_party import get_third_party

router = DefaultRouter()

urlpatterns = [
    path('get-third-party/', get_third_party),
]

urlpatterns += router.urls
