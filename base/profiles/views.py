from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Q

from profiles.models import DonorProfile
from profiles.forms import (
                            UserForm,
                            DonorProfileForm
                            )


User = get_user_model()


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        
        profile_form = DonorProfileForm(request.POST,
                                        request.FILES,
              instance=request.user.donor_profile)                          
        

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request, 'Profile updated successfully.')  
            return redirect('profile_self')
        else:
            messages.error(request, 'Error occured.')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = DonorProfileForm(instance=request.user.donor_profile)
        

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile/update.html', context=context)


@login_required
def public_profile_view(request, id):
    get_user = get_object_or_404(User, id=id)

    profile = get_user.donor_profile
    profile.hobbies = [hobby.strip() for hobby in profile.hobbies.split(',')]

    context = {
        'user': get_user,
        'profile': profile
    }

    return render(request, 'profile/public_view.html', context=context)


@login_required
def self_profile_view(request):
    profile = request.user.donor_profile
    profile.hobbies = [hobby.strip() for hobby in profile.hobbies.split(',')]

    context = {
        'user': request.user,
        'profile': profile
    }

    return render(request, 'profile/self_view.html', context=context)


@login_required
def all_profile_view(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        q = False
        found = False
        total_found = 0
        if query:
            q = True
            found_profiles = User.objects.filter(Q(donor_profile__blood_group__icontains=query)|
                                                Q(id_num__iexact=query) |
                                                Q(name__icontains=query) |
                                                Q(donor_profile__hobbies__icontains=query)|
                                                Q(donor_profile__department__icontains=query)|
                                                Q(donor_profile__city__icontains=query)|
                                                Q(donor_profile__job_title__icontains=query)
                                                )
            total_found = found_profiles.count()
            found = True
            if total_found == 0:
                found = False
        else:
            found_profiles = User.objects.filter(is_superuser=False)
        
        context={
            'profiles':found_profiles,
            'total_found': total_found,
            'found': found,
            'q' : q
            }

    return render(request, 'profile/all_profile.html', context=context)

@login_required
def available(request):
    if request.method == 'POST' and request.user.is_authenticated:
        get_user = request.user
        profile = get_user.donor_profile
        profile.available = True

    return render(request, 'profile/self_view.html')

@login_required
def not_available(request):
    if request.method == 'POST' and request.user.is_authenticated:
        get_user = request.user
        profile = get_user.donor_profile
        profile.last_donated = datetime.utcnow()
        profile.available = False

    return render(request, 'profile/self_view.html')
