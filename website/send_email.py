from django.template import Context
from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.http import JsonResponse, HttpResponse


def approval_mail(name, email, password):
    template = render_to_string('emailtemplates/approvaltemplate.html', {
        'name': name,
        'email': email,
        'password': password,
    })

    email = EmailMessage(
        "Approval Request for Namita's Fitness Hub Accepted",
        template,
        settings.EMAIL_HOST_USER,
        [email],
    )

    email.fail_silently = False
    email.send()
    return JsonResponse('Email sent', safe=False, status=200)


def request_notify_mail(data):
    template = get_template('emailtemplates/requestnotifytemplate.html')
    # context = Context(data)
    content = template.render(data)
    # template = render_to_string('emailtemplates/requestnotifytemplate.html', {
    #     'data': data,
    #     'id': request_id
    # })

    email = EmailMessage(
        "Request Notification for New User",
        content,
        settings.EMAIL_HOST_USER,
        ['dishanktak1999@gmail.com'],
    )

    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()
    return JsonResponse('Email sent', safe=False, status=200)


def payment_success_notify_main(data):
    template = render_to_string(
        'emailtemplates/paymentsucessnotifytemplate.html', data)

    subject = "Payment Success Notifiation for "+data.get(
        'first_name') + ' ' + data.get('last_name')
    email = EmailMessage(
        subject,
        template,
        settings.EMAIL_HOST_USER,
        ['dishanktak1999@gmail.com'],
    )

    email.fail_silently = False
    email.send()
    return JsonResponse('Email sent', safe=False, status=200)


def forgot_password_mail(data):
    template = get_template('emailtemplates/forgotpasswordtemplate.html')
    # context = Context(data)
    content = template.render(data)
    # template = render_to_string('emailtemplates/requestnotifytemplate.html', {
    #     'data': data,
    #     'id': request_id
    # })

    email = EmailMessage(
        "Reset Password : Namita's Fitness Hub",
        content,
        settings.EMAIL_HOST_USER,
        [data.get('email')],
    )

    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()
    return JsonResponse('Email sent', safe=False, status=200)
