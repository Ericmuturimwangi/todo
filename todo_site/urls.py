
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('admin/', admin.site.urls),
    path('views/', admin.site.views),


]
