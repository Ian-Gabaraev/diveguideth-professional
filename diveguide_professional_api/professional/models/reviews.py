from django.db import models

from .professional import Professional


class Review(models.Model):
    pro = models.ForeignKey(
        to=Professional, on_delete=models.CASCADE, verbose_name="Professional"
    )
    content = models.TextField(verbose_name="Review content")
    created = models.DateTimeField(
        null=False, blank=False, auto_now_add=True, verbose_name="Created"
    )
    verified = models.BooleanField(default=False, verbose_name="Verified")

    def __str__(self):
        return "Review of %s %s" % (self.pro.first_name, self.pro.last_name)
