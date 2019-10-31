from django.db import models

class Event(models.Model):
    #'Event Name' verbose name (what would someone want to read?)
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    #optional field 
    description = models.TextField(blank=True)

    #Represents the name of the event instance(returns the name of the event itself in admin dashboard)
    def __str__(self):
        return self.name

#People invited to event
class People(models.Model):
    #Event associated with person
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=25)
    last_name = models.CharField('Last Name', max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


