from django.core.management.base import BaseCommand
from catalog.models import Brand, Product

class Command(BaseCommand):
    help = 'Seeds canonical products with Cloudinary image URLs'

    def handle(self, *args, **kwargs):
        # Cloudinary base URL for rollinglog folder
        cloudinary_base = "https://res.cloudinary.com/dhqhqyexq/image/upload/v1/rollinglog/products"
        
        data = {
            'Raw': [
                ('Classic King Size', 'Natural', 'King Size', f'{cloudinary_base}/raw_classic_king.jpg'),
                ('Classic 1 1/4', 'Natural', '1 1/4', f'{cloudinary_base}/raw_classic_114.jpg'),
                ('Classic Single Wide', 'Natural', 'Single Wide', f'{cloudinary_base}/raw_classic_single.jpg'),
                ('Organic Hemp King Size', 'Hemp', 'King Size', f'{cloudinary_base}/raw_hemp_king.jpg'),
                ('Organic Hemp 1 1/4', 'Hemp', '1 1/4', f'{cloudinary_base}/raw_hemp_114.jpg'),
                ('Black King Size', 'Natural', 'King Size', f'{cloudinary_base}/raw_black_king.jpg'),
                ('Black 1 1/4', 'Natural', '1 1/4', f'{cloudinary_base}/raw_black_114.jpg'),
                ('Black Organic Hemp King Size', 'Hemp', 'King Size', f'{cloudinary_base}/raw_black_hemp_king.jpg'),
                ('Black Organic Hemp 1 1/4', 'Hemp', '1 1/4', f'{cloudinary_base}/raw_black_hemp_114.jpg'),
                ('Ethereal King Size', 'Phenomenally Thin', 'King Size', f'{cloudinary_base}/raw_ethereal_king.jpg'),
            ],
            'OCB': [
                ('Premium King Size', 'Flax/Wood', 'King Size', f'{cloudinary_base}/ocb_premium_king.jpg'),
                ('Premium Slim', 'Flax/Wood', 'Slim', f'{cloudinary_base}/ocb_premium_slim.jpg'),
                ('Premium 1 1/4', 'Flax/Wood', '1 1/4', f'{cloudinary_base}/ocb_premium_114.jpg'),
                ('Organic Hemp King Size', 'Hemp', 'King Size', f'{cloudinary_base}/ocb_hemp_king.jpg'),
                ('Organic Hemp 1 1/4', 'Hemp', '1 1/4', f'{cloudinary_base}/ocb_hemp_114.jpg'),
                ('Virgin Unbleached King Size', 'Unbleached', 'King Size', f'{cloudinary_base}/ocb_virgin_king.jpg'),
                ('Bamboo King Size', 'Bamboo', 'King Size', f'{cloudinary_base}/ocb_bamboo_king.jpg'),
                ('X-Pert Slim Fit', 'Ultra Thin', 'Slim', f'{cloudinary_base}/ocb_xpert_slim.jpg'),
                ('Ultimate', 'Micro-thin', 'King Size', f'{cloudinary_base}/ocb_ultimate_king.jpg'),
                ('Solaire', 'Hemp', 'King Size Slim', f'{cloudinary_base}/ocb_solaire_king.jpg'),
            ],
            'ZigZag': [
                ('Orange', 'Wood Pulp', '1 1/4', f'{cloudinary_base}/zigzag_orange_114.jpg'),
                ('White', 'Wood Pulp', 'Single Wide', f'{cloudinary_base}/zigzag_white_single.jpg'),
                ('Blue', 'Wood Pulp', 'Single Wide', f'{cloudinary_base}/zigzag_blue_single.jpg'),
                ('Ultra Thin', 'Wood Pulp', '1 1/4', f'{cloudinary_base}/zigzag_ultra_114.jpg'),
                ('Organic Hemp', 'Hemp', '1 1/4', f'{cloudinary_base}/zigzag_hemp_114.jpg'),
                ('Organic Hemp King Size', 'Hemp', 'King Size', f'{cloudinary_base}/zigzag_hemp_king.jpg'),
                ('French Orange', 'Wood Pulp', '1 1/4', f'{cloudinary_base}/zigzag_french_114.jpg'),
                ('Unbleached', 'Unbleached', '1 1/4', f'{cloudinary_base}/zigzag_unbleached_114.jpg'),
                ('Kutcorners', 'Wood Pulp', 'Single Wide', f'{cloudinary_base}/zigzag_kutcorners_single.jpg'),
                ('1 1/2', 'Wood Pulp', '1 1/2', f'{cloudinary_base}/zigzag_112.jpg'),
            ],
            'Elements': [
                ('Ultra Thin Rice King Size', 'Rice', 'King Size', f'{cloudinary_base}/elements_rice_king.jpg'),
                ('Ultra Thin Rice 1 1/4', 'Rice', '1 1/4', f'{cloudinary_base}/elements_rice_114.jpg'),
                ('Red King Size', 'Hemp', 'King Size', f'{cloudinary_base}/elements_red_king.jpg'),
                ('Red 1 1/4', 'Hemp', '1 1/4', f'{cloudinary_base}/elements_red_114.jpg'),
                ('Blue King Size', 'Rice', 'King Size', f'{cloudinary_base}/elements_blue_king.jpg'),
                ('Green King Size', 'Alfalfa', 'King Size', f'{cloudinary_base}/elements_green_king.jpg'),
                ('Pink King Size', 'Rice', 'King Size', f'{cloudinary_base}/elements_pink_king.jpg'),
                ('Artesano King Size', 'Rice', 'King Size', f'{cloudinary_base}/elements_artesano_king.jpg'),
                ('Connoisseur King Size', 'Rice', 'King Size', f'{cloudinary_base}/elements_connoisseur_king.jpg'),
                ('Single Wide Rice', 'Rice', 'Single Wide', f'{cloudinary_base}/elements_rice_single.jpg'),
            ]
        }

        created_count = 0
        updated_count = 0
        
        for brand_name, products in data.items():
            brand, _ = Brand.objects.get_or_create(name=brand_name, defaults={'verified': True})
            for name, material, size, image_url in products:
                product, created = Product.objects.get_or_create(
                    name=name,
                    brand=brand,
                    defaults={
                        'material': material,
                        'size': size,
                        'manufacturer_image_url': image_url
                    }
                )
                if created:
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f'✓ Created: {brand_name} {name}'))
                elif not product.manufacturer_image_url:
                    # Update existing products that don't have image URLs
                    product.manufacturer_image_url = image_url
                    product.save()
                    updated_count += 1
                    self.stdout.write(self.style.WARNING(f'⊙ Updated image URL: {brand_name} {name}'))
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Complete! Created: {created_count}, Updated: {updated_count} products.'
            )
        )
