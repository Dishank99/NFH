# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.forms import modelformset_factory
# from .models import *
# from .forms import *

# @login_required
# def home(request):
#     return render(request, 'admin_view/main.html')

# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         messages.info(request, 'Username or Password is Incorrect')

#     return render(request, 'admin_view/login.html')

# def logoutPage(request):
#     logout(request)
#     return redirect('login')

# @login_required
# def achievementsPage(request):
#     achievements = Achievements.objects.all()
#     context = {
#         'achievements': achievements,
#     }

#     return render(request, 'admin_view/achievements.html', context)

# @login_required
# def add_achievement(request):
#     form = AchievementForm()
#     images = request.FILES.getlist('images')
#     if request.method == 'POST':
#         form = AchievementForm(request.POST)        
#         if form.is_valid():
#             achievement = form.save()
#             for i in images:
#                 Images.objects.create(achievements=achievement, image = i)
#             # achievement.save()
#             return redirect('admin-achievements-page')

#     return render(request, 'admin_view/add_achievement.html', {'form':form})

# @login_required
# def update_achievements(request, pk=None):
#     achievement = Achievements.objects.get(pk=pk)
#     form = AchievementForm(instance=achievement)
#     images = achievement.images_set.all()
#     if request.method == 'POST':
#         form = AchievementForm(request.POST,instance=achievement)        
#         # formset = ImageFormSet(request.FILES,instance=achievement)       
#         if form.is_valid(): # and formset.is_valid():
#             form.save()
#             images_more = request.FILES.getlist('image')
#             print(images_more)
#             for i in images_more:
#                 image, created = Images.objects.get_or_create(achievements = achievement, image=i)
#                 if created:
#                     image.save()
#     context = {'achievement':achievement,'form':form,'images':images}# , 'formset':formset 'image_formset':image_formset}
#     return render(request, 'admin_view/update_achievement.html', context)

# def delete_achievement_image(request, pk=None):
#     image = Images.objects.get(pk=pk)
#     image.delete()
#     return redirect('update-achievements-page', pk=image.achievements.id)

# @login_required
# def delete_achievements(request, pk=None):
#     achievement = Achievements.objects.get(pk=pk)
#     achievement.delete()
#     return redirect('admin-achievements-page')

# @login_required
# def anniversaryPage(request):
#     anniversary = Anniversary.objects.all()
#     context = {
#         'anniversary': anniversary,
#     }

#     return render(request, 'admin_view/anniversary.html', context)

# @login_required
# def add_anniversary(request):
#     form = AnniversaryForm()
#     images = request.FILES.getlist('images')
#     if request.method == 'POST':
#         form = AnniversaryForm(request.POST, request.FILES)        
#         if form.is_valid():
#             anniversary = form.save()
#             for i in images:
#                 Images.objects.create(anniversary=anniversary, image = i)
#             return redirect('admin-anniversary-page')

#     return render(request, 'admin_view/add_anniversary.html', {'form':form})

# @login_required
# def update_anniversary(request, pk=None):
#     anniversary = Anniversary.objects.get(pk=pk)
#     form = AnniversaryForm(instance=anniversary)
#     images = anniversary.images_set.all()
#     if request.method == 'POST':
#         form = AnniversaryForm(request.POST, request.FILES,instance=anniversary)        
#         if form.is_valid():
#             form.save()
#             images_more = request.FILES.getlist('image')
#             print(images_more)
#             for i in images_more:
#                 image, created = Images.objects.get_or_create(anniversary = anniversary, image=i)
#                 if created:
#                     image.save()
#             # return redirect('admin-anniversary-page')

#     return render(request, 'admin_view/update_anniversary.html', {'anniversary':anniversary,'form':form, 'images':images})

# @login_required
# def delete_anniversary(request, pk=None):
#     anniversary = Anniversary.objects.get(pk=pk)
#     anniversary.delete()
#     return redirect('admin-anniversary-page')

# def delete_anniversary_image(request, pk=None):
#     image = Images.objects.get(pk=pk)
#     image.delete()
#     return redirect('update-anniversary-page', pk=image.anniversary.id)

# @login_required
# def eventPage(request):
#     event = Events.objects.all()
#     context = {
#         'event': event,
#     }

#     return render(request, 'admin_view/event.html', context)

# @login_required
# def add_event(request):
#     form = EventForm()
#     images = request.FILES.getlist('images')
#     if request.method == 'POST':
#         form = EventForm(request.POST, request.FILES)        
#         if form.is_valid():
#             event = form.save()
#             for i in images:
#                 Images.objects.create(events=event, image = i)
#             return redirect('admin-event-page')

#     return render(request, 'admin_view/add_event.html', {'form':form})

# @login_required
# def update_event(request, pk=None):
#     event = Events.objects.get(pk=pk)
#     form = EventForm(instance=event)
#     images = event.images_set.all()
#     if request.method == 'POST':
#         form = EventForm(request.POST, request.FILES,instance=event)        
#         if form.is_valid():
#             form.save()
#             images_more = request.FILES.getlist('image')
#             print(images_more)
#             for i in images_more:
#                 image, created = Images.objects.get_or_create(events = event, image=i)
#                 if created:
#                     image.save()
#             # return redirect('admin-event-page')

#     return render(request, 'admin_view/update_event.html', {'event':event,'form':form, 'images':images})

# @login_required
# def delete_event(request, pk=None):
#     event = Events.objects.get(pk=pk)
#     event.delete()
#     return redirect('admin-event-page')

# def delete_event_image(request, pk=None):
#     image = Images.objects.get(pk=pk)
#     image.delete()
#     return redirect('update-event-page', pk=image.events.id)

# @login_required
# def noticePage(request):
#     notice = Notices.objects.all()
#     context = {
#         'notice': notice,
#     }

#     return render(request, 'admin_view/notice.html', context)

# @login_required
# def add_notice(request):
#     form = NoticeForm()

#     if request.method == 'POST':
#         form = NoticeForm(request.POST, request.FILES)        
#         if form.is_valid():
#             form.save()
#             return redirect('admin-notice-page')

#     return render(request, 'admin_view/add_notice.html', {'form':form})

# @login_required
# def update_notice(request, pk=None):
#     notice = Notices.objects.get(pk=pk)
#     form = NoticeForm(instance=notice)
    
#     if request.method == 'POST':
#         form = NoticeForm(request.POST, request.FILES,instance=notice)        
#         if form.is_valid():
#             form.save()
#             return redirect('admin-notice-page')

#     return render(request, 'admin_view/update_notice.html', {'event':notice,'form':form})

# @login_required
# def delete_notice(request, pk=None):
#     notice = Notices.objects.get(pk=pk)
#     notice.delete()
#     return redirect('admin-notice-page')

# @login_required
# def socialPage(request):
#     social = Socials.objects.all()
#     context = {
#         'social': social,
#     }

#     return render(request, 'admin_view/social.html', context)

# @login_required
# def add_social(request):
#     form = SocialForm()
#     images = request.FILES.getlist('images')
#     if request.method == 'POST':
#         form = SocialForm(request.POST, request.FILES)        
#         if form.is_valid():
#             social = form.save()
#             for i in images:
#                 Images.objects.create(socials=social, image = i)
#             return redirect('admin-social-page')

#     return render(request, 'admin_view/add_social.html', {'form':form})

# @login_required
# def update_social(request, pk=None):
#     social = Socials.objects.get(pk=pk)
#     form = SocialForm(instance=social)
#     images = social.images_set.all()
#     if request.method == 'POST':
#         form = SocialForm(request.POST, request.FILES,instance=social)        
#         if form.is_valid():
#             form.save()
#             images_more = request.FILES.getlist('image')
#             print(images_more)
#             for i in images_more:
#                 image, created = Images.objects.get_or_create(socials = social, image=i)
#                 if created:
#                     image.save()
#             # return redirect('admin-social-page')

#     return render(request, 'admin_view/update_social.html', {'social':social,'form':form,'images':images})

# @login_required
# def delete_social(request, pk=None):
#     social = Socials.objects.get(pk=pk)
#     social.delete()
#     return redirect('admin-social-page')

# def delete_social_image(request, pk=None):
#     image = Images.objects.get(pk=pk)
#     image.delete()
#     return redirect('update-social-page', pk=image.socials.id)

# @login_required
# def testimonialPage(request):
#     testimonials = Testimonials.objects.all()
#     context = {
#         'testimonials': testimonials,
#     }

#     return render(request, 'admin_view/testimonials.html', context)

# @login_required
# def add_testimonial(request):
#     form = TestimonialForm()

#     if request.method == 'POST':
#         form = TestimonialForm(request.POST, request.FILES)        
#         if form.is_valid():
#             form.save()
#             return redirect('admin-testimonial-page')

#     return render(request, 'admin_view/add_testimonial.html', {'form':form})

# @login_required
# def update_testimonial(request, pk=None):
#     testimonial = Testimonials.objects.get(pk=pk)
#     form = TestimonialForm(instance=testimonial)
    
#     if request.method == 'POST':
#         form = TestimonialForm(request.POST, request.FILES,instance=testimonial)        
#         if form.is_valid():
#             form.save()

#     return render(request, 'admin_view/update_testimonial.html', {'testimonial':testimonial,'form':form})

# @login_required
# def delete_testimonial(request, pk=None):
#     testimonial = Testimonials.objects.get(pk=pk)
#     testimonial.delete()
#     return redirect('admin-testimonial-page')
