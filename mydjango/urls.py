from django.contrib import admin
from django.urls import path

import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", app.views.index),
    path("app/<int:pk>/", app.views.post_detail),
    path("app/new/", app.views.post_new),
]
