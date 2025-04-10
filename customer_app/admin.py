from django.contrib import admin

from .models import HelpRequest

admin.site.register(HelpRequest)


admin.site.site_header = "Helpdesk Support Admin"
admin.site.site_title = "Helpdesk Admin Portal"
admin.site.index_title = "Welcome to the Helpdesk Support System"
