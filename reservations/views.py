from django.shortcuts import render, redirect
from .models import Seat, Reservation
from .forms import ReservationForm

def seat_list(request):
    seats = Seat.objects.all()
    return render(request, 'reservations/seat_list.html', {'seats': seats})

def reserve_seat(request, seat_id):
    seat = Seat.objects.get(id=seat_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.seat = seat
            reservation.save()
            seat.is_reserved = True
            seat.save()
            return redirect('seat_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reserve_seat.html', {'form': form, 'seat': seat})
