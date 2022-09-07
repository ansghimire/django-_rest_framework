from rest_framework import serializers
from .models import Company, Document, Shareholders



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Document
        fields = '__all__'
        read_only_fields = ['id']


class ShareholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shareholders
        fields = "__all__"
        read_only_fields = ['id']



class CompanySerializer(serializers.ModelSerializer):
    shareholders = ShareholdersSerializer()
    # document =  serializers.ListField(child = DocumentSerializer())
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['id']

    
    def create(self, validated_data):
        shareholders = validated_data.pop('shareholders',[])

        id= []
        print("data")
        
        # for shareholder in shareholders:
        #     print(shareholder)
        #    data =  Shareholders.objects.create(**shareholder)
        #    print(data.id)
        #    id.append(data.id)

        # c1:Company = Company.objects.create(**validated_data)

        # # for i in id:
        #     # print("============")
        #     # print(i)
        #     # print("================")
        # c1.shareholders_id = id
        # c1.save()
        # c1.shareholders.set(id)
            

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

