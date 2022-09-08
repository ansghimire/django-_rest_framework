from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from .models import Company, Document, Shareholders
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework import status

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        '''
        Paila validate hanem
        '''
        serializer.is_valid(raise_exception=True)
        shareholders = serializer.validated_data.pop('shareholders',[])
        id= []
        for shareholder in shareholders:
            data =  Shareholders.objects.create(**shareholder)
            id.append(data.id)
        '''
        yo simple cha buj6au affai
        '''
        company = Company()
        company.__dict__.update(serializer.validated_data)
        company.save()
        company.shareholders.set(id)
        return Response(request.data, status=status.HTTP_201_CREATED)




