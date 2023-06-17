from django.db import models

class Audio(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'audio'