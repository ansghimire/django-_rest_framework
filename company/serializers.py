from rest_framework import serializers
from .models import Company, Document, Shareholders
from django.http import HttpResponse
from rest_framework.response import Response



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Document
        fields = '__all__'
        # read_only_fields = ['id']


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
    #     shareholders = validated_data.pop('shareholders',[])
    #     id = []
    #     for shareholder in shareholders:
    #        data =  Shareholders.objects.create(**shareholder)
    #        id.append(data.id)
    #     '''
    #     yesma share holder append ni bhayo
    #     '''
    #     validated_data['shareholders'] = id
        # # company = Company(cmp_name=validated_data["cmp_name"],cmp_address=validated_data["cmp_address"],cmp_info=validated_data["cmp_info"],shareholders=validated_data["shareholders"])
        # company.save()
        # company.shareholders.set(id)
        # print(company)
        # return company

        '''
        yesma validation problem null data ni save bha6
        '''
        # company = Company()
        # company.save()
        # company.shareholders.set(id)
        # print(company)
        # return company

        # '''
        # validate_data
        # '''
        # company = Company(validated_data)
        # company.save()
        # company.shareholders.set(id)
        # return company


        '''
        yo tarikale mil6
        '''
        # company = Company()
        # company.__dict__.update(validated_data)
        # print(validated_data)
        # company.save()
        # company.shareholders.set(id)
        # return company



        # return super().create(validated_data)
    

      
   
    # def create(self, validated_data):
    #     print(validated_data)
    #     # shareholders = validated_data.pop('shareholders')
    #     # print("======================")
    #     # print(shareholders)
    #     # print("======================")
    #     # print("======================")
       
    #     # documents = validated_data.pop('document')
        

    #     # #saving shareholder
    #     # for shareholder in shareholders
    #     #    data =  Shareholders.objects.create(**shareholder)
    #     #    print('data',data)
            
    #     # Company.objects.create(**validated_data)
    #     return validated_data
