from rest_framework import serializers
from django.conf import settings
User = settings.AUTH_USER_MODEL
from accounts.models import CustomUser

from main_app.models import SportsCenter, Coaches, Schedule, Transcations, TranscationsDetail, Categories, SubscriptionPlans, SportsCenterOwner,\
    CoachManagement, UserManagement, AssignedPendingSportsCenter, UploadPost, Subscription, Setting, UserSportCenter, ScheduleCoaches, DietPlan

# Sports_Center_Serializer
class SportsSerializer(serializers.ModelSerializer):
    # timings = serializers.SerializerMethodField("get_full_timings")
    contact = serializers.CharField(max_length=15, min_length=10, error_messages={"required": "Please enter your phone number!"})

    class Meta:
        model = SportsCenter
        fields = '__all__'
        # fields = ['id', 'name', 'location', 'email', 'timefrom', 'timeto', 'timings', 'contact']
        # extra_kwargs = {
        #     'email': {
        #         'write_only': True,
        #     },
        #     'timefrom': {
        #         'write_only': True
        #     },
        #     'timeto': {
        #         'write_only': {
        #             'write_only': True
        #         }
        #     }
        # }

    # def get_full_timings(self, obj):
    #     return '{} {}'.format(obj.time_from, obj.time_to)
    #

# Coaches_Serializer
class CoachesSerializer(serializers.ModelSerializer):
    phoneno = serializers.CharField(max_length=15, min_length=10, error_messages={"required": "Please enter your phone number!"})

    class Meta:
        model = Coaches
        fields = '__all__'
        # fields = ['id', 'name',  'location', 'sports_center', 'Contact', 'email', 'specialization']
        # extra_kwargs = {
        #     'email': {
        #         'write_only': True,
        #     },
        #     'specialization': {'write_only': True,
        #                        }
        # }

# Schedule_Serializer
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

# Transcations_Serializer
class TranscationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcations
        fields = '__all__'

# Transcation_Detail_Serializer
class TranscationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscationsDetail
        fields = '__all__'

# Categories_Serializer
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

# Subscription_Plans_Serializer
class SubscriptionPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlans
        fields = '__all__'

# Sports_Center_Owner_Serializer
class SportsCenterOwnerSerializer(serializers.ModelSerializer):
    phoneno = serializers.CharField(max_length=15, min_length=10, error_messages={"required": "Please enter your phone number!"})

    class Meta:
        model = SportsCenterOwner
        fields = '__all__'
        # fields = ['id', 'ownername', 'location', 'sportcenter', 'phoneno', 'email', 'opentimings', 'closetimings']
        # extra_kwargs = {
        #     'email': {
        #         'write_only': True,
        #     },
        #     'opentimings': {
        #         'write_only': True,
        #     },
        #     'closetimings': {
        #         'write_only': True,
        #     }
        #
        # }


# User_Management_Serializer
class UserManagementSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField("get_full_name")
    sports_center_owner = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = UserManagement
        fields = '__all__'
    #     fields = ['id', 'firstname', 'lastname', 'name', 'location', 'email', 'phoneno',  'gender']
    #     extra_kwargs = {
    #         'gender': {
    #             'write_only': True,
    #         },
    #         'firstname': {
    #             'write_only': True
    #         },
    #         'lastname': {
    #             'write_only': True
    #         }
    #     }
    #
    # def get_full_name(self, obj):
    #     return '{} {}'.format(obj.firstname, obj.lastname)




# Coach_Management_Serializer
class CoachManagementSerializer(serializers.ModelSerializer):
    owner_name = serializers.StringRelatedField()
    coach_name = serializers.StringRelatedField()
    class Meta:
        model = CoachManagement
        fields = '__all__'
        # fields = ['id', 'name', 'location', 'sportcenter', 'email', 'contact', 'specialization']
        # extra_kwargs = {
        #     'email': {
        #         'write_only': True,
        #     },
        #     'specialization': {
        #         'write_only': True
        #     }
        # }



# Assigned_Pending_Sports_Center_Serializer
class AssignedPendingSportsCenterSerializer(serializers.ModelSerializer):
    phoneno = serializers.CharField(max_length=15, min_length=10, error_messages={"required": "Please enter your phone number!"})
    class Meta:
        model = AssignedPendingSportsCenter
        fields = '__all__'





    # def to_internal_value(self, data):
    #     phoneno = data.get('phoneno')
    #     """
    #     Validate Password.
    #     """
    #     if not phoneno:
    #         raise serializers.ValidationError({'phoneno': 'Phone number cannot be empty!'})
    #     elif len(phoneno) < 10:
    #         raise serializers.ValidationError({'phoneno': 'Please enter Phone number minimum 10 characters'})
    #
    #     return {
    #         'phoneno': phoneno
    #     }




# Image_Video_Upload_Serializer
class UploadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadPost
        fields = '__all__'


# Diet_Plan_Serializer
class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = '__all__'

# Subscription_Serializer
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

# Setting_Serializer
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'



class UserSportCenterSerializer(serializers.ModelSerializer):
    phoneno = serializers.CharField(max_length=15, min_length=10, error_messages={"required": "Please enter your phone number!"})

    class Meta:
        model = UserSportCenter
        fields = '__all__'




class ScheduleCoachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleCoaches
        fields = '__all__'