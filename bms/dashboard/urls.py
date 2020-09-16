from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard import views

router = DefaultRouter()
router.register(r'theatre', views.TheatreList)
router.register(r'show', views.ShowList)
router.register(r'movie', views.MoviesList)
router.register(r'seat', views.SeatList)
router.register(r'booking', views.BookingList)
router.register(r'booked_seat', views.BookedSeatList)

urlpatterns = [
    path('', include(router.urls)),
]