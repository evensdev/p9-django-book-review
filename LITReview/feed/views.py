from feed.models import Ticket, Review
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from . import forms, models
from django.contrib.auth.decorators import login_required, permission_required
from .forms import TicketForm, ReviewForm, FollowUsersForm
from authentication.models import User
from .models import UserFollows


# AFFICHER LES PUBLICATIONS

@login_required
def home(request):

    tickets = Ticket.objects.all().order_by('time_created').reverse()
    reviews = Review.objects.all()
    list = {}


    for ticket in tickets:
        list[ticket.id] = {'ticket': ticket, 'reviews': []}
        list_reviews = Review.objects.filter(ticket=ticket)
        list[ticket.id]['reviews'].append(list_reviews)

    ticket_form = TicketForm(request.POST, request.FILES)

    #print("##########PPPPPPPPPPP", ticket_form.errors)
    if ticket_form.is_valid():
        ticket = ticket_form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('home')

    users = UserFollows.objects.all().filter(user__pk=request.user.id)





    context = {
        'tickets': tickets,
        'reviews': reviews,
        'list': list,
        'ticket_form': ticket_form,
        'users': users,
    }


    return render(request, 'feed/home.html', context=context )




# POSTER LES PUBLICATIONS


@login_required
def ticketCreate(request):
    form = TicketForm(request.POST, request.FILES)
    ticket = Ticket.objects.all()

    if form.is_valid():
        """
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        """

        return redirect('home')

    return render(request, 'feed/ticket_create.html', {'form':form})




@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if(ticket.user != request.user):
        return redirect('home')
    edit_form = forms.EditTicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()

    if request.method == 'POST':

        edit_form = forms.EditTicketForm(request.POST, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')

        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
}
    return render(request, 'feed/edit_ticket.html', context=context)



@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'feed/view_ticket.html', {'ticket': ticket})





@login_required
def reviewCreate(request):
    form = ReviewForm(request.POST)
    review = Review.objects.all()
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('home')

    return render(request, 'feed/review_create.html', {'form':form})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    if(review.user != request.user):
        return redirect('home')
    edit_form = forms.EditReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()

    if request.method == 'POST':

        edit_form = forms.EditReviewForm(request.POST, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')

        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
}
    return render(request, 'feed/edit_review.html', context=context)










@login_required
def accountProfil(request):
    tickets = Ticket.objects.filter(user = request.user)
    reviews = Review.objects.all()
    list = {}

    #print("EEEEEEEEEEEEEEEE",tickets)

    for ticket in tickets:
        list[ticket.id] = {'ticket': ticket, 'reviews': []}
        list_reviews = Review.objects.filter(ticket=ticket)
        list[ticket.id]['reviews'].append(list_reviews)

    #print("EEEEEEEEEEEEEEEE", list)

    ticket_form = TicketForm(request.POST, request.FILES)

    if ticket_form.is_valid():
        ticket = ticket_form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('home')

    context = {
        'tickets': tickets,
        'reviews': reviews,
        'list': list,
        'ticket_form': ticket_form,
    }

    return render(request, 'feed/account_profil.html', context=context)


@login_required
def Editprofil(request):
    form = forms.EditProfil()

    context = {
        'form': form,
        'id': request.user.id
    }

    form = forms.EditProfil(request.POST, request.FILES)

    print("##########PPPPPPPPPPP", form.errors)
    if form.is_valid():
        user = form.save(commit=False)
        currentUser = User.objects.get(id = request.POST['id'])
        currentUser.email = user.email
        currentUser.username = user.username
        currentUser.profile_photo = user.profile_photo
        currentUser.save()
        return redirect('home')

    return render(request, 'feed/edit_profil.html', context=context)




@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)

    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST)

        if form.is_valid():
            try:
                follow = form.save(commit= False)
                follow.user = request.user
                follow.save()
                #print("SAVED")
                return redirect('follow_users')
            except:
                print("ERROR")


    users = UserFollows.objects.all().filter(user__pk = request.user.id)

    return render(request, 'feed/follow_users_form.html', context={'form': form, 'users':users})


@login_required
def unfollow_users(request, user_id):
    form = forms.FollowUsersForm(instance=request.user)
    if len(UserFollows.objects.filter(user = request.user, followed_user__id = user_id))>0:
        follow_user = UserFollows.objects.filter(user = request.user, followed_user__id = user_id)[0]
        follow_user.delete()
        return redirect('follow_users')
        #print(request.user, user_id, follow_user)
    users = UserFollows.objects.all().filter(user__pk=request.user.id)
    return render(request, 'feed/follow_users_form.html', context={'form': form, 'users': users})
