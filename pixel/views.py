from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView, UpdateView
from django.urls import reverse


from account.models import User



class LightCode(TemplateView):
    template_name = 'pixel/ui.html'
    extra_context = {
        'title': 'Image Editor'
    }
    # form_class = UserRegisterForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        # context['form'] = self.form_class()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        # request = self.request
        context = self.get_context_data()

        # form = self.form_class(request.POST)
        # if form.is_valid():
            
        #     return redirect('login')
        # else:
        #     messages.warning(request, 'You did not properly fill the sign up form.')
        
        # context['form'] = form
        
        return render(request, self.template_name, context)