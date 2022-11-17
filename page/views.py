from django.shortcuts import render
from django.views import View


class index(View):
    def get(self, request):
        return render(request, 'page.html')


class rekruto(View):
    def get(self, request):
        name = request.GET.get('name', 'Undefined')
        message = request.GET.get('message', 'Undefined')
        context = {
                     'name': name,
                     'message': message
                 }
        return render(request, 'rekruto.html', context)



