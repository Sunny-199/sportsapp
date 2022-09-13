from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, MyTokenObtainPairSerializer, UserForgetPasswordSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import uuid
from main_app.models import *
from main_app.serializers import *

# CustomUser Sign-up API
class UserViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user_serializer_obj = UserSerializer(data=data)
        if user_serializer_obj.is_valid():
            profile_serializer_obj = ProfileSerializer(data=data)
            if profile_serializer_obj.is_valid():
                user_obj = user_serializer_obj.save()
                prof_data = profile_serializer_obj.data
                prof_data['user'] = user_obj
                # prof_data['sports_center_owner'] = UserManagement.objects.get(id=request.data.get('sports_center_owner'))
                Profile.objects.create(**prof_data)
                return Response({"success": 'Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": profile_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": user_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)



    @action(detail=False, methods=['post'])
    def user_profile(self, request):
        data = request.data
        sports_center_owner = self.request.query_params.get('sports_center_owner')
        user = CustomUser.objects.get(id=sports_center_owner)
        user_serializer_obj = UserSerializer(data=data)
        if user_serializer_obj.is_valid():
            profile_serializer_obj = ProfileSerializer(data=data)
            if profile_serializer_obj.is_valid():
                user_obj = user_serializer_obj.save()
                prof_data = profile_serializer_obj.data
                prof_data['user'] = user_obj
                Profile.objects.create(**prof_data)
                UserManagement.objects.create(sports_center_owner=user, user=user_obj)
                return Response({"success": 'Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": profile_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": user_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def coach_profile(self, request):
        data = request.data
        owner_name = self.request.query_params.get('owner_name')
        owner = CustomUser.objects.get(id=owner_name)
        user_serializer_obj = UserSerializer(data=data)
        if user_serializer_obj.is_valid():
            profile_serializer_obj = ProfileSerializer(data=data)
            if profile_serializer_obj.is_valid():
                coach_obj = user_serializer_obj.save()
                prof_data = profile_serializer_obj.data
                prof_data['user'] = coach_obj
                Profile.objects.create(**prof_data)
                CoachManagement.objects.create(owner_name=owner, coach_name=coach_obj)
                return Response({"success": 'Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": profile_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": user_serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)


# CustomUser Login API
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class AccountForgetViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserForgetPasswordSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def step1(self, request):
        email = request.data.get('email')
        # name = request.data.get('name')
        user_obj = CustomUser.objects.filter(email=email)
        # print(dir(user_obj.last()))
        # print(user_obj)
        # user_obj.last().name
        if user_obj:
            query_string = str(uuid.uuid4())
            otp_obj = VerifyOtp.objects.filter(email=email)
            if otp_obj:
                otp_obj.update(query_string=query_string)
            else:
                otp_obj = VerifyOtp(email=email, query_string=query_string)
                otp_obj.save()
            # send_email.delay([email], 'OTP for forgot password', 'Your OTP is ' + str(user_otp))
            # email_link = "http://localhost:3000/changepassword/?query_string="+ query_string +"&email"+ email +""
            email_link = "http://localhost:3000/changepassword/" + query_string + "&" + email + ""
            send_mail(
                           'Sports App - Reset password',
                           'Hello ' + user_obj.last().name + ',\n' + 'Please click on the link below to reset your password.' +'\n'+
                            email_link,
                            settings.EMAIL_HOST_USER,
                            [email],
                            fail_silently=False,
                        )

            # send_mail(
            #     'Subject - Django Email Testing',
            #     'Hello ' + name + ',\n' + message,
            #     'sender@example.com',  # Admin
            #     [
            #         email,
            #     ]
            # )
            return Response({'status': 'Email sent successfully', 'email': email}, status=status.HTTP_201_CREATED)
        return Response({'status': 'User with this Email not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def step2(self, request):
        try:
            email = request.data.get('email')
            query_string = request.data.get('query_string')
            query_obj = VerifyOtp.objects.filter(email=email).last() or None
            if query_obj:
                # otp_set_time = query_obj.date_modified + timedelta(days=1)
                # current_time = datetime.now()
                # if otp_set_time.replace(tzinfo=None) < current_time.replace(tzinfo=None):
                #     message = {'error': 'Your OTP has been expired'}
                #     status_code = status.HTTP_400_BAD_REQUEST
                if query_obj.query_string == query_string:
                    message = {'message': 'Your Link verified successfully', "email": email}
                    status_code = status.HTTP_200_OK
                    # query_obj.delete()
                else:
                    message = {'message': 'Please enter valid link'}
                    status_code = status.HTTP_400_BAD_REQUEST
                return Response(message, status=status_code)
            else:
                return Response({'message': 'Please enter valid link'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': 404, 'error': str(e)})

    @action(detail=False, methods=['post'])
    def step3(self, request):
        email = request.data.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            if user:
                password = request.data.get('password')
                user.set_password(password)
                user.save()
                VerifyOtp.objects.filter(email=email).delete()

                return Response({'success': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 404, 'error': str(e)})