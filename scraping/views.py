from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .models import Vakation, Resume
from .form import findForm, resume_form
from django.http import HttpResponse
from django.views.generic import View



# Creating a class based view
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data={}
        pdf = render_to_pdf('accounts/resume.html')
        return HttpResponse(pdf, content_type='application/pdf')
def scraping_home(request):
    form = findForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    _context={'form': form,'city':request.GET.get('city'),'language':request.GET.get('language')}
    if city or language:
        _filter={}
        if city:
            _filter['city__slug']=city
        if language:
            _filter['language__slug'] = language
        v = Vakation.objects.filter(**_filter)
        vak = Paginator(v,7)
        p=request.GET.get('page')
        if p:
            page=p
        else:
            page=1
        page_number = vak.page(page)

        _context.update({'vakantion':page_number})
    return render(request,'scraping/home.html',_context)
#
class resume(DetailView):
    queryset = Resume.objects.all()
    template_name ='scraping/home.html'
    context_object_name = 'resume'

#
#

class L_List(ListView):
    queryset = Vakation.objects.all()
    model=Vakation
    form=findForm()
    template_name = 'scraping/home.html'
    paginate_by = 5
    context_object_name = 'vakantion'
    def get_context_data(self,**kwargs):
        context=super(L_List,self).get_context_data(**kwargs)
        context['city'] = self.request.GET.get('city')
        context['language']=self.request.GET.get('language')
        context['form']=self.form
        return context
    def get_queryset(self):
        city=self.request.GET.get('city')
        language=self.request.GET.get('language')
        qs=[]
        _filter={}
        if city or language:
            if city:
                _filter['city__slug']=city
            if language:
                _filter['language__slug']=language

            qs=Vakation.objects.filter(**_filter)
        return qs


def resume_edit(request):
    if request.method == 'POST':
        form= resume_form(request.POST or None)
        if form.is_valid():
            form.save()

            messages.success(request, 'succesfuly register')

            return HttpResponseRedirect(reverse('scraping:resume'))

    else:

        form= resume_form()
    context = {'form': form}

    return render(request, 'accounts/resume_edit.html', context)










@login_required
def resume(request):

    user=request.user
    data=Resume.objects.filter(email=user.email).first()
    if request.GET:
        form = resume_form(data=request.GET)
    return render(request,'accounts/resume.html',{'resume':data})

def resume_search(request):
    user = request.user
    data=Resume.objects.filter(email=user.email).first()
    if request.GET:
        form = resume_form(data=request.GET)
    return render(request,'accounts/resume.html',{'resume':data})


class resume_list(ListView):
    queryset = Resume.objects.all()
    model=Resume
    form=resume_form()
    template_name = 'scraping/resume.html'
    paginate_by = 5
    context_object_name = 'vakantion'

def resume_home(request):



    city = request.GET.get('city')
    language = request.GET.get('language')
    _context={'form': form,'city':request.GET.get('city'),'language':request.GET.get('language')}
    if city or language:
        _filter={}
        if city:
            _filter['city__slug']=city
        if language:
            _filter['language__slug'] = language
        v = Resume.objects.filter(**_filter)
        vak = Paginator(v,7)
        p=request.GET.get('page')
        if p:
            page=p
        else:
            page=1
        page_number = vak.page(page)

        _context.update({'vakantion':page_number})
    return render(request,'scraping/resume.html',_context)


















# class L_List(ListView):
#     queryset = Vakation.objects.all()
#     template_name = 'scraping/home.html'
#     context_object_name = 'vakantion'
#     form=findForm()
#
#
#
#     def get_context_data(self, **kwargs):
#
#         context = super(L_List, self).get_context_data(**kwargs)
#         context['city']=self.request.Get.get('city')
#         context['language']=self.request.Get.get('language')
#         context['form']=self.form
#         return context
#     def get_queryset(self):
#         _filter={}
#         qs = []
#         city=self.request.Get.get('city')
#         language=self.request.Get.get('language')
#         if city or language:
#             if city:
#                 _filter['city__slug'] = city
#             if language:
#                 _filter['language__slug'] = language
#             qs = Vakation.objects.filter(**_filter)
#         return qs
