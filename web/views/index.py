from django.views.generic.base import TemplateView
from web.models.page import Page, PageSection
from web.models.footer_section import FooterSection
from web.models.work import Work, WorkSection
from web.models.tech import TechnologyIcons


class Home(TemplateView):
    template_name = "main.jinja2"

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):
        page_path = kwargs.get('page')
        print("page path:", page_path)
        self.page_path = page_path
        self.works = Work.objects.filter(is_published=True)

        try:
            self.case = Work.objects.get(title=kwargs.get('case'))
            print("work found by case name, continuing...", self.case)
            self.work_sections = self.case.worksection_set.all()
            print("work_sections found by case name, continuing...", self.work_sections)
            self.tech_icons = TechnologyIcons.objects.all()
            print("icons:", self.tech_icons)
        except Work.DoesNotExist:
            print("no work found by case name, continuing...")
        except WorkSection.DoesNotExist:
            print("no work section found, continuing...")

        try:
            self.current_page = Page.objects.get(path=page_path)
            print("current page found", self.current_page)
            self.page_sections = PageSection.objects.filter(page=self.current_page)
            print("page sections", self.page_sections)
        except Page.DoesNotExist:
            print("no page found, continuing...")

        self.menu_pages = Page.objects.filter(is_in_menu=True)
        self.footer_sections = FooterSection.objects.all()
        return super(Home, self).dispatch(request, *args, **kwargs)
