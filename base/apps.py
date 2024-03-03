from django.apps import AppConfig


# Define the configuration for the 'base' Django application
class BaseConfig(AppConfig):
    # Define the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define the name of the application
    name = 'base'
