from django.db import models
from multiselectfield import MultiSelectField


class Program(models.Model):
    id = models.CharField(max_length=2000, primary_key=True,unique=True)
    program_name = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.program_name

class Centre(models.Model):
    id = models.CharField(max_length=2000, primary_key=True,unique=True)
    centre_name = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.centre_name

class Professor(models.Model):
    id = models.CharField(max_length=2000,  primary_key=True,unique=True)
    professor_name = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.professor_name



class Activity(models.Model):
    DAYS= (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    batch = models.CharField(max_length=2000, null=True)
    centre  = models.ForeignKey(Centre, on_delete=models.CASCADE)
    classroom  = models.CharField(max_length=2000, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    day = MultiSelectField(choices = DAYS, max_choices=7,
                                 max_length=2000)
    start_time = models.TimeField()
    end_time = models.TimeField()
    

    def __str__(self):
        return '{}{}{}'.format(self.program, self.day, self.start_time)
    class Meta:
       unique_together = ("professor", "day", "start_time", "end_time")