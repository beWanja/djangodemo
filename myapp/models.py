from django.db import models

# Create your models here.

# This is table containing first and last names as fields -- remember we're
# working with a SQLite3 Database -- all will be in db.sqlite3 file
class mydata(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

