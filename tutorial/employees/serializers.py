from rest_framework import serializers
from employees.models import Employee

class EmployeeSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    firstname = serializers.CharField(max_length=100, allow_blank=False, required=False)
    lastname = serializers.CharField(max_length=100, allow_blank=False, required=False)
    phoneno = serializers.CharField(max_length=17, allow_blank=True, required=False)
    email = serializers.EmailField(max_length=120, allow_blank=True, required=False)
    role = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new 'Employee' instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Employee' instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.phoneno = validated_data.get('phoneno', instance.phoneno)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
