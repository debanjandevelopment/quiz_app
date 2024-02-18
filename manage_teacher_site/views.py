from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import CreateQuestionPaper

def dashboard(request):
    return render (request,'dashboard.html')

class CreateQuestionPaperView(CreateView):
    model=CreateQuestionPaper
    fields= ['question_paper_name','total_question','exam_time','subject']
    template_name="form.html"
    
    def form_valid(self, form):
        return super().form_valid(form)