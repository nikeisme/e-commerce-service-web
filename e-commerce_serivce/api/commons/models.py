from django.db import models



class TimeStampedModel(models.Model):
    """
    created_at, updated_at 필드 생성을 위한 기본 모델
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


