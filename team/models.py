from django.db import models

class Team(models.Model):
    
    code = models.CharField(max_length=20)
    
    name = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            unique=False)
    
    country = models.CharField(max_length=50,
                            null=True,
                            blank=True,
                            unique=False)
    
    dateFounded = models.DateField(null=True,blank=True) 
    
    def __str__(self):
        return self.code

    