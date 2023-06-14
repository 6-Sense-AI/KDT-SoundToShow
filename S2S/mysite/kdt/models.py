from django.db import models

# Create your models here.
# 해당 내용은 db 구조에 따라 내용이 달라집니다.
# Create your models here.
class Audio(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'audio'