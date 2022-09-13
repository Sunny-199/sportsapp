from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main_app.models import SportsCenter, Coaches, Schedule, Transcations, TranscationsDetail, Categories, SubscriptionPlans, SportsCenterOwner,\
    CoachManagement, UserManagement, AssignedPendingSportsCenter, UploadPost, Subscription, Setting, UserSportCenter, ScheduleCoaches, DietPlan
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.conf import settings
from accounts.serializers import *
from main_app.serializers import SportsSerializer, CoachesSerializer, ScheduleSerializer, \
    TranscationsSerializer, TranscationDetailSerializer, CategoriesSerializer, SubscriptionPlansSerializer, SportsCenterOwnerSerializer, CoachManagementSerializer, \
    UserManagementSerializer, AssignedPendingSportsCenterSerializer, UploadPostSerializer, SubscriptionSerializer, SettingSerializer, \
    UserSportCenterSerializer, ScheduleCoachesSerializer, DietPlanSerializer
import itertools

# Sports_Center_Owner_Sports_Center_API

class SportsCenterViewSet(ModelViewSet):
    queryset = SportsCenter.objects.all()
    serializer_class = SportsSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }

        return Response(custom_data, status=status.HTTP_201_CREATED)



# Sports_Center_Owner_Coaches_API
class CoachesViewSet(ModelViewSet):
    queryset = Coaches.objects.all()
    serializer_class = CoachesSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }

        return Response(custom_data, status=status.HTTP_201_CREATED)


# Sports_Center_Owner_Schedule_API
class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# Sports_Center_Owner_Transcations_API
class TranscationsViewSet(ModelViewSet):
    queryset = Transcations.objects.all()
    serializer_class = TranscationsSerializer

# Sports_Center_Owner_Transcation_Detail_API
class TranscationDetailViewSet(ModelViewSet):
    queryset = TranscationsDetail.objects.all()
    serializer_class = TranscationDetailSerializer

# Super_Admin_Categories_API
class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_201_CREATED)



# Sports_Center_Owner_Subscription_API
class SubscriptionPlansViewSet(ModelViewSet):
    queryset = SubscriptionPlans.objects.all()
    serializer_class = SubscriptionPlansSerializer

# Super_Admin_Sports_Center_Owner_API
class SportsCenterOwnerViewSet(ModelViewSet):
    queryset = SportsCenterOwner.objects.all()
    serializer_class = SportsCenterOwnerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }

        return Response(custom_data, status=status.HTTP_201_CREATED)



# Super_Admin_Coach_Management_API
class CoachManagementViewSet(ModelViewSet):
    queryset = CoachManagement.objects.all()
    serializer_class = CoachManagementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_201_CREATED)


# Super_Admin_User_Management_API
class UserManagementViewSet(ModelViewSet):
    queryset = UserManagement.objects.all()
    serializer_class = UserManagementSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     custom_data = {
    #         "status": "success",
    #         "message": "Created Successfully",
    #         "data": serializer.data
    #     }
    #     return Response(custom_data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        queryset = UserManagement.objects.get(sports_center_owner=request.user)
        serializer = UserManagementSerializer(queryset, many=False)

        custom_data = {
            "message": "success",
            "status": 200,
            "data": serializer.data,
        }
        return Response(custom_data, status=status.HTTP_200_OK)

    # def list(self, request, *args, **kwargs):
    #     queryset = list(itertools.chain(UserManagement.objects.all(), CoachManagement.objects.all()))
    #     serializer = UserManagementSerializer(queryset, many=True)
    #     return Response(serializer.data)






    # def list(self, request, *args, **kwargs):
    #     try:
    #         sports_center_owner = request.GET.get('sports_center_owner')
    #         coach_obj = CoachManagement.objects.filter(coach_name=sports_center_owner)
    #
    #         if coach_obj:
    #             user_obj = UserManagement.objects.get(user=coach_obj)
    #             serializer = UserManagementSerializer(user_obj, many=True)
    #             return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)
    #         return Response({'message': 'No data found', 'status': 400}, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         print(e)
    #         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




# Coaches_Image_Video_Upload_API
class UploadPostViewSet(ModelViewSet):
    queryset = UploadPost.objects.all()
    serializer_class = UploadPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Post Uploaded Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_201_CREATED)

# User_Diet_Plan_API
class DietPlanViewSet(ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

# User_Subscription_API
class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

# Super_Admin_Setting_API
class SettingViewSet(ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    def get_accepted_data(self, data):
        data = 0.0
        try:
            user = Setting.objects.get(pk=data)
            coach = Setting.objects.filter(user=user, request=data).last()
            data = coach.data
        except:
            pass
        return data



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)

        custom_data = {
            "status": True,
            "error": False,
            "message": "Created Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_201_CREATED)

# User_Sports_Center_Api
class UserSportCenterViewSet(ModelViewSet):
    queryset = UserSportCenter.objects.all()
    serializer_class = UserSportCenterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_201_CREATED)

    # def list(self, request):
    #     queryset = UserSportCenter.objects.all()
    #     serializer = UserSportCenterSerializer(queryset, many=True)
    #     custom_data = {
    #         "status": "success",
    #         "message": "Listing Successfully",
    #         "data": serializer.data
    #     }
    #     return Response(custom_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = UserSportCenter.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSportCenterSerializer(user)
        custom_data = {
            "status": "success",
            "message": "Detail Get Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.delete()
        return Response(data={"status": "success", "message": "Deleted Successfully"}, status=status.HTTP_400_BAD_REQUEST)



# Coaches_Assigned_Pending_Sports_Center_API
class AssignedPendingSportsCenterViewSet(ModelViewSet):
    queryset = AssignedPendingSportsCenter.objects.all()
    serializer_class = AssignedPendingSportsCenterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        custom_data = {
            "status": "success",
            "message": "Created Successfully",
            "data": serializer.data
        }

        return Response(custom_data, status=status.HTTP_201_CREATED)

    # def list(self, request):
    #     queryset = AssignedPendingSportsCenter.objects.all()
    #     serializer = AssignedPendingSportsCenterSerializer(queryset, many=True)
    #     custom_data = {
    #         "status": "success",
    #         "message": "Data Listing Successfully",
    #         "data": serializer.data
    #     }
    #     return Response(custom_data, status=status.H def list(self, request):
    #     #     queryset = AssignedPendingSportsCenter.objects.all()
    #     #     serializer = AssignedPendingSportsCenterSerializer(queryset, many=True)
    #     #     custom_data = {
    #     #         "status": "success",
    #     #         "message": "Data Listing Successfully",
    #     #         "data": serializer.data
    #     #     }
    #     #     return Response(custom_data, staTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = AssignedPendingSportsCenter.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AssignedPendingSportsCenterSerializer(user)
        custom_data = {
            "status": "success",
            "message": "Detail Get Successfully",
            "data": serializer.data
        }
        return Response(custom_data, status=status.HTTP_200_OK)

    # def update(self, request, pk):
    #     queryset = AssignedPendingSportsCenter.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = AssignedPendingSportsCenterSerializer(user, data=request.data)
    #     custom_data = {
    #         'status': True,
    #         'error': False,
    #         'message': 'Updated Successfully',
    #         'data': serializer.data
    #     }
    #     return Response(custom_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.delete()
        return Response(data={"status": "success", "message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)


# Coaches_Schedule_Api
class ScheduleCoachesViewSet(ModelViewSet):
    queryset = ScheduleCoaches.objects.all()
    serializer_class = ScheduleCoachesSerializer

    # def list(self, request):
    #     queryset = ScheduleCoaches.objects.all()
    #     serializer = ScheduleCoachesSerializer(queryset, many=True)
    #     custom_data = {
    #         "status": "success",
    #         "message": "Schedule Coaches Listing Successfully",
    #         "data": serializer.data
    #     }
    #     return Response(custom_data, status=status.HTTP_200_OK)


