from dataclasses import field
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressSerializer, ProfileSerializer
from .models import Address, Profile


class AddressView(APIView):
    def get(self, *args, **kwargs):
        qs = Address.objects.all()
        ser = AddressSerializer(instance=qs, many=True)
        # ser = AddressSerializer(instance=qs, many=True, fields=("uuid",))
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def post(self, *args, **kwargs):
        data = self.request.data 
        ser = AddressSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)


class ProfileView(APIView):
    def get(self, *args, **kwargs):
        qs = Profile.objects.all()
        ser = ProfileSerializer(instance=qs, many=True, context={"request":self.request})
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        ser = ProfileSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
