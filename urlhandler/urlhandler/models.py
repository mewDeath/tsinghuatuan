#-*- coding: UTF-8 -*-
from django.db import models


class User(models.Model):
    weixin_id = models.CharField(max_length=255)
    stu_id = models.CharField(max_length=255)
    status = models.IntegerField()
    seed = models.FloatField(default=1024)

class Activity(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.CharField(max_length=255)
    book_start = models.DateTimeField()
    book_end = models.DateTimeField()
    max_tickets_per_order = models.IntegerField(default=2)
    total_tickets = models.IntegerField()
    status = models.IntegerField()
    pic_url = models.CharField(max_length=255)
    remain_tickets = models.IntegerField()
    # Something about status:
    # -1: deleted
    # 0: saved but not published
    # 1: published but not determined

class Ticket(models.Model):
    user = models.ForeignKey(User)
    unique_id = models.CharField(max_length=255)
    activity = models.ForeignKey(Activity)
    status = models.IntegerField()
    seat = models.CharField(max_length=255)
    # Something about isUsed
    # 0: ticket order is cancelled
    # 1: ticket order is valid
    # 2: ticket is used

class Order(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    status = models.IntegerField()
    tickets = models.IntegerField()
    # Something about status
    # 0: canceled
    # 1: valid
