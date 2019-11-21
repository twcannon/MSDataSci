from django.db import models


class CurrentWind(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField()
    WDIR=models.FloatField()
    WSPD=models.FloatField()
    GST=models.FloatField()
    PRES=models.FloatField()
    PTDY=models.FloatField()
    WTMP=models.FloatField()
    WSPD10M=models.FloatField()
    WSPD20M=models.FloatField()


class HighestOneMinWind(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField()
    WSPD=models.FloatField()
    WDIR=models.CharField(max_length=3)


class CurrentCondition(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField()
    WDIR=models.CharField(max_length=3)
    WSPD=models.FloatField()
    GST=models.FloatField()
    WVHT=models.FloatField()
    DPD=models.FloatField()
    APD=models.FloatField()
    MWD=models.CharField(max_length=3) 
    PRES=models.FloatField()
    PTDY=models.FloatField()
    ATMP=models.FloatField()
    WTMP=models.FloatField()
    DEWP=models.FloatField()
    SAL=models.FloatField()
    VIS=models.FloatField()
    TIDE=models.FloatField()


class CurrnetWave(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField()
    WVHT=models.FloatField()
    SwH=models.FloatField()
    SwP=models.FloatField()
    SwD=models.FloatField()
    WWH=models.FloatField()
    WWP=models.FloatField()
    WWD=models.CharField(max_length=3)
    APD=models.FloatField()


class DetailWave(models.Model):
    Location=models.IntegerField()
    DateTime=models.DateTimeField()
    WVHT=models.FloatField()
    SwH=models.FloatField()
    SwP=models.FloatField()
    SwD=models.CharField(max_length=3)
    WWH=models.FloatField()
    WWP=models.FloatField()
    WWD=models.CharField(max_length=3)
    STEEPNESS=models.CharField(max_length=20)
    APD=models.FloatField()