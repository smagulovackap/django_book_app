"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from catalog import views
from django.urls import re_path as url

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit_author/<int:id>/', views.edit_author, name='edit_author'),
    path('create_author/', views.create_author, name='create_author'),
    path('delete_author/<int:id>/', views.delete_author, name='delete_author'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors_add/', views.authors_add, name='authors_add'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]
