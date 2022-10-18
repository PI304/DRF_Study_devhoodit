from django.contrib import admin

from user.models import User, UserPrivate

admin.site.register(User)
admin.site.register(UserPrivate)