# Django imports.
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Blog app imports.
from blog.forms.account.register_forms import UserRegisterForm


class UserRegisterView(View):
    """
      View to let users register
    """
    template_name = 'account/register.html'
    context_object = {
                       "register_form": UserRegisterForm()
                      }

    def get(self, request):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            username = register_form.cleaned_data.get('username')

            messages.success(request, f"Congratulations {username} !!! "
                                      f"Your account was created successfully")
            return redirect('blog:login')

        else:
            messages.error(request, "Please provide valid information.")
            # Redirect user to register page
            return render(request, self.template_name, self.context_object)