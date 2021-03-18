from django.apps import AppConfig


# class QuickstartConfig(AppConfig):
#     name = 'quickstart'

class QuickstartConfig(AppConfig):
    name = 'quickstart'

    def ready(self):
        pass
        # write your startup code here you can import application code here
        #from app_name.models import MyModel
        print('xin chao moi nguoi')
        print('alo alo alo')
