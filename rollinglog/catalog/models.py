from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250, blank=True)
    # New fields for Audit recommendations
    verified = models.BooleanField(default=False)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    material = models.CharField(max_length=50) # e.g., Hemp, Rice, Wood Pulp
    size = models.CharField(max_length=50) # e.g., King Size, 1 1/4
    flavor = models.CharField(max_length=100, blank=True)
    manufacturer_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.size})"

class LogEntry(models.Model):
    # Relational
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='log_entries')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='log_entries')
    
    # User-specific fields
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='paper_images/', blank=True, null=True) # User's photo
    created_at = models.DateTimeField(auto_now_add=True)

    # DEPRECATED FIELDS (Keep for migration, then delete)
    # --------------------------------------------------
    # The original 'brand' FK is kept to help migrate to Product.brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=100, default="Unknown") 
    size = models.CharField(max_length=50, blank=True)
    material = models.CharField(max_length=50, blank=True)
    flavor = models.CharField(max_length=100, blank=True)
    # --------------------------------------------------

    def get_absolute_url(self):
        # We'll update the URL name later, for now keep compatibility if possible or break it intentionally to fix views
        from django.urls import reverse
        return reverse('paper-detail', kwargs={'pk': self.id})

    def __str__(self):
        # Fallback to old name if product not set yet
        product_name = self.product.name if self.product else self.name
        return f"{self.user.username}'s log of {product_name}"
    
class Review(models.Model):
    # Review model might be redundant now that LogEntry IS a review, 
    # but the prompt didn't strictly say to delete it, only to refactor RollingPaper.
    # However, RollingPaper WAS the log. 
    # The existing Review model links to RollingPaper. 
    # "Review by User for RollingPaper". 
    # If RollingPaper becomes LogEntry, Review becomes specific comments?
    # Actually, RollingPaper had a 'rating' field too. 
    # Let's inspect the original models again.
    # Original RollingPaper: rating, user, brand, image.
    # Original Review: paper(FK), user, rating, comment.
    # It seems RollingPaper was the "Object" and Review was "Social Proof"?
    # "Each user can create... entries... including... personal ratings."
    # The prompt says: "Modify existing RollingPaper... Keeping user-specific fields only (rating, photo...)"
    # So LogEntry effectively absorbs the user's personal experience.
    # I will adapt Review to point to LogEntry if strictly needed, or Product?
    # "Review" -> "paper" (RollingPaper).
    # Since I renamed RollingPaper to LogEntry, Django will update this FK automatically.
    # I will leave Review as is for now to avoid "Refactoring unrelated features" unless it breaks.
    paper = models.ForeignKey(LogEntry, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username}"



    
    

    def __str__(self):
        return self.name
    

