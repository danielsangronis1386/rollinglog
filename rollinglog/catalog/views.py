from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import LogEntry
from .models import Brand
from .models import Review
from .models import Product
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

class LogEntryList(LoginRequiredMixin, ListView):
    model = LogEntry
    template_name = 'papers/index.html'
    context_object_name = 'papers' # Maintain compatibility if template uses 'papers' or 'object_list'

    def get_queryset(self):
        return LogEntry.objects.filter(user=self.request.user)


class LogEntryDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'paper'
    model = LogEntry
    template_name = 'papers/detail.html'

    def get_queryset(self):
        return LogEntry.objects.filter(user=self.request.user)


class LogEntryCreate(LoginRequiredMixin, CreateView):
    model = LogEntry
    fields = ['name', 'size', 'material', 'flavor', 'rating', 'brand', 'image']
    template_name = 'papers/rollingpaper_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LogEntryUpdate(LoginRequiredMixin, UpdateView):
    model = LogEntry
    fields = ['size', 'material', 'flavor', 'rating', 'brand', 'image']
    template_name = 'papers/rollingpaper_form.html'

    def get_queryset(self):
        return LogEntry.objects.filter(user=self.request.user)

class LogEntryDelete(LoginRequiredMixin, DeleteView):
    model = LogEntry
    success_url = reverse_lazy('paper-index')
    template_name = 'papers/rollingpaper_confirm_delete.html'

    def get_queryset(self):
        return LogEntry.objects.filter(user=self.request.user)

class BrandList(LoginRequiredMixin, ListView):
    model = Brand
    template_name = 'brands/index.html'
    context_object_name = 'brand'


class BrandDetail(LoginRequiredMixin, DetailView):
    model = Brand
    template_name = 'brands/detail.html'
    context_object_name = 'brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['papers'] = LogEntry.objects.filter(brand=self.object)
        return context
 
class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    fields = ['name', 'origin_country', 'description']
    template_name = 'brands/brand_form.html'
    success_url = reverse_lazy('brand-index')

    

class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = Brand
    fields = ['name', 'origin_country', 'description']
    template_name = 'brands/brand_form.html'
    success_url = reverse_lazy('brand-index')


class BrandDelete(LoginRequiredMixin, DeleteView):
    model = Brand
    success_url = reverse_lazy('brand-index')
    template_name = 'brands/brand_confirm_delete.html'


@login_required
def add_review(request, paper_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        paper = LogEntry.objects.get(id=paper_id)
        Review.objects.create(
            comment=comment,
            rating=rating,
            paper=paper,
            user=request.user
        )
    return redirect('paper-detail', pk=paper_id)

from django.http import JsonResponse

def product_list_api(request):
    material = request.GET.get('material')
    size = request.GET.get('size')
    products = Product.objects.all()
    
    if material:
        products = products.filter(material__icontains=material)
    if size:
        products = products.filter(size__icontains=size)
        
    data = list(products.values('id', 'name', 'brand__name', 'material', 'size', 'flavor', 'manufacturer_image'))
    return JsonResponse({'products': data})





    



        
