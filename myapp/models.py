from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        super().save(update_fields=['is_deleted'])

    def save(self, *args, **kwargs):
        self.full_name = self.full_name.capitalize()
        super().save(*args, **kwargs)

    def restore(self, *args, **kwargs):
        self.is_deleted = False
        super().save(update_fields=['is_deleted'])

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        super().save(update_fields=['is_deleted'])

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def restore(self, *args, **kwargs):
        self.is_deleted = False
        super().save(update_fields=['is_deleted'])

    def __str__(self):
        return self.name