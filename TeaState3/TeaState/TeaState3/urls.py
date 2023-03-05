from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

from . import views

urlpatterns = [
    path('', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('mainmenu/', views.mainmenu, name='mainmenu'),
    path('staffmenu/', views.staffmenu, name='staffmenu'),
    path('accountsmenu/', views.accountsmenu, name='accountsmenu'),
    path('inventorymenu/', views.inventorymenu, name = 'inventorymenu'),

    path('owners', OwnerList.as_view(), name='owners'),
    path('owner/<int:pk>/', OwnerDetail.as_view(), name='owner'),
    path('owner-create/', OwnerCreate.as_view(), name='owner-create'),
    path('owner-update/<int:pk>/', OwnerUpdate.as_view(), name='owner-update'),
    path('owner-delete/<int:pk>/', OwnerDelete.as_view(), name='owner-delete'),

    path('workers', WorkerList.as_view(), name='workers'),
    path('worker/<int:pk>/', WorkerDetail.as_view(), name='worker'),
    path('worker-create/', WorkerCreate.as_view(), name='worker-create'),
    path('worker-update/<int:pk>/', WorkerUpdate.as_view(), name='worker-update'),
    path('worker-delete/<int:pk>/', WorkerDelete.as_view(), name='worker-delete'),

    path('estates', EstateList.as_view(), name='estates'),
    path('estate/<int:pk>/', EstateDetail.as_view(), name='estate'),
    path('estate-create/', EstateCreate.as_view(), name='estate-create'),
    path('estate-update/<int:pk>/', EstateUpdate.as_view(), name='estate-update'),
    path('estate-delete/<int:pk>/', EstateDelete.as_view(), name='estate-delete'),

    path('attendances', AttendanceList.as_view(), name='attendances'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='attendance'),
    path('attendance-create/', AttendanceCreate.as_view(), name='attendance-create'),
    path('attendance-update/<int:pk>/', AttendanceUpdate.as_view(), name='attendance-update'),
    path('attendance-delete/<int:pk>/', AttendanceDelete.as_view(), name='attendance-delete'),

    path('ownerestates', OwnerEstateList.as_view(), name='ownerestates'),
    path('ownerestate/<int:pk>/', OwnerEstateDetail.as_view(), name='ownerestate'),
    path('ownerestate-create/', OwnerEstateCreate.as_view(), name='ownerestate-create'),
    path('ownerestate-update/<int:pk>/', OwnerEstateUpdate.as_view(), name='ownerestate-update'),
    path('ownerestate-delete/<int:pk>/', OwnerEstateDelete.as_view(), name='ownerestate-delete'), 

    path('dailyteaplucks', DailyTeaPluckedList.as_view(), name='dailyteaplucks'),
    path('dailyteaplucked/<int:pk>/', DailyTeaPluckedDetail.as_view(), name='dailyteaplucked'),
    path('dailyteaplucked-create/', DailyTeaPluckedCreate.as_view(), name='dailyteaplucked-create'),
    path('dailyteaplucked-update/<int:pk>/', DailyTeaPluckedUpdate.as_view(), name='dailyteaplucked-update'),
    path('dailyteaplucked-delete/<int:pk>/', DailyTeaPluckedDelete.as_view(), name='dailyteaplucked-delete'), 

    path('officers', OfficerList.as_view(), name='officers'),
    path('officer/<int:pk>/', OfficerDetail.as_view(), name='officer'),
    path('officer-create/', OfficerCreate.as_view(), name='officer-create'),
    path('officer-update/<int:pk>/', OfficerUpdate.as_view(), name='officer-update'),
    path('officer-delete/<int:pk>/', OfficerDelete.as_view(), name='officer-delete'),

    path('items', ItemList.as_view(), name='items'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item'),
    path('item-create/', ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>/', ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>/', ItemDelete.as_view(), name='item-delete'),

    path('suppliers', SupplierList.as_view(), name='suppliers'),
    path('supplier/<int:pk>/', SupplierDetail.as_view(), name='supplier'),
    path('supplier-create/', SupplierCreate.as_view(), name='supplier-create'),
    path('supplier-update/<int:pk>/', SupplierUpdate.as_view(), name='supplier-update'),
    path('supplier-delete/<int:pk>/', SupplierDelete.as_view(), name='supplier-delete'),

    path('itemsuppliers', ItemSupplierList.as_view(), name='itemsuppliers'),
    path('itemsupplier/<int:pk>/', ItemSupplierDetail.as_view(), name='itemsupplier'),
    path('itemsupplier-create/', ItemSupplierCreate.as_view(), name='itemsupplier-create'),
    path('itemsupplier-update/<int:pk>/', ItemSupplierUpdate.as_view(), name='itemsupplier-update'),
    path('itemsupplier-delete/<int:pk>/', ItemSupplierDelete.as_view(), name='itemsupplier-delete'),

    path('allowances', AllowanceList.as_view(), name='allowances'),
    path('allowance/<int:pk>/', AllowanceDetail.as_view(), name='allowance'),
    path('allowance-create/', AllowanceCreate.as_view(), name='allowance-create'),
    path('allowance-update/<int:pk>/', AllowanceUpdate.as_view(), name='allowance-update'),
    path('allowance-delete/<int:pk>/', AllowanceDelete.as_view(), name='allowance-delete'),

    path('deductions', DeductionList.as_view(), name='deductions'),
    path('deduction/<int:pk>/', DeductionDetail.as_view(), name='deduction'),
    path('deduction-create/', DeductionCreate.as_view(), name='deduction-create'),
    path('deduction-update/<int:pk>/', DeductionUpdate.as_view(), name='deduction-update'),
    path('deduction-delete/<int:pk>/', DeductionDelete.as_view(), name='deduction-delete'),
]
