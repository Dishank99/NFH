from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .manager import UserManager
from django.contrib import messages
from django.db import IntegrityError

from website.send_email import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body_img = models.ImageField(
        upload_to='media/body_images', null=True, blank=True)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        choices=GENDER, max_length=10, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    date_last_active = models.DateField(null=True, blank=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Batches(models.Model):
    batch_id = models.AutoField(primary_key=True)
    timings = models.CharField(max_length=100, verbose_name='Timings')
    CATEGORY = (
        ('U', 'Unisex'),
        ('F', 'Female'),
    )
    for_category = models.CharField(
        choices=CATEGORY, max_length=50, verbose_name='Category')
    session_link = models.CharField(
        max_length=800, null=True, blank=True, verbose_name='Session Link')

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

    def __str__(self):
        return self.timings


class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    slug = models.SlugField(null=True, blank=True)
    tag_line = models.CharField(max_length=200, verbose_name='Tag Line')
    name = models.CharField(max_length=100, verbose_name='Name')
    price = models.CharField(max_length=50, verbose_name='Price')
    validity = models.IntegerField(null=True, blank=True)
    PLAN_TYPE = (('D','Default'),('N','Normal'))
    plan_type = models.CharField(choices=PLAN_TYPE, default='N', max_length=10)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(' ', '-')
        print(self.slug)
        super(Plans, self).save(*args, **kwargs)

    @staticmethod
    def get_default_plan():
        default_plan = Plans.objects.get(plan_type='D')
        return default_plan

    def __str__(self):
        return self.name


class PlanPerks(models.Model):
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, null=True,
                            blank=True, verbose_name='Text')

    class Meta:
        verbose_name = 'Plan Perk'
        verbose_name_plural = 'Plan Perks'

    def __str__(self):
        return f'{self.plan}'


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    CLASS_TYPE = (
        ('O', 'Online'),
        ('A', 'At Hub'),
    )
    class_type = models.CharField(
        choices=CLASS_TYPE, max_length=20, null=True, blank=True)
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    plan = models.ForeignKey(
        Plans, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=500, null=True, blank=True)
    date_time_of_subscription = models.DateField(
        auto_now_add=True, null=True, blank=True)
    date_valid_upto = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name}\'s subcription'

    def save(self, *args, **kwargs):
        self.user_name = self.user.first_name + ' ' + self.user.last_name
        super(Subscription, self).save(*args, **kwargs)


class PreviousStarterPlanUser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        choices=GENDER, max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=100, null=True, blank=True)
    batch = models.CharField(max_length=200, null=True, blank=True)
    starting_date = models.DateField(null=True, blank=True)


class PreRegisteredProfiles(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='First Name')
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    username = models.CharField(max_length=200, verbose_name='Email')
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        choices=GENDER, max_length=10, null=True, blank=True, verbose_name='Gender')
    mobile_no = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Mobile No.')
    CLASS_TYPE = (
        ('O', 'Online'),
        ('A', 'At Hub'),
    )
    class_type = models.CharField(
        choices=CLASS_TYPE, max_length=20, null=True, blank=True, verbose_name='Class Type')
    batch = models.ForeignKey(
        Batches, on_delete=models.CASCADE, verbose_name='Batch')
    plan = models.ForeignKey(
        Plans, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Plan')
    is_approved = models.BooleanField(default=False, verbose_name='Approve')

    class Meta:
        verbose_name = 'User Request'
        verbose_name_plural = 'User Requests'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # super(PreRegisteredProfiles, self).save(*args, **kwargs)

        try:
            if self.is_approved:
                user = User()
                user.first_name = self.first_name
                user.last_name = self.last_name
                user.username = self.username.strip()
                user.set_password('abcd123!@#')
                user.save()

                profile = Profile()
                profile.user = user
                profile.gender = self.gender
                profile.mobile_no = self.mobile_no
                profile.save()

                subscription = Subscription()
                subscription.user = user
                subscription.class_type = self.class_type
                subscription.batch = self.batch
                subscription.plan = self.plan
                subscription.save()

                username_for_mail = self.first_name+' ' + self.last_name
                approval_mail(username_for_mail,
                              self.username.strip(), 'abcd123!@#')
                return 'Approved'
                print({'message': 'Approved', 'status': 201})
        except IntegrityError:
            print({'message': 'User already approved and present', 'status': 403})
            self.is_approved = False
            return 'User already approved and present'
        finally:
            super(PreRegisteredProfiles, self).save(*args, **kwargs)


'''
def save(self, *args, **kwargs):
        super(PreRegisteredProfiles, self).save(*args, **kwargs)
        if self.is_approved:
            user = User()
            user.first_name = self.first_name
            user.last_name = self.last_name
            user.username = self.username.strip()
            user.set_password('abcd123!@#')
            user.save()

            profile = Profile()
            profile.user = user
            profile.gender = self.gender
            profile.mobile_no = self.mobile_no
            profile.save()

            subscription = Subscription()
            subscription.user = user
            subscription.class_type = self.class_type
            subscription.batch = self.batch
            subscription.plan = self.plan
            subscription.save()

            username_for_mail = self.first_name+' ' + self.last_name
            approval_mail(username_for_mail,
                          self.username.strip(), 'abcd123!@#')

'''
