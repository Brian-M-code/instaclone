from django.contrib import admin
from .models import Image,Profile,Comments

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal=("followers","following")

# Register your models here.
admin.site.register(Profile,admin_class=ProfileAdmin)
admin.site.register(Image)
admin.site.register(Comments)