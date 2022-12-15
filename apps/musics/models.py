from django.db import models


# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'app_musics'
        db_table = "music"
        verbose_name = u'音乐表'
        verbose_name_plural = u'音乐表'
