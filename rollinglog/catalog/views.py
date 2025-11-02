from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import RollingPaper
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def paper_index(request):
    papers = RollingPaper.objects.all()
    return render(request, 'papers/index.html', {'papers':papers})


def paper_detail(request, paper_id):
    paper = RollingPaper.objects.get(id=paper_id)
    return render(request, 'papers/detail.html', {'paper': paper})

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





    



        
