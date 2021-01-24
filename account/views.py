from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import (
    LogoutView as DLogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import CustomerCreateForm, CustomeProfileForm
from .models import User, Customer

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are logged in already")
            return redirect("estore:home")
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {username}")
            return redirect('estore:home')
        else:
            messages.warning(request, "Login credentials are incorrect")
        return redirect(request.META.get("HTTP_REFERER"))

class LogoutView(DLogoutView, LoginRequiredMixin):
    login_url = 'account:login'
    next_page = 'account:login'

class CustomerCreateView(CreateView):
    form_class = CustomerCreateForm
    queryset = User.objects.all()
    template_name = 'customer.html'
    success_url = reverse_lazy('estore:home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            username = form.data.get("username")
            password = form.data.get("password1")
            email = form.data.get("email")
            first_name = form.data.get('first_name')
            last_name = form.data.get("last_name")
            birth_date = form.data.get("birth_date")
            photo = form.files.get('photo')

            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)
            user.save()

            Customer.objects.create(user=user,
                                    first_name=first_name,
                                    last_name=last_name,
                                    birth_date=birth_date,
                                    photo=photo)
            messages.success(request, message=f"Congratulations {first_name}. Your Profile Created succesefully")

            html_email = render_to_string('registration_success_email.html', {"name": first_name, "surname": last_name})
            send_mail(f"Estore. Welcome to your profile {first_name}",
                      "",
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False, html_message=html_email)

            return redirect('estore:home')
        return render(request, self.template_name, {"form":form})

class CustomerProfileView(UpdateView, LoginRequiredMixin):
    login_url = 'account:login'
    template_name = 'customer.html'
    form_class = CustomeProfileForm
    initial = {}

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        self.initial.update({"email": user.email})
        return Customer.objects.get(user=user)

    def form_valid(self, form):
        user = User.objects.get(username=self.kwargs["username"])
        user.email = form.data.get("email")
        user.first_name, user.last_name = form.data.get('first_name'), form.data.get('last_name')
        user.save()
        return super().form_valid(form)

class CustomerDeleteView(DeleteView, LoginRequiredMixin):
    login_url = 'account:login'
    template_name = 'customer_delete.html'
    success_url = reverse_lazy("account:login")
    model = User

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.request.user.username)
        return user

class CusPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('account:password_reset_done')
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'

class CusPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CusPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy("account:password_reset_complete")

class CusPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'