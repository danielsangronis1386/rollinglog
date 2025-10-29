from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

#temporary mock class before we use Django models 

class RollingPaper:
    def __init__(self, name, brand, size, material, rating):
        self.name = name
        self.brand = brand
        self.size = size
        self.material = material
        self.rating = rating

    
#fake list of papers to render the UI 
papers = [
    RollingPaper('Raw Classic', 'RAW', '1 1/4', 'Hemp', 5),
    RollingPaper('OCB Organic', 'OCB', 'King Size', 'Organic Hemp', 4),
    RollingPaper('Vibes Ultra Thing', 'Vibes', 'King Size Slim', 'Rice',3),
    RollingPaper('Elements Rice', 'Elements', 'Single Wide', 'Rice', 4),
    ]

def paper_index(request):
    return render(request, 'paper/index.html', {'papers':papers})

        
