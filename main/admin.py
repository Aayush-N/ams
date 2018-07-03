from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(DjangoUserAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone',)}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)

	list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
	search_fields = ('email', 'first_name', 'last_name', 'username', 'phone')
	ordering = ('username',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	'''
		Admin View for Student
	'''
	list_display = ('name', 'sem', 'sec', 'phone')
	search_fields = ('name', 'phone')

	class Meta:
		verbose_name = 'Student'


@admin.register(Teaches)
class TeachesAdmin(admin.ModelAdmin):
	list_display = ('teachers_first_name','subject_name','semester','sec')
	search_fields = ('teacher__first_name', 'subject__name', 'subject__code')
	ordering = ('id',)

	def teachers_first_name(self, instance):
		return instance.teacher.first_name

	def subject_name(self, instance):
		return instance.subject.name

	def semester(self, instance):
		return instance.sem.sem

	class Meta:
		verbose_name_plural = 'Teaches'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'theory', 'elective',)
	search_fields = ('name', 'code',)
	ordering = ('name',)