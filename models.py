import sys

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class TabbitUser(models.Model):
    UserID = models.ForeignKey(User, unique=True, verbose_name=_("user"))
    FacebookID = models.IntegerField()
    # FirstName
    # LastName
    # Email
    PayPalEmail = models.EmailField()
    DebtShufflingEnabled = models.BooleanField()
    LastActivity = models.DateTimeField()

    def __unicode__(self):
	return self.UserID
