from django.db import models
from django.contrib.auth.models import User #az mamadkhavari raftim settings.py didim ke hamchin chizi contrib.auth unja hast redan

# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('draft' , 'Draft'),
        ('published', 'Published')
    ) #inja neshon mide post ke shod che statusi mitune dashte bashe

    #ye title barash misazim
    title = models.CharField(max_length=250, unique=True)
    #slug yaeni hamon masalan ru link ha ke esm o kalame haye dorost o ina miad be jaye chizayue cherto pert
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #ondelete yaeni vaghty user hazf shod harchi user matlab ina zade una ro ham pak kon
    #modela mokhtalef dare mishe entkhab kard kar hasho ke chikar kone
    body = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True) #vaghty in post sakhte shod automatik mire zaman inasho zakhire mikone
#auto no add le true bashe yaeni dige nemishe tarikhesho taghir dad
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') #yaeni post ke sakhte shod default draft beshe

    #in def str bara in bood ke tu panele admins ma betunim esme khode post ro bebinim na inke bege post 1 post 2 post 3 injuri sakhte beine hezar ta post donbale ye post khas bashi
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        #it makes a url for each post
        from django.urls import reverse
        return reverse('post_detail', args=[self.created_data.year, self.created_data.strftime('%m'), self.created_data.strftime('%d'), self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"Comment written by {self.name} on {self.post}"


#hala model ro bayad migrate konim