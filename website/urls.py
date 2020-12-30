from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', HomePage, name='home-page'),
    path('events/', EventsPage, name='events-page'),
    path('anniversaries/', AnniversaryPage, name='anniversarys-page'),
    path('social-causes/', SocialPage, name='socials-page'),
    path('testimonials/', TestimonialPage, name='testimonials-page'),
    path('testimonials/<int:range_start>/',
         TestimonialPage, name='testimonials-page'),
    path('achievements/', AchievementPage, name='achievements-page'),
    path('achievements/<int:range_start>/',
         AchievementPage, name='achievements-page'),
    path('highlights/', HighlightPage, name='highlight-page'),
    path('exercises/', ExercisesPage, name='exercises-page'),
    path('exercises-in-detail/', ExercisesPage, name='exercises-detail-page'),

    path('uploadpicture/', UploadPicturePage, name='upload-pic-page'),
    path('attend/', AttendPage, name='attend-page'),
    path('plandetails/', PlanDetailsPage, name='plan-details-page'),
    path('payment/', PaymentPage, name='payment-page'),
    path('makepayment/<slug:slug>/', MakePaymentPage, name='makepayment-page'),
    path('payment_status/', PaymentStatusPage, name='payment-status-page'),

    # path('login/',LoginView.as_view(template_name='website/login.html'),name='login-page'),
    path('login/', LoginPage, name='login-page'),
    path('logout/', LogoutPage, name='logout-page'),
    path('register/', RegisterPage, name='register-page'),
    path('preregister/', PreRegisterPage, name='preregister-page'),
    path('password-reset/<int:unique_number>',
         PasswordReset, name='password-reset'),
    path('forgotpassword/', ForgotPassword, name='forgot-password'),

    path('get-batches/', get_batches, name='get-batches'),
    path('get-mobile-nos/', get_mobile_nos, name='get-mobile-nos'),

    path('validitycheck/', validity_check, name='validity-check'),
    path('accountvaliditycheck/', account_validity_check,
         name='account-validity-check'),

    path('approve-request/<int:request_id>/',
         aprrove_request, name='approve-request'),
]
