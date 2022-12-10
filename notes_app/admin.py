# todo_list/todo_app/admin.py

from django.contrib import admin
from notes_app.models import NotesItem,NotesList

admin.site.register(NotesItem)
admin.site.register(NotesList)
