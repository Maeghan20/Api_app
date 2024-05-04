from django.db import models

class Event(models.Model):
    Event_ID = models.CharField(max_length=100)
    Title = models.CharField(max_length=200)
    Attendee_No = models.CharField(max_length=100)
    doe = models.DateField()
    Location = models.CharField(max_length=100)
    Organizer = models.CharField(max_length=100)
    Event_Category = models.CharField(max_length=100)

    def __str__(self):
        return self.Title
