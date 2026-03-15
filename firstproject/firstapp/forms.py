from django import forms

from .models import Reservation


class ReservationForm(forms.modelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
