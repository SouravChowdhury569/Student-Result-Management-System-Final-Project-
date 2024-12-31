from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectCombination
from .forms import SubjectForm, SubjectCombinationForm
from django.urls import reverse_lazy
# Create your views here.



class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Course Creation'
        context['panel_name'] = 'Courses'
        context['panel_title'] = 'Add Course'
        return context

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    field_list = [
        'Course Name', 'Course Code', 'Creation Date', 'Last Updated'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Courses'
        context['panel_name']   =   'Courses'
        context['panel_title']  =   'View Courses Info'
        context['field_list']   =   self.field_list
        return context

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name_suffix = '_form'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:subject_list')

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name_suffix = '_delete'
    success_url = reverse_lazy('subjects:subject_list')

    
    def get_context_data(self, **kwargs):
        context = super(SubjectDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Course Delete Confirmation'
        context['panel_name'] = 'Courses'
        context['panel_title'] = 'Delete Course'
        return context
    
class SubjectCombinationCreateView(LoginRequiredMixin, CreateView):
    model = SubjectCombination
    form_class = SubjectCombinationForm
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'CourseCombination Creation'
        context['panel_name'] = 'CourseConbinations'
        context['panel_title'] = 'Create CourseConbination'
        return context

class SubjectCombinationListView(LoginRequiredMixin, ListView):
    model = SubjectCombination
    field_list = [
        'Semester', 'Section', 'Course'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage CourseCombinations'
        context['panel_name']   =   'CourseCombinations'
        context['panel_title']  =   'View CourseCombinations Info'
        context['field_list']   =   self.field_list
        return context

class SubjectCombinationUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectCombination
    template_name_suffix = '_form'
    form_class = SubjectCombinationForm
    success_url = reverse_lazy('subjects:subject_combination_list')

class SubjectCombinationDeleteView(LoginRequiredMixin, DeleteView):
    model = SubjectCombination
    template_name_suffix = "_delete"
    success_url = reverse_lazy('subjects:subject_combination_list')

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'CourseCombination Delete Confirmation'
        context['panel_name'] = 'CourseCombinations'
        context['panel_title'] = 'Delete CourseCombination'
        return context
