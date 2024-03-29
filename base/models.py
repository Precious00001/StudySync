from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Model representing a topic for chat rooms
class Topic(models.Model):
    name = models.CharField(max_length=200)  # Name of the topic

    def __str__(self):
        # Return the name of the topic when converted to a string
        return self.name  # Return the name of the topic when converted to a string


# Model representing a chat room
class Room(models.Model):
    # User who created the room
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Topic of the room
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # Name of the room
    name = models.CharField(max_length=200)
    # Description of the room
    description = models.TextField(null=True, blank=True)
    # Users participating in the room
    participants = models.ManyToManyField(User, related_name='participants')
    # Date and time when the room was last updated
    updated = models.DateTimeField(auto_now=True)
    # Date and time when the room was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordering of instances by 'updated' and 'created' fields
        ordering = ['-updated', '-created']

    def __str__(self):
        # Return the name of the room when converted to a string
        return self.name


# Model representing a message in a chat room
class Message(models.Model):
    # User who sent the message
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Room in which the message was sent
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # Content of the message
    body = models.TextField()
    # Date and time when the message was last updated
    updated = models.DateTimeField(auto_now=True)
    # Date and time when the message was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordering of instances by 'updated' and 'created' fields
        ordering = ['-updated', '-created']

    def __str__(self):
        # Return the first 50 characters of the message body when converted to a string
        return self.body[0:50]