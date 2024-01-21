# your_app/management/commands/seed_db.py
from django.core.management.base import BaseCommand
from core.models import Todo
import random


class Command(BaseCommand):
    help = "Seed the database with 25,000 todos"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding the database..."))

        # Clear existing todos
        Todo.objects.all().delete()

        # Seed the database with 25,000 todos
        for i in range(1, 25001):
            title = f"Todo {i}"
            completed = random.choice([True, False])
            Todo.objects.create(title=title, completed=completed)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
