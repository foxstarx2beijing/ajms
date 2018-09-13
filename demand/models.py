from django.db import models

class human(models.Model):
    company = models.CharField(max_length = 100, blank = True)
    deparment = models.CharField(max_length = 100, blank = True)
    name = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 20, blank = True)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.name
