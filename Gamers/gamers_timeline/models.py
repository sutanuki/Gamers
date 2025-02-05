from django.db import models

class Thread(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    count_comment = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length=1000)
    commented = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    def __str__(self):
        return self.content
    
class Anchor(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply_to = models.IntegerField()
    def __str__(self):
        return str(self.reply_to)
