import django.forms as forms
from .models import *

INPUT_BOX_SIZE = 50

# class AchievementForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'form-control'}),
#             'year': forms.TextInput(attrs={'class':'form-control'}),
#             'type': forms.TextInput(attrs={'class':'form-control'}),
#             'institution': forms.TextInput(attrs={'class':'form-control'}),
#             }
#         model = Achievements
#         fields = '__all__'

# # class DateInput(forms.DateInput):
# #     input_type = 'date'

# class AnniversaryForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.Textarea(attrs={'class':'form-control'}),
#             'date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
#             }
#         model = Anniversary
#         fields = '__all__'

# class EventForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.Textarea(attrs={'class':'form-control'}),
#             # 'date': forms.DateInput(attrs={'class':'datepicker'}),
#             'date': forms.DateInput(attrs={'type': 'date', 'class':'form-control datepicker'}),
#             }
#         model = Events
#         fields = '__all__'

# class NoticeForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'notice': forms.TextInput(attrs={'class':'form-control'}),
#             }
#         model = Notices
#         fields = '__all__'

# class SocialForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.Textarea(attrs={'class':'form-control'}),
#             # 'date': forms.DateInput(attrs={'class':'datepicker'}),
#             'date': forms.DateInput(attrs={'type': 'date', 'class':'form-control datepicker'}),
#             }
#         model = Socials
#         fields = '__all__'

# class TestimonialForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'client_name': forms.TextInput(attrs={'class':'form-control'}),
#             'b_weight': forms.TextInput(attrs={'class':'form-control'}),
#             'a_weight': forms.TextInput(attrs={'class':'form-control'}),
#             'type': forms.TextInput(attrs={'class':'form-control'}),
#             'duration': forms.TextInput(attrs={'class':'form-control'}),
#             'total_loss': forms.TextInput(attrs={'class':'form-control'}),
#             'review': forms.Textarea(attrs={'class':'form-control'}),
#             }
#         model = Testimonials
#         fields = '__all__'
#         exclude = ['client_id']

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Images
#         fields = ['image']
