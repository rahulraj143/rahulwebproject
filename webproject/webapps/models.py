from django.db import models



class webapps(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
    year=models.IntegerField()

    def __str__(self):
        return self.name