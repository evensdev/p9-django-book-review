from django import forms
from django.contrib.auth import get_user_model
from .models import Ticket, Review, UserFollows, User


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class EditTicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)






class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'headline', 'body', 'rating']


class EditReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)






class EditProfil(forms.ModelForm):

    class Meta:
        model = User
        fields = ['profile_photo', 'username', 'email']


User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
