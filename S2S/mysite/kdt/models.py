from django.db import models

class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'audio'