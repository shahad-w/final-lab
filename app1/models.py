from django.db import models

# Developer table
class Developer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

# Game table
class Game(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.title
