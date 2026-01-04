"""
Cloudinary Configuration Module

This module configures Cloudinary for the rollinglog project.
Cloudinary is used for image upload, storage, and transformation.
"""

import cloudinary
import cloudinary.uploader
import cloudinary.api
import os


def configure_cloudinary():
    """
    Configure Cloudinary with credentials from environment variables.
    
    Environment variables required:
    - CLOUDINARY_CLOUD_NAME: Your Cloudinary cloud name
    - CLOUDINARY_API_KEY: Your Cloudinary API key
    - CLOUDINARY_API_SECRET: Your Cloudinary API secret
    """
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET'),
        secure=True  # Use HTTPS
    )
    
    # Verify configuration
    if not all([
        os.getenv('CLOUDINARY_CLOUD_NAME'),
        os.getenv('CLOUDINARY_API_KEY'),
        os.getenv('CLOUDINARY_API_SECRET')
    ]):
        print("WARNING: Cloudinary credentials not fully configured. Check your .env file.")
    else:
        print(f"✓ Cloudinary configured successfully for cloud: {os.getenv('CLOUDINARY_CLOUD_NAME')}")


# Auto-configure when module is imported
configure_cloudinary()
