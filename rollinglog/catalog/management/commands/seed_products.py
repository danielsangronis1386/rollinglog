from django.core.management.base import BaseCommand
from catalog.models import Brand, Product

class Command(BaseCommand):
    help = 'Seeds canonical products'

    def handle(self, *args, **kwargs):
        data = {
            'Raw': [
                ('Classic King Size', 'Natural', 'King Size'),
                ('Classic 1 1/4', 'Natural', '1 1/4'),
                ('Classic Single Wide', 'Natural', 'Single Wide'),
                ('Organic Hemp King Size', 'Hemp', 'King Size'),
                ('Organic Hemp 1 1/4', 'Hemp', '1 1/4'),
                ('Black King Size', 'Natural', 'King Size'),
                ('Black 1 1/4', 'Natural', '1 1/4'),
                ('Black Organic Hemp King Size', 'Hemp', 'King Size'),
                ('Black Organic Hemp 1 1/4', 'Hemp', '1 1/4'),
                ('Ethereal King Size', 'Phenomenally Thin', 'King Size'),
            ],
            'OCB': [
                ('Premium King Size', 'Flax/Wood', 'King Size'),
                ('Premium Slim', 'Flax/Wood', 'Slim'),
                ('Premium 1 1/4', 'Flax/Wood', '1 1/4'),
                ('Organic Hemp King Size', 'Hemp', 'King Size'),
                ('Organic Hemp 1 1/4', 'Hemp', '1 1/4'),
                ('Virgin Unbleached King Size', 'Unbleached', 'King Size'),
                ('Bamboo King Size', 'Bamboo', 'King Size'),
                ('X-Pert Slim Fit', 'Ultra Thin', 'Slim'),
                ('Ultimate', 'Micro-thin', 'King Size'),
                ('Solaire', 'Hemp', 'King Size Slim'),
            ],
            'ZigZag': [
                ('Orange', 'Wood Pulp', '1 1/4'),
                ('White', 'Wood Pulp', 'Single Wide'),
                ('Blue', 'Wood Pulp', 'Single Wide'),
                ('Ultra Thin', 'Wood Pulp', '1 1/4'),
                ('Organic Hemp', 'Hemp', '1 1/4'),
                ('Organic Hemp King Size', 'Hemp', 'King Size'),
                ('French Orange', 'Wood Pulp', '1 1/4'),
                ('Unbleached', 'Unbleached', '1 1/4'),
                ('Kutcorners', 'Wood Pulp', 'Single Wide'),
                ('1 1/2', 'Wood Pulp', '1 1/2'),
            ],
            'Elements': [
                ('Ultra Thin Rice King Size', 'Rice', 'King Size'),
                ('Ultra Thin Rice 1 1/4', 'Rice', '1 1/4'),
                ('Red King Size', 'Hemp', 'King Size'),
                ('Red 1 1/4', 'Hemp', '1 1/4'),
                ('Blue King Size', 'Rice', 'King Size'),
                ('Green King Size', 'Alfalfa', 'King Size'),
                ('Pink King Size', 'Rice', 'King Size'),
                ('Artesano King Size', 'Rice', 'King Size'),
                ('Connoisseur King Size', 'Rice', 'King Size'),
                ('Single Wide Rice', 'Rice', 'Single Wide'),
            ]
        }

        created_count = 0
        for brand_name, products in data.items():
            brand, _ = Brand.objects.get_or_create(name=brand_name, defaults={'verified': True})
            for name, material, size in products:
                _, created = Product.objects.get_or_create(
                    name=name,
                    brand=brand,
                    defaults={
                        'material': material,
                        'size': size
                    }
                )
                if created:
                    created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} products.'))
