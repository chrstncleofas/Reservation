from django.urls import reverse
from app.models import Reservation
from django.shortcuts import render
from .forms import ReservationForm
from django.http import HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app.serializers import ReservationSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reservationApi(request, id=0):
    # Fetch all Data API
    if request.method=='GET':
        reservations = Reservation.objects.all()
        reservation_serializer=ReservationSerializer(reservations, many=True)
        return JsonResponse(reservation_serializer.data, safe=False)
    # Create or Add API
    elif request.method=='POST':
        reservation_data=JSONParser().parse(request)
        reservation_serializer=ReservationSerializer(data=reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add",safe=False)
    # Update API
    elif request.method=='PUT':
        reservation_data=JSONParser().parse(request)
        reservation=Reservation.objects.get(userID=reservation_data['userID'])
        reservations_serializer=ReservationSerializer(reservation, data=reservation_data)
        if reservations_serializer.is_valid():
            reservations_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    # Delete API
    elif request.method=='DELETE':
        reservation=Reservation.objects.get(userID=id)
        reservation.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
def home(request):
    return render(request, 'app/base.html')
    
def list(request):
    return render(request, 'app/list.html', {
        'reservation' : Reservation.objects.all(),
    })

def list_item(request, id):
    reservations = Reservation.objects.get(pk=id)
    return HttpResponseRedirect(reverse('list'))

def edit_list(request, id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=id)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return render(request, 'app/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        reservation = Reservation.objects.get(pk=id)
        form = ReservationForm(instance=reservation)
    return render(request, 'app/edit.html',{
        'form': form,
    })


def delete_list(request, id):
    if request.method == 'POST':
        reservation = Reservation.objects.get(pk=id)
        reservation.delete()
    return HttpResponseRedirect(reverse('list'))
