from django.db import models

# Create your models here.
class Profile(models.Model):

    BG_CHOICES = (
        ('blue' ,'Blue'),
        ('green' ,'Green'),
        ('red' ,'Red'),
        ('yellow' ,'Yellow'),
        ('purple' ,'Purple'),
        ('orange' ,'Orange'),
        ('pink' ,'Pink'),
        ('gray' ,'Gray'),
        ('black' ,'Black'),
        ('white' ,'White'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=100)
    bg_color = models.CharField(max_length=50 , choices=BG_CHOICES)




    def __str__(self):
        return self.name
    
class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()

    #many to many , one to one , many to onee

    profile = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name='links')


    def __str__(self):
        return f"{self.text} - {self.url}"