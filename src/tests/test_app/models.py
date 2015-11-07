from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from simple_review.models import Review

class Information(models.Model):
    info = models.TextField()
    reviews = GenericRelation(Review)

