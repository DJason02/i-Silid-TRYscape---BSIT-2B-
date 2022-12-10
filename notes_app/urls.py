# notes_list/notes_app/urls.py
from django.urls import path
from notes_app import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="notes"),

    path("list/<int:list_id>/", views.ItemListView.as_view(), name="notes-list"),
    # CRUD patterns for NoTesLists
    path("list/add/", views.ListCreate.as_view(), name="notes-list-add"),
    path(
        "list/<int:pk>/delete/", views.ListDelete.as_view(), name="notes-list-delete"
    ),
    # CRUD patterns for NoTesItems
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreate.as_view(),
        name="notes-item-add",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="notes-item-update",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="notes-item-delete",
    ),
]
