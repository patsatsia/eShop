from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_currentuser.middleware import get_current_user, get_current_authenticated_user

from django_currentuser.db.models import CurrentUserField

class Category(models.Model):
    name       = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = CurrentUserField()
    updated_at = models.DateTimeField(null = True)
    updated_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="updated_by")
    delete     = models.BooleanField(default=False, null=True)
    deleted_at = models.DateTimeField(null = True)
    deleted_by = models.ForeignKey(User, default = None, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='deleted_by')
    
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def soft_delete(self, deleter):
        self.delete = True
        self.deleted_by = deleter
        self.deleted_at = timezone.now()
        self.save()

    def get_updater(self, updater):
        self.updated_by = updater
        self.updated_at = timezone.now()
        self.save()