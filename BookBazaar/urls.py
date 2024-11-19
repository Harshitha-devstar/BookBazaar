"""
URL configuration for BookBazaar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from baseapp import views
app_name = 'baseapp'
urlpatterns = [
    path("admin/", admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path("", views.home_view, name = 'home'),
    path('home/', views.afterlogin_home_view, name = 'afterlogin_home'),
    # path("login/", views.CustomLoginView.as_view(), name='custom_login'),
    path("about/", views.about_view, name = 'about'),
    path("contact/", views.contact_view, name = 'contact'),
    path("buy/", views.buy_view, name = 'buy'),
    path("sell/", views.book_add_view, name = 'sell'),
    # path("accounts/", include('django.contrib.auth.urls'), name = 'login'),
    # path("accounts/profile/", views.dashboard_view, name = 'profile')
    
    path("sell-list/", views.sale_list_view, name = 'sale-list'),
    path("books/", views.book_list_view, name = 'book_list'),
    path("<slug:category_slug>/", views.book_list_view, name = 'book_list_by_category'),
    path("<int:id>/<slug:slug>/", views.book_detail, name = 'book_detail'),
    
    path("sale/<slug:category_slug>/", views.sale_list_view, name = 'sale-book_list_by_category'),
    path("sale/<int:id>/<slug:slug>/", views.sale_book_detail, name = 'sale_book_detail'),
    path("sale/update/<int:id>/<slug:slug>/", views.sale_update_view, name = "sale_update"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name = 'baseapp/home.html'), name = 'login'),
    
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page = '/'), name = 'logout'),
    path("accounts/profile/", login_required(views.UserView.as_view()), name = 'profile'),
    path("accounts/signup/", views.signup, name = 'signup'),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    )
