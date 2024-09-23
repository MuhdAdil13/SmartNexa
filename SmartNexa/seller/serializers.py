from rest_framework import serializers
from .models import Seller
from sn_user.models import SmartNexaUser

class SellerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    company_name = serializers.CharField(write_only=True)  # Custom field for Seller
    company_address = serializers.CharField(write_only=True)  # Custom field for Seller
    tax_id = serializers.CharField(write_only=True)  # Custom field for Seller

    class Meta:
        model = SmartNexaUser
        fields = ('username', 'firstname', 'lastname', 'email', 'password', 'mobile', 'company_name', 'company_address', 'tax_id')

    def create(self, validated_data):
        # Extract seller-specific data
        company_name = validated_data.pop('company_name')
        company_address = validated_data.pop('company_address')
        tax_id = validated_data.pop('tax_id')

        # Create the SmartNexaUser instance
        user = SmartNexaUser(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            mobile=validated_data['mobile'],
            user_type="seller"
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create the Seller instance using the extracted seller-specific data
        Seller.objects.create(
            user=user,
            company_name=company_name,
            company_address=company_address,
            tax_id=tax_id
        )

        return user
