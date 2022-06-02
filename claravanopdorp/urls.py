"""claravanopdorp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import index, robots
from django.contrib.staticfiles.storage import staticfiles_storage
from os import listdir
from pathlib import Path
from django.views.generic import RedirectView
from django.urls import include

def get_favicon_paths():
    filenames = listdir(Path(__file__).parent.absolute().__str__() + "/../web/static/web/favicons/")
    return [path(
        name,
        RedirectView.as_view(url=staticfiles_storage.url("web/favicons/" + name)),
    ) for name in filenames]

app_name = "main"

from web.views import index, robots, contact
from django.contrib.staticfiles.storage import staticfiles_storage
from os import listdir
from pathlib import Path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("robots.txt", robots.robots_txt),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="/home"), name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += get_favicon_paths() + [
    path("contact", contact.contact, name="contact"),
    path('<work>/<case>', index.Home.as_view()),
    path('<page>/<case>', index.Home.as_view()),
    path('<page>/<about>', index.Home.as_view()),
    path('<page>', index.Home.as_view()),
    ]



