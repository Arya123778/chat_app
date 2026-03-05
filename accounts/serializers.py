from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User=get_user_model()

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password doesn't match"})
        # If username is not provided, generate one from email
        if not attrs.get('username'):
            attrs['username'] = attrs['email'].split('@')[0]
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','bio','avatar','is_online']
        read_only_fields=['id','email']
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(write_only=True)
    new_password=serializers.CharField(write_only=True, validators=[validate_password])
    
    def validate_old_password(self, value):
        user=self.context['request'].user
        user.set_password(self.validate_data['new_password'])
        user.save()
        