from rest_framework import serializers
from . import models


class SignupSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.User
        fields = ('first_name', 'last_name', 'username', 'password', 'age',
                  'address', 'pincode', 'phone', 'created', 'updated')


    def create(self, validated_data):
        user = models.User(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                           age=validated_data['age'], address=validated_data['address'], pincode=validated_data['pincode'], 
                           phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        return user
