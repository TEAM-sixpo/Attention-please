from django.contrib import admin
from .models import UserUpload, Video, Feedback
# Register your models here.

admin.site.register(UserUpload)
admin.site.register(Video)
admin.site.register(Feedback)