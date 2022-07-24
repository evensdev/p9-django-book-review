from django.contrib import admin
from .models import Ticket, Review, User, UserFollows
from authentication.forms import SignupForm
from django.contrib.auth.admin import UserAdmin


# J'ajoute une option de recherche dans mon tableau d'administration

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created', 'image', 'published')
    search_fields = ['title']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'headline', 'time_created')
    search_fields = ['title']

class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')
    search_fields = ['user']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)