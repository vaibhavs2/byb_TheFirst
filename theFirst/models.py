from django.db import models



choice=(  
        ('I', "sem I"),
        ('II', "sem II"),
        ('III', "sem III"),
        ('IV', "sem IV"),
        ('V', "sem V"),
        ('VI', "sem VI"),('VII', "sem VII"),('VIII',"sem VIII"),)
        
class branch(models.Model):
    branches = models.CharField(max_length=100)
    def __str__(self):
        return self.branches
             
# Create your models here.
class GoodDeals(models.Model):
    semester = models.CharField(default='I', max_length=11, choices=choice)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    bookSets = models.BooleanField()
    priceTosell = models.FloatField()
    priceTOshow = models.FloatField()
    description = models.CharField(max_length=1000, null=True)
    TimeLimit = models.PositiveSmallIntegerField(default= 2)
    ImageUrl = models.URLField(unique = True)
    InStock = models.SmallIntegerField(default=1)
    def __str__(self):
        return self.branch.branches
        

class bestSelling(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    semester = models.CharField(default='I',max_length=11, choices=choice)
    bookName = models.CharField(max_length = 120)
    bookPrice = models.FloatField()
    newedition = models.BooleanField(default=True)
    InStock = models.SmallIntegerField( default=1)
    def __str__(self):
        return self.bookName
