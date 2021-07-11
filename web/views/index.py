from django.views.generic.base import TemplateView
from web.models.page import Page

class Home(TemplateView):
    template_name = "main.jinja2"

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):
        page_path = kwargs.get('page')
        if(page_path):
            self.current_page = Page.objects.get(path=page_path)
        self.pages = Page.objects.filter(is_in_menu=True)
        return super(Home, self).dispatch(request, *args, **kwargs)
