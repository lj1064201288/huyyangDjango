from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

# Create your views here.

from .models import Student
from .forms import StudentForms


# def index(request):
#
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentForms(request.POST)
#         if form.is_valid():
#             # cleaned_data = form.cleaned_data
#             # student = Student()
#             # student.name = cleaned_data['name']
#             # student.sex = cleaned_data['sex']
#             # student.email = cleaned_data['email']
#             # student.profession = cleaned_data['profession']
#             # student.qq = cleaned_data['qq']
#             # student.phone = cleaned_data['phone']
#
#             form.save()
#
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             form = StudentForms()
#
#     # words = 'World'
#     return  render(request, 'index.html', context=locals())

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        content = {
            'students': students,
        }

        return content

    # 使用get请求触发的方法
    def get(self, request):
        context = self.get_context()
        form = StudentForms()
        context.update({
            'form': form,
        })

        return render(request, self.template_name, context=context)

    # 使用post请求触发的方法
    def post(self, request):
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

        context = self.get_context()
        context.update({
            'form', form,
        })

        return render(request, self.template_name, context=context)
