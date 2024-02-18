from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import CreateQuestionPaper
from django.urls import reverse,reverse_lazy

def dashboard(request):
    return render (request,'dashboard.html')

class CreateQuestionPaperView(CreateView):
    model=CreateQuestionPaper
    fields= ['question_paper_name','total_question','exam_time','subject']
    template_name="form.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Exam Paper"
        return context

    def form_valid(self, form):
        print('receive')
        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('teacher_manage_app:teacher_dashboard')