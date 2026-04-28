from django.contrib import admin
from .models import About,Experience,Education,Project,LiveProject,ContactMessage

admin.site.register(About)
admin.site.register(Experience)

admin.site.register(Education)
admin.site.register(Project)
admin.site.register(LiveProject)
admin.site.register(ContactMessage)