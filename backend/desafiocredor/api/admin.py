from django.contrib import admin

from .models import ProposalFields, Proposal, Response


@admin.register(ProposalFields)
class ProposalFieldsAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "nullable", "order")
    ordering = ["order"]


class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0
    fields = ("key", "value")
    readonly_fields = []

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    inlines = (ResponseInline,)
    list_display = ["id", "status"]
    ordering = ["-created_at"]
    list_filter = ("status",)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
