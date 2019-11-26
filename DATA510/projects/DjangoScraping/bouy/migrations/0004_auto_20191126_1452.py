# Generated by Django 2.2.5 on 2019-11-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouy', '0003_auto_20191126_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentcondition',
            name='APD',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='ATMP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='DEWP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='DPD',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='DateTime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='GST',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='MWD',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='PRES',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='PTDY',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='SAL',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='TIDE',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='VIS',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='WDIR',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='WSPD',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='WTMP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentcondition',
            name='WVHT',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='APD',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='SwD',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='SwH',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='SwP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='WVHT',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='WWD',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='WWH',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwave',
            name='WWP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='GST',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='PRES',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='WDIR',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='WSPD',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='WSPD10M',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='WSPD20M',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currentwind',
            name='WTMP',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='APD',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='STEEPNESS',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='SwD',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='SwH',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='SwP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='WVHT',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='WWD',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='WWH',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='detailwave',
            name='WWP',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='highestoneminwind',
            name='TIME',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='highestoneminwind',
            name='WDIR',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='highestoneminwind',
            name='WSPD',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
