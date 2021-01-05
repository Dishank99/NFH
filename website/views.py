import razorpay
from django.shortcuts import render, redirect
from admin_view.models import *
from .models import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import *
from .decorators import *

import datetime

from website.send_email import *

from website import razorpay_secrets


def get_programs_at_nfh_details():
    anniversary_pan = events_pan = socials_pan = None
    anniversary_pan = Anniversary.objects.order_by('-date').first()
    events_pan = Events.objects.order_by('-date').first()
    socials_pan = Socials.objects.order_by('-date').first()

    programs_at_nfh = {
        'Anniversary': {
            'details': anniversary_pan if anniversary_pan is not None else None,
            'image': anniversary_pan.anniversaryimages_set.first() if anniversary_pan is not None else None,
        },
        'Events': {
            'details': events_pan if events_pan is not None else None,
            'image': events_pan.eventimages_set.first() if events_pan is not None else None,
        },
        'Socials': {
            'details': socials_pan if socials_pan is not None else None,
            'image': socials_pan.socialimages_set.first() if socials_pan else None,
        },
    }

    return programs_at_nfh


def HomePage(request):

    try:
        if request.user.is_superuser:
            logout(request)

        notice = Notices.objects.first()

        success_stories = Testimonials.objects.all().order_by('-total_loss')[:3]

        plans = Plans.objects.all()
        plan_perks = {p.name: p.planperks_set.all() for p in plans}

        context = {
            'Notice': notice if notice is not None else None,
            'success_stories': success_stories,
            'programs_at_nfh': get_programs_at_nfh_details(),

            'plans': plans,
            'plan_perks': plan_perks
        }

        return render(request, 'website/home.html', context)
    except Exception as e:
        print(e)


def EventsPage(request):
    events = Events.objects.all()
    event_images = {e.name: e.eventimages_set.all() for e in events}
    print(event_images)

    context = {
        'name': 'Events',
        'Query': events,
        'query_images': event_images,
        'programs_at_nfh': get_programs_at_nfh_details(),
    }
    return render(request, 'website/events.html', context)


def AnniversaryPage(request):
    anniversarys = Anniversary.objects.all()
    anniversary_images = {a.name: a.anniversaryimages_set.all()
                          for a in anniversarys}
    print(anniversary_images)

    context = {
        'name': 'Anniversary',
        'Query': anniversarys,
        'query_images': anniversary_images,
        'programs_at_nfh': get_programs_at_nfh_details(),
    }
    return render(request, 'website/events.html', context)


def SocialPage(request):
    socials = Socials.objects.all()
    social_images = {s.name: s.socialimages_set.all() for s in socials}
    print(social_images)

    context = {
        'name': 'Socials',
        'Query': socials,
        'query_images': social_images,
        'programs_at_nfh': get_programs_at_nfh_details(),
    }
    return render(request, 'website/events.html', context)


def TestimonialPage(request, range_start=None):
    testimonials = None
    if range_start is not None:
        range_end = range_start + 5
        testimonials = Testimonials.objects.all().filter(
            total_loss__range=(range_start, range_end)).order_by('-total_loss')
    else:
        testimonials = Testimonials.objects.all().order_by('-total_loss')

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'website/testimonials.html', context)


def AchievementPage(request, range_start=None):
    achievements = None
    if range_start is not None:
        range_end = range_start + 4
        achievements = Achievements.objects.all().filter(
            year__range=(range_start, range_end))
    else:
        achievements = Achievements.objects.all()

    # achievement_images = {a.title: a.images_set.first() for a in achievements}
    # print(achievement_images)

    context = {
        'achievements': achievements.order_by('-year'),
        # 'achievement_images':achievement_images,
    }

    return render(request, 'website/achievements.html', context)


def HighlightPage(request):
    return render(request, 'website/highlights.html')


def ExercisesPage(request):
    exercises = Exercises.objects.all()
    context = {
        'Exercises': exercises,
    }
    if request.path == '/exercises/':
        return render(request, 'website/exerciseprograms.html', context)
    else:
        paginator = Paginator(exercises, 1)
        page = request.GET.get('page')  # ?page=2
        exercises = paginator.get_page(page)
        context = {
            'Exercises': exercises,
        }
        return render(request, 'website/exercisedetails.html', context)


@login_required
def UploadPicturePage(request):
    if request.method == 'POST':
        image = request.FILES.get('image', False)
        if image:
            try:                
                profile = request.user.profile
            except Profile.DoesNotExist:
                messages.info(request, 'Your Account was not created properly. Kindly re-registr with diffrent credentials')
                return redirect('home-page')
            print(profile)
            profile.body_img = image
            profile.save()
            return redirect('attend-page')
        else:
            messages.info(request, 'Upload Picture')
    context = {
        'image': request.user.profile.body_img if request.user.profile.body_img is not None else None,
    }
    return render(request, 'website/uploadpic.html', context)


@login_required
@pay_first
@has_body_pic
def AttendPage(request):
    try:
        if request.user.subscription and request.user.subscription.is_active:
            link = request.user.subscription.batch.session_link
            context = {
                'link': link,
            }
        else:
            messages.info(request, 'Your Subscription has ended')
        return render(request, 'website/attend.html', context)
    except Exception as e:
        messages.info(request, str(e))
        return redirect('home-page')


@login_required
def PlanDetailsPage(request):
    try:
        user_subscription = request.user.subscription
        context = {
            'user_subscription': user_subscription,
        }
    except:
        context = {}
    return render(request, 'website/plandetails.html', context)


def PaymentPage(request):
    if request.method == 'POST':
        try:
            user_profile = Profile.objects.get(
                mobile_no=request.POST.get('mobile_no'))
            if user_profile is not None:
                user = user_profile.user
                print(user)
                login(request, user)
                if request.user.subscription.is_active:
                    messages.info(request, 'You already have an active Plan')
                    logout(request)
                    return redirect('login-page')
                elif request.GET.get('next'):
                    print(request.GET.get('next'))
                    return redirect(request.GET.get('next'))
                else:
                    slug = user.subscription.plan.slug if user.subscription.plan else Plans.get_default_plan().slug
                    return redirect('/makepayment/'+slug+'/')
            else:
                messages.info(
                    request, 'Contect number is incorrect. If not Registered, Pleases Consider Register ')
                # return redirect('register-page')
        except Exception as e:
            print(str(e))
            messages.info(
                request, 'Contect number is incorrect. If not Registered, Pleases Consider Register ')
            # return redirect('register-page')
    return render(request, 'website/payment.html')


client = razorpay.Client(
    auth=(razorpay_secrets.RAZORPAY_AUTH_TEST_KEY, razorpay_secrets.RAZORPAY_AUTH_TEST_TOKEN))


@register_first
@login_through_mobile_no
def MakePaymentPage(request, slug):
    try:
        print('reached here before error')
        plan = request.user.subscription.plan or Plans.objects.get(slug=slug)
        context = {
            'plan': plan,
            'user': request.user,
        }
        # order_currency = 'INR'
        # order_amount = int(plan.price) * 100
        # print(order_amount)
        # order_receipt = request.user.subscription.pk
        # notes = {
        #     'Plan': plan.name,
        # }
        print('started with post if cond')
        order_currency = 'INR'
        order_amount = int(plan.price) * 100
        print(type(order_amount))
        print(order_amount)
        order_receipt = f'receipt_no_{request.user.subscription.pk}'
        notes = {
            'Plan': plan.name,
        }
        print('checkpoint1')

        # Crreating order
        response = client.order.create(dict(
            amount=order_amount,
            currency=order_currency,
            receipt=order_receipt,
            notes=notes,
            payment_capture=1,
        ))
        order_id = response['id']
        order_status = response['status']

        if order_status == 'created':
            # Server data for user convinience
            context['plan'] = plan
            context['price'] = order_amount
            context['name'] = request.user.subscription.user_name
            context['phone'] = request.user.profile.mobile_no
            context['email'] = request.user.username

            # data that'll be send to the razorpay for
            context['order_id'] = order_id

        if request.method == 'POST':
            response = request.POST

            params_dict = {
                'razorpay_payment_id': response['razorpay_payment_id'],
                'razorpay_order_id': response['razorpay_order_id'],
                'razorpay_signature': response['razorpay_signature']
            }

            # VERIFYING SIGNATURE
            try:
                status = client.utility.verify_payment_signature(params_dict)
                print(request.POST)
                subscription = request.user.subscription
                subscription.payment_id = params_dict.get(
                    'razorpay_payment_id')  # that is generated after payment
                subscription.is_active = True
                subscription.plan = plan
                subscription.date_valid_upto = datetime.date.today(
                ) + datetime.timedelta(days=plan.validity)
                print(datetime.date.today())
                print(subscription.date_valid_upto)
                subscription.save()
                payment_success_notify_main({
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.username.strip(),
                    'gender': request.user.profile.gender,
                    'mobile_no': request.user.profile.mobile_no,
                    'class_type': 'Online' if subscription.class_type == 'O' else 'At Hub',
                    'batch': subscription.batch,
                    'plan_price': subscription.plan.price,
                    'plan_name': subscription.plan.name,
                })
                return redirect('plan-details-page')
            except:
                messages.error(request, 'Payment Failure')
                return render(request, 'website/makepayment.html', context)

        return render(request, 'website/makepayment.html', context)
    except Exception as e:
        print(str(e))
        error_message = str(e)
        if request.user.is_superuser: error_message = error_message.replace('User', 'Admin')
        messages.error(request, error_message)
        return redirect('home-page')

    # # return HttpResponse('<h1>Error in  create order function</h1>')
    # return render(request, 'website/makepayment.html', context)


def PaymentStatusPage(request):
    response = request.POST

    params_dict = {
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        print(request.POST)
        subscription = request.user.subscription
        subscription.payment_id = params_dict.get(
            'razorpay_payment_id')  # that is generated after payment
        subscription.is_active = True
        subscription.save()
        return render(request, 'website/payment_status.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'website/payment_status.html', {'status': 'Payment Faliure!!!'})


def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        print(user)
        # if user is not None and user.is_superuser:
        #     login(request, user)
        #     return redirect('/admin/')
        # elif user is not None and not user.profile.is_blocked:
        #     login(request, user)
        #     if request.GET.get('next'):
        #         return redirect(request.GET.get('next'))
        #     else:
        #         return redirect('attend-page')
        # elif user is not None and user.profile.is_blocked:
        #     messages.info(request, 'You are Blocked by the Admin')
        # else:
        #     messages.info(request, 'Email-Id or Password is incorrect')

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('/admin/')
            elif user.profile and not user.profile.is_blocked:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('attend-page')
            elif user.profile and user.profile.is_blocked:
                messages.info(request, 'You are Blocked by the Admin')

        else:
            messages.info(request, 'Email-Id or Password is incorrect')

    return render(request, 'website/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('home-page')


def RegisterPage(request):
    # print(request.path)
    print(request.GET.get('next'))
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            if Profile.objects.get(mobile_no=request.POST.get('mobile_no')) is not None:
                messages.info(
                    request, 'User with this Mobile Number already exists.')
        except:
            if form.is_valid():
                try:
                    user = form.save()
                    first_name = form.cleaned_data.get('first_name')
                    profile = Profile.objects.create(
                        user=user,
                        gender=request.POST.get('gender'),
                        mobile_no=request.POST.get('mobile_no'),
                    )
                    profile.save()
                    subscription = Subscription.objects.create(
                        user=user,
                        class_type=request.POST.get('class-type'),
                        batch=Batches.objects.get(
                            batch_id=request.POST.get('batch_time')),
                        plan=Plans.objects.get(slug=request.GET.get('next')[1:-1].split('/')[1]
                                            )
                    )
                    subscription.save()
                    messages.success(
                        request, f'User {first_name} created successfully')
                    print(request.GET.get('next'))
                    # return HttpResponseRedirect(f"{reverse('payment-page')}?next={request.GET.get('next')}")
                    if request.GET.get('next'):
                        return HttpResponseRedirect(f"{reverse('payment-page')}?next={request.GET.get('next')}")
                    else:
                        return redirect('payment-page')
                    # return redirect('login-page')
                except:
                    messages.error(request, 'There was some problem while registering. Please try again after some time')
                    if user: user.delete()
                    if profile: profile.delete()
                    if subscription: subscription.delete()
                    
            # messages.error(request,form.errors)

    context = {'form': form}
    return render(request, 'website/register.html', context)


def PreRegisterPage(request):

    if request.method == 'POST':
        try: 
            preregister = PreRegisteredProfiles()
            preregister.first_name = request.POST.get('first_name')
            preregister.last_name = request.POST.get('last_name')
            preregister.username = request.POST.get('username')
            preregister.gender = request.POST.get('gender')
            preregister.mobile_no = request.POST.get('mobile_no')
            preregister.class_type = request.POST.get('class-type')
            preregister.batch = Batches.objects.get(
                batch_id=request.POST.get('batch_time'))
            preregister.plan = Plans.objects.get(slug=Plans.get_default_plan().slug)
            preregister.is_approved = False
            preregister.save()
            request_notify_mail({
                'id': preregister.id,
                'first_name': preregister.first_name,
                'last_name': preregister.last_name,
                'email': preregister.username.strip(),
                'gender': preregister.gender,
                'mobile_no': preregister.mobile_no,
                'class_type': 'Online' if preregister.class_type == 'O' else 'At Hub',
                'batch': preregister.batch,
            })
            messages.info(
                request, 'Your Profile has been shared with Admin, wait for Approval.')
            
            # return redirect('home-page')
        except:
            messages.error(request, 'There was some problem while registering. Please try again after some time')
            if preregister: preregister.delete()

    return render(request, 'website/preregister.html')


def aprrove_request(request, request_id):
    try:
        preregister = PreRegisteredProfiles.objects.get(id=request_id)
        preregister.is_approved = True
        response = preregister.save()
        return HttpResponse('<center><h1>'+response+'</h1></center>')
    except PreRegisteredProfiles.DoesNotExist:
        return HttpResponse('Request for this User is Not Present', status=404)


def get_batches(request):
    batches = Batches.objects.all()
    batches_json = []
    for b in batches:
        batches_json.append({
            'Id': b.batch_id,
            'timings': b.timings,
            'category': b.for_category,
            'link': b.session_link,
        })

    return JsonResponse(batches_json, safe=False)


def get_mobile_nos(request):
    existing_user_profiles = Profile.objects.all().filter(
        mobile_no__startswith=request.POST.get('prefix'))
    if existing_user_profiles:
        return JsonResponse({'Present': True}, safe=False)
    else:
        return JsonResponse({'Present': False}, safe=False)


def ForgotPassword(request):
    try:
        if request.method == 'POST':
            user = User.objects.get(
                username=(request.POST.get('email')).strip())
            print(user)
            forgot_password_mail({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.username,
                'unique_number': user.id + 999,
            })
            messages.info(request, 'Check your email for Password reset link')
    except Exception as e:
        print(e)
        messages.info(request, str(e))
    return render(request, 'website/forgotpassword.html')


def PasswordReset(request, unique_number):
    # messages = []
    try:
        if request.method == 'POST':
            user_id = unique_number - 999
            user = User.objects.get(id=user_id)
            if request.POST.get('password1') == request.POST.get('password2'):
                user.set_password(request.POST.get('password1'))
                user.save()
                return redirect('login-page')
            else:
                messages.info(request, 'Password Doesnot Match')
    except User.DoesNotExist:
        messages.info(request, 'User not Found. Check Your Email-Id')
    return render(request, 'website/passwordreset.html')


def validity_check(request):
    cumulated_resp = []
    users = User.objects.all()
    for user in users:
        print(f'checking user: {user}')
        if not user.is_superuser and user.subscription.is_active and datetime.date.today() >= user.subscription.date_valid_upto:
            if user.subscription.plan.slug == 'starter':
                prevuser = PreviousStarterPlanUser.objects.create(
                    name=user.first_name + user.last_name,
                    gender=user.profile.gender,
                    email=user.username,
                    mobile_no=user.profile.mobile_no,
                    batch=user.subscription.batch.timings,
                    starting_date=user.subscription.date_time_of_subscription,
                )
                prevuser.save()
                user.delete()
            else:
                user.profile.date_last_active = user.subscription.date_valid_upto + \
                    datetime.timedelta(days=365)
                user.profile.save()
                user.subscription.payment_id = None
                user.subscription.is_active = False
                user.subscription.date_valid_upto = None
                user.subscription.plan = None
                user.subscription.save()
            cumulated_resp.append(user.username)
    return JsonResponse({'unsubscribed users': cumulated_resp}, safe=False, status=200)


def account_validity_check(request):
    cumulated_resp = []
    profiles = Profile.objects.all()
    for profile in profiles:
        user = profile.user
        if not user.is_superuser and user.profile and user.profile.date_last_active and datetime.date.today() >= user.profile.date_last_active:
            print(f'checking user: {user}')
            user.delete()
            cumulated_resp.append(user.username)
    return JsonResponse({'unsubscribed users': cumulated_resp}, safe=False, status=200)
