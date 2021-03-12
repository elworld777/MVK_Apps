from django.db import models

class Maps(models.Model):
    title = models.CharField(max_length = 120)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to='romanmaps/gallery')
    maps = models.ForeignKey(Maps, on_delete=models.CASCADE, related_name='images') 