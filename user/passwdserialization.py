from user.models import users_new
from rest_framework import serializers

class PasswdserializerClass(serializers.ModelSerializer):
   # acc_created = serializers.CharField(required=False)
    otp = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields = ('password','emailid','acc_created','userId','mobilenumber','otp')