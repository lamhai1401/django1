# posts/models.py
from django.db import models

class Post(models.Model): 
    text = models.TextField()

    # def __getitem__(self, item):
    #     return getattr(self, item)

    # def set_variable(self, var_name, value):
    #         self[var_name]["value"] = value

    def __str__(self): 
        return self.text[:50]