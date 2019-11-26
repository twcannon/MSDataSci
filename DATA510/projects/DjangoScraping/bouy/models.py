from django.db import models


class CurrentWind(models.Model):
    Location=models.IntegerField()
    WDIR=models.CharField(default=None,null=True,blank=True,max_length=20)
    WSPD=models.CharField(default=None,null=True,blank=True,max_length=20)
    GST=models.CharField(default=None,null=True,blank=True,max_length=20)
    PRES=models.CharField(default=None,null=True,blank=True,max_length=20)
    WTMP=models.CharField(default=None,null=True,blank=True,max_length=20)
    WSPD10M=models.CharField(default=None,null=True,blank=True,max_length=20)
    WSPD20M=models.CharField(default=None,null=True,blank=True,max_length=20)


class HighestOneMinWind(models.Model):
    Location=models.IntegerField()
    TIME=models.CharField(default=None,null=True,blank=True,max_length=15)
    WSPD=models.FloatField(default=None,null=True,blank=True)
    WDIR=models.CharField(default=None,null=True,blank=True,max_length=3)


class CurrentCondition(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField(default=None,null=True,blank=True)
    WDIR=models.CharField(default=None,null=True,blank=True,max_length=3)
    WSPD=models.FloatField(default=None,null=True,blank=True)
    GST=models.FloatField(default=None,null=True,blank=True)
    WVHT=models.FloatField(default=None,null=True,blank=True)
    DPD=models.FloatField(default=None,null=True,blank=True)
    APD=models.FloatField(default=None,null=True,blank=True)
    MWD=models.CharField(default=None,null=True,blank=True,max_length=3) 
    PRES=models.FloatField(default=None,null=True,blank=True)
    PTDY=models.FloatField(default=None,null=True,blank=True)
    ATMP=models.FloatField(default=None,null=True,blank=True)
    WTMP=models.FloatField(default=None,null=True,blank=True)
    DEWP=models.FloatField(default=None,null=True,blank=True)
    SAL=models.FloatField(default=None,null=True,blank=True)
    VIS=models.FloatField(default=None,null=True,blank=True)
    TIDE=models.FloatField(default=None,null=True,blank=True)


class CurrentWave(models.Model):
    Location=models.IntegerField()
    WVHT=models.FloatField(default=None,null=True,blank=True)
    SwH=models.FloatField(default=None,null=True,blank=True)
    SwP=models.FloatField(default=None,null=True,blank=True)
    SwD=models.CharField(default=None,null=True,blank=True,max_length=3)
    WWH=models.FloatField(default=None,null=True,blank=True)
    WWP=models.FloatField(default=None,null=True,blank=True)
    WWD=models.CharField(default=None,null=True,blank=True,max_length=3)
    APD=models.FloatField(default=None,null=True,blank=True)


class DetailWave(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField(default=None,null=True,blank=True)
    WVHT=models.FloatField(default=None,null=True,blank=True)
    SwH=models.FloatField(default=None,null=True,blank=True)
    SwP=models.FloatField(default=None,null=True,blank=True)
    SwD=models.CharField(default=None,null=True,blank=True,max_length=3)
    WWH=models.FloatField(default=None,null=True,blank=True)
    WWP=models.FloatField(default=None,null=True,blank=True)
    WWD=models.CharField(default=None,null=True,blank=True,max_length=3)
    STEEPNESS=models.CharField(default=None,null=True,blank=True,max_length=20)
    APD=models.FloatField(default=None,null=True,blank=True)