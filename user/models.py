from django.db import models

class Diagnostic(models.Model):
    plant_image = models.TextField(null=True, blank=True)
    is_infected = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    plant = models.ForeignKey(
        'plant.Plant',
        on_delete=models.CASCADE,
        related_name='diagnostics'
    )

    disease = models.ForeignKey(
        'plant.Disease',
        on_delete=models.CASCADE,
        related_name='diagnostics',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'diagnostics'
        verbose_name = 'diagnostic'
        verbose_name_plural = 'diagnostics'