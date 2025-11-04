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

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

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
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})

class RollingPaperList(ListView):
    model = RollingPaper
    template_name = 'papers/index.html'


class RollingPaperDetail(DetailView):
    context_object_name = 'paper'
    model = RollingPaper
    template_name = 'papers/detail.html'

class RollingPaperCreate(CreateView):
    model = RollingPaper
    fields = ['name', 'size', 'material', 'flavor', 'rating', 'brand']
    template_name = 'papers/rollingpaper_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RollingPaperUpdate(UpdateView):
    model = RollingPaper
    fields = ['size', 'material', 'flavor', 'rating', 'brand']
    template_name = 'papers/rollingpaper_form.html'

class RollingPaperDelete(DeleteView):
    model = RollingPaper
    success_url = reverse_lazy('paper-index')
    template_name = 'papers/rollingpaper_confirm_delete.html'

class BrandDetail(DeleteView):
    model = Brand
    template_name = 'brands/detail.html'
    context_object_name = 'brand'

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





    



        
