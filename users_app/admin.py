from django.contrib import admin
from users_app.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'social_link')
    list_filter = ('user',)
    search_fields = ('user', 'social_link')
