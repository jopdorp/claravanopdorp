from django.contrib import admin

from web.models.page import Page, PageSection
from web.models.footer_section import FooterSection


class PageSectionInline(admin.TabularInline):
    model = PageSection


class PageAdmin(admin.ModelAdmin):
    inlines = [
        PageSectionInline,
    ]


admin.site.register(Page, PageAdmin)
admin.site.register(PageSection)
admin.site.register(FooterSection)

