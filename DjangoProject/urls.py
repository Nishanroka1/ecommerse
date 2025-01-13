# from django.urls import path, include  # Import path from django.urls
# from django.contrib import admin
# from guitarshop import views as guitarshop_views
# from contact import views as contact_views


# from guitarshop import views as guitarshop_views  # Import from guitarshop views

# urlpatterns = [
#     path('', guitarshop_views.home, name='home'),  # Corrected view import
#     path('admin/', admin.site.urls),
#     path('', include('guitarshop.urls')),
#     path('contact/', include('contact.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from guitarshop.views import shop, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guitarshop.urls')),  # Includes URLs for the guitarshop app
    path('contact/', include('contact.urls')),
    path('shop/', shop, name='shop'),  # Includes URLs for the contact app
    path('about/', about, name='about'),
]
