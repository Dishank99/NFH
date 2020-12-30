from django.contrib import admin
from .models import *
from admin_view.admin import CustomActionForm
from django.forms import ModelForm, Form
from django.forms import DateField, CharField, ChoiceField, TextInput, BooleanField


@admin.register(Batches)
class BatchesAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['timings', 'for_category', 'session_link']

    class Meta:
        model = Batches


class PlanPerksAdmin(admin.StackedInline):
    model = PlanPerks


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    inlines = [PlanPerksAdmin]
    list_display = ['name', 'price', 'tag_line']

    class Meta:
        model = Plans


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['user_name', 'plan',
                    'class_type', 'batch', 'date_valid_upto']
    list_filter = ['is_active', 'plan', 'batch', 'class_type']
    # search_fields = ['class_type', 'batch__timings']
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # to disable view and add you can do this
    # def has_view_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return False

    class Meta:
        model = Subscription


@admin.register(PreviousStarterPlanUser)
class PreviousStarterPlanUserAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['name', 'gender', 'email',
                    'mobile_no', 'batch', 'starting_date']

    class Meta:
        model = PreviousStarterPlanUser


class BodyImageFilter(admin.SimpleListFilter):
    title = 'Body Image'  # or use _('country') for translated title
    parameter_name = 'body_img'

    def lookups(self, request, model_admin):
        return [('present', 'Present'),
                ('not present', 'Not Present'), ]

    def queryset(self, request, queryset):
        if self.value() == 'present':
            return queryset.filter(body_img__startswith='media/body_images/')
        elif self.value() == 'not present':
            return queryset.distinct().filter(body_img='')
        # if self.value():
        #     return queryset.filter(country__id__exact=self.value())


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['get_name', 'gender', 'mobile_no',
                    'get_body_img', 'date_last_active', 'is_blocked']
    list_filter = [BodyImageFilter, 'is_blocked']

    def get_body_img(self, obj):
        if obj.body_img:
            return 'Present'
        return 'Not Present'
    get_body_img.short_description = 'Body Image'  # Renames column head

    def get_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name
    get_name.admin_order_field = 'user'  # Allows column order sorting
    get_name.short_description = 'User Name'  # Renames column head

    class Meta:
        model = Profile


@admin.register(PreRegisteredProfiles)
class PreRegisterAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['get_name', 'gender', 'mobile_no',
                    'username', 'class_type', 'batch', 'plan', 'is_approved']
    list_filter = ['is_approved']

    def get_name(self, obj):
        return obj.first_name + ' ' + obj.last_name
    # get_name.admin_order_field = 'user'  # Allows column order sorting
    get_name.short_description = 'User Name'  # Renames column head

    class Meta:
        model = PreRegisteredProfiles
