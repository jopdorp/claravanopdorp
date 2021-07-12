from django.contrib import admin

from web.models.page import Page
from web.models.footer_section import FooterSection
from web.models.page_section import PageSection

admin.site.register(Page)
admin.site.register(FooterSection)
admin.site.register(PageSection)
