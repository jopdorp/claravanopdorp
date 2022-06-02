from django.contrib import admin

from web.models.page import Page, PageSection
from web.models.footer_section import FooterSection
from web.models.work import Work, WorkSection
from web.models.tech import TechnologyIcons, TechnologyIconsAbout
from web.models.about import About, AboutSection


class PageSectionInline(admin.TabularInline):
    model = PageSection


class PageAdmin(admin.ModelAdmin):
    inlines = [
        PageSectionInline,
    ]


admin.site.register(Page, PageAdmin)
admin.site.register(PageSection)
admin.site.register(FooterSection)


class WorkSectionInline(admin.TabularInline):
    model = WorkSection

class WorkAdmin(admin.ModelAdmin):
    inlines = [
        WorkSectionInline,
    ]

admin.site.register(Work, WorkAdmin)
admin.site.register(WorkSection)
admin.site.register(TechnologyIcons)
admin.site.register(TechnologyIconsAbout)
admin.site.register(About)
admin.site.register(AboutSection)
