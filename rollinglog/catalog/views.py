from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import RollingPaper
from .models import Brand
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

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





    



        
