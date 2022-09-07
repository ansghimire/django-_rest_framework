from dataclasses import field
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Person, PersonDetail



class funcSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()

  

class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=20)
    is_good = serializers.BooleanField(default=True)
    

    def validate(self, attrs):
        print(len(attrs.get('name')))
        return attrs



class PersonSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()

    # changing model name to first_name in serializer
    first_name = serializers.CharField(source='name')

    class Meta:
        model = Person
        fields = ['first_name', 'age', 'message']


    def validate_age(self, obj):
        if int(obj) < 18:
            raise ValidationError("age should be greater than 18")
        return super().validate(obj)

    @staticmethod
    def get_message(obj):
        return f'Hi my age is {obj.age}'

    



class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetail
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        # print(request)
        # print(request.method)

        if request and request.method == "GET":
            fields['person'] = PersonSerializer()       
        return fields


