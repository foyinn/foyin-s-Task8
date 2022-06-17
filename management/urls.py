from django.urls import path
from .views import record, createpost

app_name = "management"

urlpatterns = [
    path("", record, name='hotel-record'),
    path("records/", record, name='hotel-record'),
    path("create-post/", createpost, name='create-post')
]