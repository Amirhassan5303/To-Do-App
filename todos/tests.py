from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title = "First todo",
            body = "Body text"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First todo")
        self.assertEqual(self.todo.body, "Body text")
        self.assertEqual(str(self.todo), "First todo")    
