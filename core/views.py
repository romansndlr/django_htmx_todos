from urllib.parse import urlencode
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView
from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todos"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_todo_id = self.request.GET.get("selected-todo", None)

        if selected_todo_id:
            selected_todo = get_object_or_404(Todo, id=selected_todo_id)
            context["selected_todo"] = selected_todo

        return context


class TodoUpdateView(View):
    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        completed = request.POST.get("completed", None)
        next = request.POST.get("next", reverse("todo_list"))

        if completed is not None:
            todo.completed = completed

        todo.save()

        return redirect(next)
