from rest_framework import serializers
from .models import Address,Profile


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)






class AddressSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Address
        fields = ['uuid','city','area']
        read_only_fields = ['uuid']


class ProfileSerializer(serializers.ModelSerializer):
    # address = serializers.SlugRelatedField(slug_field='uuid', queryset=Address.objects.all())
    address = serializers.ListField(child=serializers.SlugRelatedField(slug_field='id', queryset=Address.objects.all()))

    class Meta:
        model = Profile
        fields = ['id', 'address', 'name']
        read_only_fields = ['id']


    def create(self, validated_data):
        addresses = validated_data['address']
        name = validated_data['name']

        for address in addresses:
            self.Meta.model.objects.create(address=address, name=name)

        return validated_data
    

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == "GET":
            fields["address"] = AddressSerializer(fields=('uuid', 'city'))
        return fields
        