from django.views.generic.base import TemplateView
from web.models.page import Page, PageSection
from web.models.footer_section import FooterSection
from web.models.work import Work


class Home(TemplateView):
    template_name = "main.jinja2"

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):
        page_path = kwargs.get('page')
        self.page_path = page_path
        self.works = Work.objects.filter(is_published=True)

        try:
            self.current_page = Page.objects.get(path=page_path)
            self.page_sections = PageSection.objects.filter(page=self.current_page)
        except Page.DoesNotExist:
            print("no page found, continuing...")

        self.menu_pages = Page.objects.filter(is_in_menu=True)
        self.footer_sections = FooterSection.objects.all()
        return super(Home, self).dispatch(request, *args, **kwargs)
