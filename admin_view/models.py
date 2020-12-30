from django.db import models


class Achievements(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/achievements',
                              default='media/default.jpg', null=True, blank=True)
    year = models.CharField(max_length=100)
    type = models.CharField(max_length=1000)
    institution = models.CharField(max_length=300)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return self.title


class Anniversary(models.Model):
    name = models.CharField(max_length=300)
    # image = models.ImageField(upload_to='media/anniversary', default='media/default.jpg', null=True, blank=True)
    desc = models.TextField(null=True, blank=True, verbose_name='Description')
    date = models.DateField()
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Anniversary'
        verbose_name_plural = 'Anniversaries'

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=300)
    # image = models.ImageField(upload_to='media/events', default='media/default.jpg', null=True, blank=True)
    desc = models.TextField(null=True, blank=True, verbose_name='Description')
    date = models.DateField()
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name


class Notices(models.Model):
    notice = models.CharField(max_length=500)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.notice


class Testimonials(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(
        max_length=300, verbose_name="Client's Name")
    b_img = models.ImageField(upload_to='media/testimonials', default='media/default.jpg',
                              null=True, blank=True, verbose_name="Before Image")
    a_img = models.ImageField(upload_to='media/testimonials', default='media/default.jpg',
                              null=True, blank=True, verbose_name='After Image')
    b_weight = models.FloatField(verbose_name='Before Weight')
    a_weight = models.FloatField(verbose_name='After Weight')
    duration = models.CharField(
        max_length=200, verbose_name='Duration (in months)')
    total_loss = models.FloatField(verbose_name='Total Loss (in Kgs)')
    review = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name="Client's Review")
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.client_name


class Socials(models.Model):
    name = models.CharField(max_length=300)
    # social_img = models.ImageField(upload_to='media/socials', default='media/default.jpg', null=True, blank=True)
    desc = models.TextField(verbose_name='Description')
    date = models.DateField()
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Social Cause'
        verbose_name_plural = 'Social Causes'

    def __str__(self):
        return self.name


class Carnivals(models.Model):
    carnival_name = models.CharField(max_length=300)
    # carnival_img = models.ImageField(upload_to='media/carnivals', default='media/default.jpg', null=True, blank=True)
    carnival_desc = models.CharField(max_length=3000)
    carnival_date = models.DateField()
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.carnival_name


class AnniversaryImages(models.Model):
    anniversary = models.ForeignKey(
        Anniversary, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='media/misc', default='media/default.jpg', null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class EventImages(models.Model):
    events = models.ForeignKey(
        Events, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='media/misc', default='media/default.jpg', null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class SocialImages(models.Model):
    socials = models.ForeignKey(
        Socials, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='media/misc', default='media/default.jpg', null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class Exercises(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    desc = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='media/exercises',
                              default='media/default.jpg', null=True, blank=True, verbose_name='Image')
    video_link = models.CharField(
        max_length=2000, null=True, blank=True, verbose_name='Video Link')

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
