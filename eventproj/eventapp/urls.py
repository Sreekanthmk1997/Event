

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from eventapp import views



urlpatterns = [
    path('',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('wedding/',views.wedding,name='wedding'),
    path('floral/',views.floral,name='floral'),
    path('homedec/',views.homedec,name='homedec'),
    path('party/',views.party,name='party'),
    path('styling/',views.styling,name='styling'),
    path('favors/',views.favors,name='favors'),
    path('services/messenger/',views.services,name='messenger'),
    path('alert/',views.confirm,name='alert'),
    path('review/',views.review,name='review'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)