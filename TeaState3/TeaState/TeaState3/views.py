from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Allowances, Deductions, Owner, Estate, Worker, OwnerEstate, Attendance, DailyTeaPlucked, Officer, Item, Supplier, ItemSupplier 
import random

class CustomLoginView(LoginView):
    template_name = 'TeaState3/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('mainmenu')

class RegisterPage(FormView):
    template_name ='TeaState3/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('mainmenu')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('managers')
        return super(RegisterPage, self).get(*args, **kwargs)

#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------

class OwnerList(LoginRequiredMixin, ListView):
    model = Owner
    context_object_name = 'owners'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = context['owners'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['owners'] = context['owners'].filter(first_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class OwnerDetail(LoginRequiredMixin, DetailView):
    model = Owner
    context_object_name = 'owner'
    fields = {'first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date'}
    template_name = 'TeaState3/owner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OwnerCreate(LoginRequiredMixin, CreateView):
    model = Owner
    fields = {'first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date'}
    success_url = reverse_lazy('owners')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OwnerCreate, self).form_valid(form)

class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = Owner
    fields = {'first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date'}
    success_url = reverse_lazy('owners')

class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    context_object_name = 'owner'
    success_url = reverse_lazy('owners')

#------------------------------------------------------------------------------------------

class WorkerList(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = 'workers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workers'] = context['workers'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['workers'] = context['workers'].filter(first_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class WorkerDetail(LoginRequiredMixin, DetailView):
    model = Worker
    context_object_name = 'worker'
    fields = {'epf_number', 'first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date', 'join_date', 'hourly_rate', 'estate'}
    template_name = 'TeaState3/worker.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WorkerCreate(LoginRequiredMixin, CreateView):
    model = Worker
    fields = {'epf_number', 'first_name', 'gender', 'last_name',  'address', 'phone_number', 'birth_date', 'join_date', 'hourly_rate', 'estate'}
    success_url = reverse_lazy('workers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkerCreate, self).form_valid(form)

class WorkerUpdate(LoginRequiredMixin, UpdateView):
    model = Worker
    fields = {'epf_number','first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date', 'join_date', 'hourly_rate', 'estate'}
    success_url = reverse_lazy('workers')


class WorkerDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Worker
    context_object_name = 'worker'
    success_url = reverse_lazy('workers')

#------------------------------------------------------------------------------------------

class EstateList(LoginRequiredMixin, ListView):
    model = Estate
    context_object_name = 'estates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estates'] = context['estates'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['estates'] = context['estates'].filter(estate_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class EstateDetail(LoginRequiredMixin, DetailView):
    model = Estate
    context_object_name = 'estate'
    fields = {'estate_name', 'address'}
    template_name = 'TeaState3/estate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EstateCreate(LoginRequiredMixin, CreateView):
    model = Estate
    fields = {'estate_name', 'address'}
    success_url = reverse_lazy('estates')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EstateCreate, self).form_valid(form)

class EstateUpdate(LoginRequiredMixin, UpdateView):
    model = Estate
    fields = {'estate_name', 'address'}
    success_url = reverse_lazy('estates')

class EstateDelete(LoginRequiredMixin, DeleteView):
    model = Estate
    context_object_name = 'estate'
    success_url = reverse_lazy('estates')

#------------------------------------------------------------------------------------------

class AttendanceList(LoginRequiredMixin, ListView):
    model = Attendance
    context_object_name = 'attendances'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attendances'] = context['attendances'].filter(recorded_by_id=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['attendances'] = context['attendances'].all().filter(epf_number__first_name__contains  = search_input)
        
        context['search_input'] = search_input

        return context

class AttendanceDetail(LoginRequiredMixin, DetailView):
    model = Attendance
    context_object_name = 'attendance'
    fields = {'id', 'epf_number', 'present_date', 'present_type'}
    template_name = 'TeaState3/attendance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AttendanceCreate(LoginRequiredMixin, CreateView):
    model = Attendance
    fields = {'id', 'epf_number', 'present_date', 'present_type'}
    success_url = reverse_lazy('attendances')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AttendanceCreate, self).form_valid(form)

class AttendanceUpdate(LoginRequiredMixin, UpdateView):
    model = Attendance
    fields = {'id', 'epf_number', 'present_date', 'present_type'}
    success_url = reverse_lazy('attendances')

class AttendanceDelete(LoginRequiredMixin, DeleteView):
    model = Attendance
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendances')
#------------------------------------------------------------------------------------------

class OwnerEstateList(LoginRequiredMixin, ListView):
    model = OwnerEstate
    context_object_name = 'ownerestates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ownerestates'] = context['ownerestates'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['ownerestates'] = context['ownerestates'].filter(owner__first_name__contains = search_input)
        
        context['search_input'] = search_input

        return context

class OwnerEstateDetail(LoginRequiredMixin, DetailView):
    model = OwnerEstate
    context_object_name = 'ownerestate'
    fields = '__all__'
    template_name = 'TeaState3/ownerestate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OwnerEstateCreate(LoginRequiredMixin, CreateView):
    model = OwnerEstate
    fields = '__all__'
    success_url = reverse_lazy('ownerestates')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OwnerEstateCreate, self).form_valid(form)

class OwnerEstateUpdate(LoginRequiredMixin, UpdateView):
    model = OwnerEstate
    fields = '__all__'
    success_url = reverse_lazy('ownerestates')

class OwnerEstateDelete(LoginRequiredMixin, DeleteView):
    model = OwnerEstate
    context_object_name = 'ownerestate'
    success_url = reverse_lazy('ownerestates')

#------------------------------------------------------------------------------------------

class DailyTeaPluckedList(LoginRequiredMixin, ListView):
    model = DailyTeaPlucked
    context_object_name = 'dailyteaplucks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dailyteaplucks'] = context['dailyteaplucks'].filter(recorded_by_id=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['dailyteaplucks'] = context['dailyteaplucks'].filter(epf_number__first_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class DailyTeaPluckedDetail(LoginRequiredMixin, DetailView):
    model = DailyTeaPlucked
    context_object_name = 'dailyteaplucked'
    fields = '__all__'
    template_name = 'TeaState3/dailyteaplucked.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DailyTeaPluckedCreate(LoginRequiredMixin, CreateView):
    model = DailyTeaPlucked
    fields = {'epf_number', 'working_date', 'green_leaf_quantity'}
    success_url = reverse_lazy('dailyteaplucks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DailyTeaPluckedCreate, self).form_valid(form)

class DailyTeaPluckedUpdate(LoginRequiredMixin, UpdateView):
    model = DailyTeaPlucked
    fields = '__all__'
    success_url = reverse_lazy('dailyteaplucks')

class DailyTeaPluckedDelete(LoginRequiredMixin, DeleteView):
    model = DailyTeaPlucked
    context_object_name = 'dailyteaplucked'
    success_url = reverse_lazy('dailyteaplucks')

#------------------------------------------------------------------------------------------

class OfficerList(LoginRequiredMixin, ListView):
    model = Officer
    context_object_name = 'officers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officers'] = context['officers'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['officers'] = context['officers'].filter(name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class OfficerDetail(LoginRequiredMixin, DetailView):
    model = Officer
    context_object_name = 'officer'
    fields = '__all__'
    template_name = 'TeaState3/officer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OfficerCreate(LoginRequiredMixin, CreateView):
    model = Officer
    fields = {'first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date', 'estate'}
    success_url = reverse_lazy('officers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OfficerCreate, self).form_valid(form)

class OfficerUpdate(LoginRequiredMixin, UpdateView):
    model = Officer
    fields = {'first_name', 'last_name', 'gender', 'address', 'phone_number', 'birth_date', 'estate'}
    success_url = reverse_lazy('officers')

class OfficerDelete(LoginRequiredMixin, DeleteView):
    model = Officer
    context_object_name = 'officer'
    success_url = reverse_lazy('officers')

#------------------------------------------------------------------------------------------

class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['items'] = context['items'].filter(item_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = 'item'
    fields = {'item_name', 'estate_id', 'unit', 'price', 'item_category', 'quantity_in_hand', 'supplier'}
    template_name = 'base/item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = {'item_name', 'estate_id', 'unit', 'price', 'item_category', 'quantity_in_hand', 'supplier'}
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = {'item_name', 'estate_id', 'unit', 'price', 'item_category', 'quantity_in_hand', 'supplier'}
    success_url = reverse_lazy('items')

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('items')

#------------------------------------------------------------------------------------------

class SupplierList(LoginRequiredMixin, ListView):
    model = Supplier
    context_object_name = 'suppliers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = context['suppliers'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['suppliers'] = context['suppliers'].filter(company_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class SupplierDetail(LoginRequiredMixin, DetailView):
    model = Supplier
    context_object_name = 'supplier'
    fields = '__all__'
    template_name = 'TeaState3/item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SupplierCreate(LoginRequiredMixin, CreateView):
    model = Supplier
    fields = {'company_name', 'address', 'email'}
    success_url = reverse_lazy('suppliers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SupplierCreate, self).form_valid(form)

class SupplierUpdate(LoginRequiredMixin, UpdateView):
    model = Supplier
    fields = {'company_name', 'address', 'email'}
    success_url = reverse_lazy('suppliers')

class SupplierDelete(LoginRequiredMixin, DeleteView):
    model = Supplier
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers')

#------------------------------------------------------------------------------------------

class ItemSupplierList(LoginRequiredMixin, ListView):
    model = ItemSupplier
    context_object_name = 'itemsuppliers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemsuppliers'] = context['itemsuppliers'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['itemsuppliers'] = context['itemsuppliers'].filter(item__item_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class ItemSupplierDetail(LoginRequiredMixin, DetailView):
    model = ItemSupplier
    context_object_name = 'itemsupplier'
    fields = '__all__'
    template_name = 'TeaState3/itemsupplier.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ItemSupplierCreate(LoginRequiredMixin, CreateView):
    model = ItemSupplier
    fields = {'item', 'supplier'}
    success_url = reverse_lazy('itemsuppliers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemSupplierCreate, self).form_valid(form)

class ItemSupplierUpdate(LoginRequiredMixin, UpdateView):
    model = ItemSupplier
    fields = {'item', 'supplier'}
    success_url = reverse_lazy('itemsuppliers')

class ItemSupplierDelete(LoginRequiredMixin, DeleteView):
    model = ItemSupplier
    context_object_name = 'itemsupplier'
    success_url = reverse_lazy('itemsuppliers')

#------------------------------------------------------------------------------------------


class AllowanceList(LoginRequiredMixin, ListView):
    model = Allowances
    context_object_name = 'allowances'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allowances'] = context['allowances'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['allowances'] = context['allowances'].filter(epf_number__first_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class AllowanceDetail(LoginRequiredMixin, DetailView):
    model = Allowances
    context_object_name = 'allowance'
    fields = '__all__'
    template_name = 'TeaState3/allowances.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AllowanceCreate(LoginRequiredMixin, CreateView):
    model = Allowances
    fields = {'epf_number', 'allowance_amount', 'allowance_description', 'start_date', 'active'}
    success_url = reverse_lazy('allowances')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AllowanceCreate, self).form_valid(form)

class AllowanceUpdate(LoginRequiredMixin, UpdateView):
    model = Allowances
    fields = {'epf_number', 'allowance_amount', 'allowance_description', 'start_date', 'active'}
    success_url = reverse_lazy('allowances')

class AllowanceDelete(LoginRequiredMixin, DeleteView):
    model = Allowances
    context_object_name = 'allowance'
    success_url = reverse_lazy('allowances')

#------------------------------------------------------------------------------------------


class DeductionList(LoginRequiredMixin, ListView):
    model = Deductions
    context_object_name = 'deductions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deductions'] = context['deductions'].filter(user=self.request.user) #Here
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['deductions'] = context['deductions'].filter(epf_number__first_name__icontains = search_input)
        
        context['search_input'] = search_input

        return context

class DeductionDetail(LoginRequiredMixin, DetailView):
    model = Deductions
    context_object_name = 'deduction'
    fields = '__all__'
    template_name = 'TeaState3/deductions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DeductionCreate(LoginRequiredMixin, CreateView):
    model = Deductions
    fields = {'epf_number', 'deduction_amount', 'deduction_description', 'start_date', 'active'}
    success_url = reverse_lazy('deductions')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeductionCreate, self).form_valid(form)

class DeductionUpdate(LoginRequiredMixin, UpdateView):
    model = Deductions
    fields = {'epf_number', 'deduction_amount', 'deduction_description', 'start_date', 'active'}
    success_url = reverse_lazy('deductions')

class DeductionDelete(LoginRequiredMixin, DeleteView):
    model = Deductions
    context_object_name = 'deduction'
    success_url = reverse_lazy('deductions')

#------------------------------------------------------------------------------------------

def mainmenu(request):
    worker_count = Worker.objects.count()
    green_leaf_quantity = 1041
    items_count = Item.objects.count()
    return render(request, 'TeaState3\mainmenu.html', {'worker_count': worker_count, 'green_leaf_quantity': green_leaf_quantity , 'items_count': items_count})

def staffmenu(request):
    return render(request, 'TeaState3\staffmenu.html')

def accountsmenu(request):
    return render(request, 'TeaState3\\accountsmenu.html')

def greenleafmenu(request):
    return render(request, 'TeaState3\greenleafmenu.html')

def inventorymenu(request):
    return render(request, 'TeaState3\inventorymenu.html')

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

#class LoginRequiredMixin(object):
#    @method_decorator(login_required)
#    def dispatch(self, request, *args, **kwargs):
#        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

#class mainmenu(LoginRequiredMixin, TemplateView):
#    template_name = "base\mainmenu.html"

#class staffmenu(LoginRequiredMixin, TemplateView):
#    template_name = "base\staffmenu.html"

#class accountsmenu(LoginRequiredMixin, TemplateView):
#    template_name = "base\\accountsmenu.html"

#class greenleafmenu(LoginRequiredMixin, TemplateView):
#    template_name = "base\greenleafmenu.html"

#class inventorymenu(LoginRequiredMixin, TemplateView):
#    template_name = "base\inventorymenu.html"

#------------------------------------------------------------------------------------------