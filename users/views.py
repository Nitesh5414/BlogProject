from django.shortcuts import redirect, render, reverse
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.models import User
from users.models import Profile
# Create your views here.


############### views for user register page ##################
class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/user_register.html'
    success_url   = '/login/'


class UserListView(ListView):
    model               = User
    template_name       = 'users/read_user.html'
    context_object_name  = 'users'

# class ProfilePageView(TemplateView):
#     template_name = 'users/profile.html'


def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,  instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)