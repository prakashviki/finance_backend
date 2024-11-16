from django.contrib import admin
from .models import AgentModel

@admin.register(AgentModel)
class AgentModelAdmin(admin.ModelAdmin):
    list_display = ('agent_id','finance_name', 'name', 'dob', 'mobile_number', 'email','address', 'agent_type', 'created_on', 'modified_on')
    search_fields = ('name', 'email', 'agent_type')
    list_filter = ('agent_type', 'created_on')

