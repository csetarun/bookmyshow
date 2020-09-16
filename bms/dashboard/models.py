from django.db import models
from django.conf import settings
import datetime
# from allauth.account.signals import user_logged_in, user_signed_up


class Theatre(models.Model):
    city_choice=(
        ('BANGALORE','Bangalore'),
        ('CHENNAI','Chennai'),
        ('DELHI','Delhi'),
        ('HYDERABAD','Hyderabad'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
    )
    name = models.CharField(max_length=50,null=False,default="Waves Cinema")
    city = models.CharField(max_length=9,choices=city_choice,null=False)
    address = models.CharField(max_length=30)

    def __str__(self):
        return '{}-{}-{}'.format(self.name, self.address, self.city)

class Movie(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
        ('KANNADA', 'Kannada')
    )
    rating_choice = (
        ('U', 'U'),
        ('UA', 'U/A'),
        ('A', 'A'),
        ('R', 'R'),
    )
    name = models.CharField(max_length=50,null=True,blank=True)
    cast = models.CharField(max_length=100,null=True,blank=True)
    director = models.CharField(max_length=50,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes",null=True,blank=True)
    certificate = models.CharField(max_length=2, choices=rating_choice)
    popularity_index = models.IntegerField(unique=True, null=True, blank=True)
    trailer = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return '{}-{}-{}'.format(self.movie, self.theatre,self.show_time)


class Booking(models.Model):
    payment_choice = (
        ('Credit Card', 'Credit Card'),
    )
    id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    payment_type = models.CharField(max_length=11, choices=payment_choice,default='Credit Card')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return str(self.id)


class Seat(models.Model):
    seat_choice = (
        ('', 'Select'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )
    no = models.CharField(max_length=3,null=True,blank=False)
    row = models.IntegerField()
    column = models.IntegerField()
    seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('no', 'show')

    def __str__(self):
        return '{}-{}'.format(self.no,self.show)

class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return '{}_{}'.format(self.booking,self.seat)