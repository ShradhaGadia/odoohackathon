from django.contrib import admin
from .models import Skill, SwapRequest, Feedback, AdminAction

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_approved')
    list_filter = ('is_approved',)

@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'status')
    list_filter = ('status',)

admin.site.register(Feedback)
admin.site.register(AdminAction)
