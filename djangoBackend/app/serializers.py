from rest_framework import serializers
from app.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation 
        fields=(
            'userID',
            'fname',
            'lname',
            'email',
            'phone'
        )
