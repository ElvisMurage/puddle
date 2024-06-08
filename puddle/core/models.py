
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.created_at >= timezone.now() - timezone.timedelta(days=1)

# Create your models here.
