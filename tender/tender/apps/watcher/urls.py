from django.urls import path
from django.contrib import admin
from . import views
#Список страниц приложения watcher
urlpatterns = [
	path('contacts',views.contacts, name = 'contacts'),
	path('',views.index, name = 'index'),
	path('admin/', admin.site.urls, name = 'admin'),
	path('<int:category_id>/',views.category_page, name = 'category_page'),
	path('/<int:tender_id>/',views.tender_page, name = 'tender_page'),
	path('<int:category_id>/',views.analysis_page, name = 'analysis_page'),
	path('stats',views.stats, name = 'stats'),
	
]