from django.db import models

class VocationalTestResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    dominant_area = models.CharField(max_length=100)
    descripcion = models.TextField()
    counts_by_area = models.JSONField()
    selections = models.JSONField()

    def __str__(self):
        return f"Resultado: {self.dominant_area} - {self.created_at}"
