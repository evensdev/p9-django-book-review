from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from feed.views import ticketCreate, home, reviewCreate, accountProfil, edit_ticket, Editprofil, follow_users, edit_review
import authentication.views

import feed.views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', feed.views.home, name='home'),
    path('create', ticketCreate, name='create'),
    path('comment', reviewCreate, name='comment'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('account', accountProfil, name='account'),
    path('feed/<int:ticket_id>/edit/', feed.views.edit_ticket, name='edit_ticket'),
    path('feed/<int:review_id>/edit_review/', feed.views.edit_review, name='edit_review'),
    path('feed/edit_profil/', feed.views.Editprofil, name='edit_profil'),
    path('follow-users/', feed.views.follow_users, name='follow_users'),
    path('unfollow-users/<int:user_id>/', feed.views.unfollow_users, name='unfollow_users'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)