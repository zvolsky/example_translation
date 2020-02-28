from django.views.generic import TemplateView


class HelloWorldView(TemplateView):
    template_name = "pokus2/helloworld.html"
