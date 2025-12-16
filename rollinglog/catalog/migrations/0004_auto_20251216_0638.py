from django.db import migrations

def populate_products(apps, schema_editor):
    # Canonical product backfill intentionally skipped
    # Manual or scripted reconciliation required
    pass

def reverse_products(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_brand_verified_brand_website_logentry_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_products, reverse_products),
    ]
