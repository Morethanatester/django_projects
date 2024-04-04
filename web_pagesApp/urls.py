from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from web_pagesApp import views

urlpatterns = [
    path("", views.home, name='home'),
    path("newhome", views.newhome, name='newhome'),

    # portfolio urls paths from RealPython
    # path("", views.project_index, name="project_index"),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)