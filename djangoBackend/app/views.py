from app.models import Reservation
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.serializers import ReservationSerializer

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
