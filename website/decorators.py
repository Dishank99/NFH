from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import *
# from django.core.exceptions import DoesNotExist


def has_body_pic(func):
    def wrapper_func(request, *args, **kwargs):
        try:
            if request.user.profile.body_img or request.user.subscription.plan.slug == 'starter':
                return func(request, *args, **kwargs)
            else:
                # return redirect('upload-pic-page')
                return HttpResponseRedirect(f"{reverse('upload-pic-page')}?next={request.path}")
        except Exception as e :
            raise Exception(e)
    return wrapper_func


def login_through_mobile_no(func):
    def wrapper_func(request, slug, *args, **kwargs):
        if slug == 'already-an-nfhite' and not request.user.is_authenticated:
            print('login_through_mobile_no if cond')
            return HttpResponseRedirect(f"{reverse('payment-page')}?next={request.path}")
        else:
            print('login_through_mobile_no else cond')
            print(request)
            print(slug)
            print(func)
            return func(request, slug, *args, **kwargs)
    return wrapper_func


def pay_first(func):
    def wrapper_func(request, *args, **kwargs):
        try:
            if not request.user.subscription or not request.user.subscription.is_active:
                slug = request.user.subscription.plan.slug if request.user.subscription.plan else 'already-an-nfhite'
                return HttpResponseRedirect(f"{reverse('makepayment-page', kwargs={'slug':slug})}?next={request.path}")
            else:
                return func(request, *args, **kwargs)
        except Exception as e:
            messages.info(request, str(e))
            return redirect('home-page')
    return wrapper_func


def register_first(func):
    def wrapper_func(request, slug, *args, **kwargs):
        # if not check_for_slug_validity(slug):
        #     return HttpResponse(status=404)
        try:
            Plans.objects.get(slug=slug)
        except Plans.DoesNotExist:
            raise Http404
        if slug != 'already-an-nfhite' and not request.user.is_authenticated:
            print('register_first if cond')
            return HttpResponseRedirect(f"{reverse('register-page')}?next={request.path}")
        elif slug == 'already-an-nfhite' and not request.user.is_authenticated:
            print('register elif cond')
            return HttpResponseRedirect(reverse('preregister-page'))
        else:
            print('register_first else cond')
            return func(request, slug, *args, **kwargs)
    return wrapper_func
