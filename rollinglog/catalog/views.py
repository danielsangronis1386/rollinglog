from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import RollingPaper
from .models import Brand
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('paper-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

class RollingPaperList(LoginRequiredMixin, ListView):
    model = RollingPaper
    template_name = 'papers/index.html'

    def get_queryset(self):
        return RollingPaper.objects.filter(user=self.request.user)


class RollingPaperDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'paper'
    model = RollingPaper
    template_name = 'papers/detail.html'

    def get_queryset(self):
        return RollingPaper.objects.filter(user=self.request.user)


class RollingPaperCreate(LoginRequiredMixin, CreateView):
    model = RollingPaper
    fields = ['name', 'size', 'material', 'flavor', 'rating', 'brand']
    template_name = 'papers/rollingpaper_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RollingPaperUpdate(LoginRequiredMixin, UpdateView):
    model = RollingPaper
    fields = ['size', 'material', 'flavor', 'rating', 'brand']
    template_name = 'papers/rollingpaper_form.html'

    def get_queryset(self):
        return RollingPaper.objects.filter(user=self.request.user)

class RollingPaperDelete(LoginRequiredMixin, DeleteView):
    model = RollingPaper
    success_url = reverse_lazy('paper-index')
    template_name = 'papers/rollingpaper_confirm_delete.html'

    def get_queryset(self):
        return RollingPaper.objects.filter(user=self.request.user)


class BrandDetail(LoginRequiredMixin, DetailView):
    model = Brand
    template_name = 'brands/detail.html'
    context_object_name = 'brand'

@login_required
def add_review(request, paper_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        paper = RollingPaper.objects.get(id=paper_id)
        Review.objects.create(
            comment=comment,
            rating=rating,
            paper=paper,
            user=request.user
        )
    return redirect('paper-detail', pk=paper_id)





    



        
