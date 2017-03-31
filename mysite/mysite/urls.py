"""money URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from mysite import settings
from mysite.views import home_site
from users import views as vw2
from django.contrib.auth import views as vw1

urlpatterns = [
                  url(r'^$', home_site),
                  url(r'^admin/', admin.site.urls),
                  url(r'^person/', include('person.urls')),
                  url(r'^list/', include('list.urls')),
                  url(r'^accounts/login/$', vw1.login, {'template_name': 'myUser/login.html'}, name='users_login'),
                  url(r'^accounts/logout/$', vw1.logout, {'template_name': 'myUser/logout.html'}, name='users_logout'),
                  url(r'^accounts/register/$', vw2.register, {'template_name': 'myUser/registration_form.html'},
                      name='users_register'),
                  url(r'^accounts/register/complete/$', vw2.registration_complete,
                      {'template_name': 'myUser/registration_complete.html'}, name='users_registration_complete'),
                  url(r'^accounts/', include('users.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
