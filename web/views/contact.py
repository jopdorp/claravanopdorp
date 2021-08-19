from django.shortcuts import redirect
from web.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template import loader


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email_address'],
                'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")

    form = ContactForm()
    template = loader.get_template('contact.jinja2')
    return HttpResponse(template.render({'form': form}, request))
