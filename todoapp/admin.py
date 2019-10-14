from django.contrib import admin
from todoapp import models

admin.site.register(models.UserProfile)
admin.site.register(models.UserTodoList)



