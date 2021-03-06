skifflog
========

This is a website that enables Skiff mates to track their time.

For mates with limited plans, there's a function to round their logs "up"
within a day, in order to spread hours a little more generously. However,
the default rounding is set to 24 hours to represent that a day is a day.

Because the rounding only affects the total time spent within a day, one is
able to log multiple entries in a day and have that count as a single day.

Logins are done via Mozilla Persona, as per the who.theskiff.org site.

Time is saved between sessions, so if you close your browser or reboot,
the site assumes you are still active.

In future there will be the ability to delete or amend time slots in the case
of forgetting to "sign out".


Screenshot
----------
![Dashboard](https://raw.github.com/radiosilence/skifflog/master/skifflog/static/images/dashboard.png)


Tools Used
----------

Compass, Zurb Foundation, Django-Rest-Framework 2.x, RequireJS, django-allauth
