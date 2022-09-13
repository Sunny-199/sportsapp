from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework import validators
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


# User Sign-up API
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    USERNAME_FIELD = 'email'

    def validate(self, attrs):
        password = attrs.get('password')
        user_obj = CustomUser.objects.filter(email=attrs.get('email'))
        if user_obj:
            credentials = {
                'email': user_obj[0].email,
                'password': password
            }
            user = CustomUser.objects.get(email = user_obj[0].email)
            print(user.check_password(password))
            # user = authenticate(request=self.context['request'], email=user_obj[0].email, password=password)
            if user.check_password(password):
                refresh = self.get_token(user)
                data = {
                        'success': True,
                        'status': 200,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'role': user.role,
                        'email': user.email,
                        'message': 'Login successfully'
                    }
                return data
            return {"message": 'please enter valid email and password', 'status': 400}
        else:
            return {"message": 'please enter valid email and password', 'status': 400}


    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token

    # @classmethod
    # def get_token(cls, user):
    #     token = super(MyTokenObtainPairSerializer, cls).get_token(user)
    #
    #     token['name'] = user.name
    #     token['email'] = user.email
    #     token['gender'] = user.gender
    #     token['contact'] = user.contact
    #     token['role'] = user.role
    #     return token


class UserForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
# from rest_framework import validators
# from .models import *
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.core.exceptions import ValidationError
# from django.contrib.auth import authenticate
#
#
# # User Sign-up API
# # User Sign-up API
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         # fields = ['user', 'phone_no', 'location', 'sports_center_name', 'from_time', 'to_time', 'specialisation', 'first_name', 'last_name', 'gender', 'status']
#         # fields = '__all__'
#         exclude = ['user']
#
# class UserSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = CustomUser
#         fields ='__all__'
#         # extra_kwargs = {
#         #     'password': {
#         #         'write_only': True,
#         #         'style': {'input_type': 'password'}
#         #     },
#         #     'role': {'write_only': True,
#         #              }
#         #
#         # }
#
#     # def create(self, validated_data):
#     #     user = CustomUser.objects.create_user(**validated_data)
#     #     return user
#     def create(self, validated_data):
#         # data = request.data
#         password = validated_data.pop('password')
#         user_serializer_obj = UserSerializer(data=validated_data)
#         if user_serializer_obj.is_valid():
#             profile_serializer_obj = ProfileSerializer(data=validated_data)
#             if profile_serializer_obj.is_valid():
#                 password = set_password(password)
#                 user_obj = user_serializer_obj.save()
#                 prof_data = profile_serializer_obj.data
#                 prof_data['user'] = user_obj, password
#                 # prof_data['sports_center_owner'] = UserManagement.objects.get(id=request.data.get('sports_center_owner'))
#                 Profile.objects.create(**prof_data)
#                 # return Response({"success": 'Created Successfully'}, status=status.HTTP_201_CREATED)
#                 return prof_data
#         #     else:
#         #         return Response({"error": profile_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
#         # else:
#         #     return Response({"error": user_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
#         #
#         # user = CustomUser(**validated_data)
#         # user.set_password(password)
#         # user.save()
#         # return user
#

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     # email = serializers.EmailField()
#     USERNAME_FIELD = 'email'
#
#     def validate(self, attrs):
#         password = attrs.get('password')
#         user_obj = CustomUser.objects.filter(email=attrs.get('email'))
#         print(user_obj)
#         if user_obj:
#             credentials = {
#                 'email': user_obj[0].email,
#                 'password': password
#             }
#             user = authenticate(request=self.context['request'], email=user_obj[0].email, password=password)
#             print(user)
#             if user:
#                 print(user,0000000000000)
#                 # try:
#                     # if (user.CustomUser.user_type.name == "user" or user.CustomUser.user_type.name == "owner"):
#                     # if user:
#                 refresh = self.get_token(user)
#                 data = {
#                             'success': True,
#                             'status': 200,
#                             'refresh': str(refresh),
#                             'access': str(refresh.access_token),
#                             # 'role': user.CustomUser.user_type.name
#                             'message':'Login successfully'
#                         }
#                 return data
#                     # return {'message': 'please enter valid email and password', 'status': 400}
#                 # except Exception as e:
#                 #     return {'message': 'please enter valid email and password', 'status': 400}
#             return {"message": 'please enter valid email and password', 'status': 400}
#         else:
#             return {"message": 'please enter valid email and password', 'status': 400}
#
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Add custom claims
#         token['username'] = user.email
#         token['role'] = user.role
#
#         return token
# #
#     # @classmethod
#     # def get_token(cls, user):
#     #     token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#     #
#     #     token['name'] = user.name
#     #     token['email'] = user.email
#     #     token['gender'] = user.gender
#     #     token['contact'] = user.contact
#     #     token['role'] = user.role
#     #     return token
#
#
# class UserForgetPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password']
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'style': {'input_type': 'password'}
#             }
#         }
#
