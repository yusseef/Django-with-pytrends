from django.db import models

class Region(models.Model):
    geoName = models.CharField(max_length=200)
    miami_heat = models.IntegerField()
    boston_celtics = models.IntegerField()

    def __str__(self):
        return self.geoName
class Historical(models.Model):
    date = models.DateTimeField()
    miami_heat = models.IntegerField()
    isPartial = models.BooleanField()

    '''Top put historical.csv file in database
        $ first put the file in following directory C:\Program Files\PostgreSQL\13\data\datasets
        $open postgresl and type following commands 
            COPY historical_trends from 'C:\Program Files\PostgreSQL\13\data\datasets\historical.csv CSV header'
    '''
 