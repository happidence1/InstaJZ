from django.views.generic import TemplateView

# HelloWorld is-a TemplateView: 继承了很多generic的东西
class HelloWorld(TemplateView):
    template_name = 'test.html'
