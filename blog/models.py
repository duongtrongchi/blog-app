from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "categories"


    def __str__(self) -> str:
        return self.name


ARTICAL_TYPES = [
    ("UN", "Unspecified"),
    ("TU", "Tutorials"),
    ("RS", "Research"),
    ("RW", "Review"),
]
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICAL_TYPES)
    categories = models.ManyToManyField(to=Category, blank=True, related_name="categories")
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)


    def type_to_string(self):
        if self.type == "UN":
            return "Unspecified"
        elif self.type == "TU":
            return "Tutorial"
        elif self.type == "RS":
            return "Research"
        elif self.type == "RW":
            return "Review"

    def __str__(self) -> str:
        return f"{self.author}: {self.title}: {self.created_datetime}"