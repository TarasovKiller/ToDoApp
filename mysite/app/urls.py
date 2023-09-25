from django.urls import path

from . import views

urlpatterns = [
    path("view/<int:id>", views.index, name="index"),
    path("view/",views.lists,name="view"),
    path("create/",views.create,name="create"),
    path("delete/to_do/<int:id>",views.delete_to_do,name="delete_to_do"),
    path("delete/item",views.delete_item,name="delete_item"),
    path("home/",views.home,name="home"),
    path("",views.home,name="home"),
]