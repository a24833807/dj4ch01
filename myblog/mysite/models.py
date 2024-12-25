from django.db import models



#  建立資料庫模型(類別)
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
    def __str__(self):
        return self.title