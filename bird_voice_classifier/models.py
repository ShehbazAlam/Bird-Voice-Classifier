from django.db import models
from django.contrib import auth

# Create your models here.
class Prediction(models.Model):

    dateAndTime = models.DateTimeField(("Date And Time"), auto_now=False, auto_now_add=True)
    user = models.ForeignKey("auth.User", verbose_name=("User"), on_delete=models.CASCADE)
    file = models.URLField(("File Url"), max_length=200)
    result = models.CharField(("Predicted Result"), max_length=150)
    confidence = models.CharField(("Model Confidence"), max_length=50)

    class Meta:
        verbose_name = ("Prediction")
        verbose_name_plural = ("Predictions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Prediction_detail", kwargs={"pk": self.pk})
