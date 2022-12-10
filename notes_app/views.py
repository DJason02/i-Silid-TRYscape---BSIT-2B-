# notes_list/notes_app/views.py
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import NotesItem, NotesList



class ListListView(ListView):
    model = NotesList
    template_name = "notes_app/index.html"

class ItemListView(ListView):
    model = NotesItem
    template_name = "notes_app/notes_list.html"

    def get_queryset(self):
        return NotesItem.objects.filter(notes_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["notes_list"] = NotesList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = NotesList
    fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context


class ItemCreate(CreateView):
    model = NotesItem
    fields = [
        "notes_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super().get_initial()
        notes_list = NotesList.objects.get(id=self.kwargs["list_id"])
        initial_data["notes_list"] = notes_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        notes_list = NotesList.objects.get(id=self.kwargs["list_id"])
        context["notes_list"] = notes_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("notes-list", args=[self.object.notes_list_id])


class ItemUpdate(UpdateView):
    model = NotesItem
    fields = [
        "notes_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super().get_context_data()
        context["notes_list"] = self.object.notes_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.notes_list_id])


class ListDelete(DeleteView):
    model = NotesList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("notes")


class ItemDelete(DeleteView):
    model = NotesItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes_list"] = self.object.todo_list
        return context
