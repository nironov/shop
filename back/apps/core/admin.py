from django.contrib import admin

# from solo.admin import SingletonModelAdmin

# from .models import Settings


# admin.site.register(Settings, SingletonModelAdmin)

# @admin.register(Settings)
# class SettingsAdmin(admin.ModelAdmin):
#     actions = None

#     def has_add_permission(self, request):
#         if self.model.objects.count() > 0:
#             return False
#         return super().has_add_permission(request)

#     def has_delete_permission(self, request, obj = None):
#         return False

#     def log_addition(self, *args):
#         return

#     def log_change(self, *args):
#         return

#     def log_deletion(self, *args):
#         return