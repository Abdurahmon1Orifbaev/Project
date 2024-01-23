from django.db import models
from django.utils.translation import gettext_lazy as _

class BreakfastModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("name"))
    description = models.TextField(verbose_name=_("name"))
    price = models.SmallIntegerField(verbose_name=_("name"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "breajfast"
        verbose_name_plural = "breajfasts"
        
        
class LunchModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "lunch"
        verbose_name_plural = "lunchs"
        
class DinnerModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "dinner"
        verbose_name_plural = "dinners"
                
class bookingModel(models.Model):
    email = models.EmailField()
    data_come = models.DateField()
    data_go = models.DateField()
    guests = models.SmallIntegerField()
    room = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "booking"