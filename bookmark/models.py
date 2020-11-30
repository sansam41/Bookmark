from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name=models.CharField(max_length=30)
    url=models.URLField()
    contents=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "사이트명 : "+self.site_name+", URL : "+self.url

    class Meta:
        ordering=["-created"]