from django.db import models



class News(models.Model):
    title = models.CharField(max_length=100,verbose_name='Sarlavha')
    body = models.TextField()

    date_published = models.DateTimeField(auto_now_add=True,verbose_name='Yaratilgan Vaqt')

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'