from django.shortcuts import redirect
from web.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template import loader
from web.models.footer_section import FooterSection
from web.models.page import Page
from django.utils.html import strip_tags
import re


def textify(html):
    # Remove html tags and continuous whitespaces
    text_only = re.sub('[ \t]+', ' ', strip_tags(html))
    # Strip single spaces in the beginning of each line
    return text_only.replace('\n ', '\n').strip()


def contact(request):
    menu_pages = Page.objects.filter(is_in_menu=True)
    footer_sections = FooterSection.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'claravanopdorp.projects@gmail.com', ['claravanopdorp.projects@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            email_template = loader.get_template('email_first_contact.jinja2')
            response_message = email_template.render({'full_name': form.cleaned_data['full_name']})
            subject = "Thanks for you interest"

            try:
                send_mail(subject, textify(response_message), 'claravanopdorp.projects@gmail.com',
                          [form.cleaned_data['email_address']], html_message=response_message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("/message-received")

    form = ContactForm()
    template = loader.get_template('main.jinja2')
    return HttpResponse(template.render({'form': form, 'name': 'contact', 'view': {
        'menu_pages': menu_pages,
        'footer_sections': footer_sections
    }}, request))
