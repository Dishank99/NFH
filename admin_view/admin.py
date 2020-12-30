from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User
from django.forms import TextInput, Textarea, CharField, HiddenInput, BooleanField, Form
from django.utils.html import format_html

admin.site.site_header = admin.site.site_title = ("Namita's Fitness Hub")
admin.site.index_title=('Admin')

# admin.site.register(Achievements)
# admin.site.register(Anniversary)
# admin.site.register(Events)
# admin.site.register(Notices)
# admin.site.register(Testimonials)
# admin.site.register(Socials)
# admin.site.register(Carnivals)
# admin.site.register(Images)

admin.site.unregister(Group)
# admin.site.unregister(User)

#####################################################################

class CustomActionForm(Form):
    action = CharField(widget=HiddenInput,
                             initial='delete_selected',
                             label='Delete Selected'
                             )
    select_across = BooleanField(
                                       label='',
                                       required=False,
                                       initial=0,
                                       widget=HiddenInput({'class': 'select-across'}),
                                       )

#####################################################################

@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['title', 'year', 'type', 'institution']

    class Meta:
        model = Achievements

#####################################################################

@admin.register(Notices)
class NoticesAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['notice']

    class Meta:
        model = Notices

#####################################################################

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['client_name', 'b_weight', 'a_weight', 'duration', 'total_loss', 'review']

    class Meta:
        model = Testimonials

#####################################################################

class EventImagesAdmin(admin.StackedInline):
    model = EventImages

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    inlines = [EventImagesAdmin]
    list_display = ['name', 'desc', 'date']

    class Meta:
        model = Events

# @admin.register(EventImages)
# class EventImagesAdmin(admin.ModelAdmin):
#     pass

#####################################################################

class SocialImagesAdmin(admin.StackedInline):
    model = SocialImages

@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    inlines = [SocialImagesAdmin]
    list_display = ['name', 'desc', 'date']

    class Meta:
        model = Socials

# @admin.register(SocialImages)
# class SocialImagesAdmin(admin.ModelAdmin):
#     pass

#######################################################################

class AnniversaryImagesAdmin(admin.StackedInline):
    model = AnniversaryImages

@admin.register(Anniversary)
class AnniversaryAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    inlines = [AnniversaryImagesAdmin]
    list_display = ['name', 'desc', 'date']

    class Meta:
        model = Anniversary

# @admin.register(AnniversaryImages)
# class AnniversaryImagesAdmin(admin.ModelAdmin):
#     pass

#####################################################################

@admin.register(Exercises)
class ExercisesAdmin(admin.ModelAdmin):
    action_form = CustomActionForm
    list_display = ['name', 'desc', 'video_link']

    class Meta:
        model = Exercises

#####################################################################