from rest_framework import serializers
from .models import Company, Document, Shareholders
# from rest_framework.response import Response
# from rest_framework import status

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Document
        fields = '__all__'
        read_only_fields = ['id']


class ShareholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shareholders
        fields = "__all__"
        # read_only_fields = ['id']



class CompanySerializer(serializers.ModelSerializer):
    shareholders = ShareholdersSerializer(many=True)
    # document =  serializers.ListField(child = DocumentSerializer())
    class Meta:
        model = Company
        fields = '__all__'
        # read_only_fields = ['id']

    def validate_shareholders(self,shareholders):
        if len(shareholders) <= 0:
            raise serializers.ValidationError("shareholders null data not accepted")
        return shareholders


    # def create(self, validated_data):
    # '''
        # yesma reponse ma problem i don't know why
    # '''
    #     print(validated_data)
    #     shareholders = validated_data.pop('shareholders',[])
    #     id= []
    #     for shareholder in shareholders:
    #         data =  Shareholders.objects.create(**shareholder)
    #         id.append(data.id)
    #     validated_data["shareholders"] = id
    #     company = Company()
    #     company.__dict__.update(validated_data)
    #     company.save()
    #     company.shareholders.set(id)
    #     return Response(company, status=status.HTTP_201_CREATED)