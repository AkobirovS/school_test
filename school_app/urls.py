from django.urls import path
from school_app.views import index

app_name = 'school_app'

urlpatterns = [
    path("", index, name="index"),
]