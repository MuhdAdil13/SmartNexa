from rest_framework import serializers
from .models import Customer
from sn_user.models import SmartNexaUser

class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    gender= serializers.CharField(write_only=True)  # Custom field for Seller
    address_1 = serializers.CharField(write_only=True)  # Custom field for Seller
    address_2 = serializers.CharField(write_only=True)  # Custom field for Seller

    class Meta:
        model = SmartNexaUser
        fields = ('username', 'firstname', 'lastname', 'email', 'password', 'mobile', 'gender', 'address_1', 'address_2')

    def create(self, validated_data):
        # Extract seller-specific data
        gender = validated_data.pop('gender')
        address_1 = validated_data.pop('address_1')
        address_2 = validated_data.pop('address_2')

        # Create the SmartNexaUser instance
        user = SmartNexaUser(
            username=validated_data['username'],
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            mobile=validated_data['mobile'],
            user_type="customer"
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create the Seller instance using the extracted seller-specific data
        Customer.objects.create(
            user=user,
            gender=gender,
            address_1=address_1,
            address_2=address_2
        )

        return user
