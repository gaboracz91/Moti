"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls

from service import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('button', views.button, name='button'),
    path('howto', views.howto, name='howto'),
    path('generate_call_list', views.generate_call_list),
    path('reset_should_be_contacted', views.reset_should_be_contacted),
    path('create_test_people', views.create_test_people),
    path('api/v1/', include('service.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Im Ok Core')),
    path('', RedirectView.as_view(url=reverse_lazy(views.button), permanent=False)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
