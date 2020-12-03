from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name       = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="created_by")
    updated_at = models.DateTimeField(auto_now = True, null = True)
    updated_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="updated_by")
    deleted_at = models.DateTimeField(null = True)
    deleted_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='deleted_by')
    
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name