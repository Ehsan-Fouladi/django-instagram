from django.db import models
from account.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actions")
    act = models.CharField(max_length=124)
    created = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name="target_obj")
    target_id = models.PositiveBigIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_ct", "target_id")

    class Meta:
        ordering = ["-created"]