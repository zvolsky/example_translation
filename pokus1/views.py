from django.views.generic import TemplateView


class HelloWorldView(TemplateView):
    template_name = "pokus1/helloworld.html"
