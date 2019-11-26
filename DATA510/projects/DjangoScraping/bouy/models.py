from django.db import models


class CurrentWind(models.Model):
    Location=models.IntegerField()
    WDIR=models.CharField(max_length=20)
    WSPD=models.CharField(max_length=20)
    GST=models.CharField(max_length=20)
    PRES=models.CharField(max_length=20)
    WTMP=models.CharField(max_length=20)
    WSPD10M=models.CharField(max_length=20)
    WSPD20M=models.CharField(max_length=20)


class HighestOneMinWind(models.Model):
    Location=models.IntegerField()
    TIME=models.CharField(max_length=15)
    WSPD=models.FloatField()
    WDIR=models.CharField(max_length=3)


class CurrentCondition(models.Model):
    Location=models.IntegerField()
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


class CurrentWave(models.Model):
    Location=models.IntegerField()
    WVHT=models.FloatField()
    SwH=models.FloatField()
    SwP=models.FloatField()
    SwD=models.CharField(max_length=3)
    WWH=models.FloatField()
    WWP=models.FloatField()
    WWD=models.CharField(max_length=3)
    APD=models.FloatField()


class DetailWave(models.Model):
    Location=models.IntegerField()
    WVHT=models.FloatField()
    SwH=models.FloatField()
    SwP=models.FloatField()
    SwD=models.CharField(max_length=3)
    WWH=models.FloatField()
    WWP=models.FloatField()
    WWD=models.CharField(max_length=3)
    STEEPNESS=models.CharField(max_length=20)
    APD=models.FloatField()