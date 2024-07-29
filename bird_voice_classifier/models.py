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
        return self.user.username

    def get_absolute_url(self):
        return reverse("Prediction_detail", kwargs={"pk": self.pk})


class Feedback(models.Model):

    predictiion = models.ForeignKey("bird_voice_classifier.Prediction", verbose_name=("Feedback On"), on_delete=models.CASCADE)
    review = models.CharField(("Feedback Review"), max_length=50)
    desc = models.TextField(("Feedback Description"), blank=True)
    correction = models.CharField(("Correct Result"), max_length=50, blank=True)

    class Meta:
        verbose_name = ("Feedback")
        verbose_name_plural = ("Feedbacks")

    def __str__(self):
        return self.predictiion.user.username

    def get_absolute_url(self):
        return reverse("Feedback_detail", kwargs={"pk": self.pk})
