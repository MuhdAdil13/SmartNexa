from rest_framework import serializers
from .models import Admin
from  sn_user.models import SmartNexaUser


class AdminRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    role=serializers.CharField(write_only=True)

    class Meta:
        model = SmartNexaUser
        fields = ('username','firstname','lastname','email','password','mobile','role')

    def create(self, validated_data):
        # Extract seller-specific data
        role = validated_data.pop('role')

        # Create the SmartNexaUser instance
        user = SmartNexaUser(
            username=validated_data['username'],
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            mobile=validated_data['mobile'],
            user_type="admin"
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create the Seller instance using the extracted seller-specific data
        Admin.objects.create(
            user=user,
            role=role
        )

        return user
