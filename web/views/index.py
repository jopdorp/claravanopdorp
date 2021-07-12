from django.views.generic.base import TemplateView
from web.models.page import Page
from web.models.footer_section import FooterSection
from web.models.page_section import PageSection


class Home(TemplateView):
    template_name = "main.jinja2"

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):
        page_path = kwargs.get('page')
        if(page_path):
            self.current_page = Page.objects.get(path=page_path)
            self.page_sections = PageSection.objects.filter(page=self.current_page)

        self.pages = Page.objects.filter(is_in_menu=True)

        self.footer_sections = FooterSection.objects.all()
        return super(Home, self).dispatch(request, *args, **kwargs)
