from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_app.views import SportsCenterViewSet, CoachesViewSet, ScheduleViewSet, TranscationsViewSet, TranscationDetailViewSet, CategoriesViewSet, SubscriptionPlansViewSet, \
     SportsCenterOwnerViewSet, AssignedPendingSportsCenterViewSet, UploadPostViewSet, SubscriptionViewSet,\
     SettingViewSet, UserSportCenterViewSet, ScheduleCoachesViewSet, DietPlanViewSet, CoachManagementViewSet, UserManagementViewSet

router = DefaultRouter()

# Sports_App_Super_Admin_Api_URL

# Sports_Center_Owner_API_URL
router.register(r'owner', SportsCenterOwnerViewSet, basename='owner'),
# Coach_Management_API_URL
router.register(r'coach', CoachManagementViewSet, basename='coach'),
# User_Management_API_URL
router.register(r'user', UserManagementViewSet, basename='user'),
# Categories_API_URL
router.register(r'categories', CategoriesViewSet, basename='categories'),
# Setting_API_URL
router.register(r'setting', SettingViewSet, basename='setting'),




# Sports_App_Sports_Center_Owner_API_URL

# Sports_Center_API_URL
router.register(r'sports', SportsCenterViewSet, basename='sports'),
# Coaches_API_URL
router.register(r'coaches', CoachesViewSet, basename='coaches'),
# Schedule_API_URL
router.register(r'schedule', ScheduleViewSet, basename='schedule'),
# Transcations_API_URL
router.register(r'transcations', TranscationsViewSet, basename='transcations'),
# Transcations_Detail_API_URL
router.register(r'transcationdetail', TranscationDetailViewSet, basename='transcation-detail'),
# Categories_API_URL
router.register(r'categories', CategoriesViewSet, basename='categories'),
# Subscription_Plans_API_URL
router.register(r'ownerplans', SubscriptionPlansViewSet, basename='owner-plans'),
# Chat_API_URL



# Sports_App_Coaches_API_URL

# Assigned_Pending_Sports_Center_API_URL
router.register(r'assigned', AssignedPendingSportsCenterViewSet, basename='assigned'),
# Image_Video_Upload_API_URL
router.register(r'post', UploadPostViewSet, basename='upload-posts'),
# Coaches_Schedule_API_URL
router.register(r'schedulecoaches', ScheduleCoachesViewSet, basename='schedule')



# Sports_App_User_API_URL

# User_Sports_Center_API_URL
router.register(r'usersportcenter', UserSportCenterViewSet, basename='user-sport-center'),
# Subscription_API_URL
router.register(r'usersubscription', SubscriptionViewSet, basename='subscription-plans'),
# Image_Video_Upload_API_URL
router.register(r'post', UploadPostViewSet, basename='post'),
# Diet_Plan_API_URL
router.register(r'userdietplan', DietPlanViewSet, basename='user-diet-plan'),


urlpatterns = [
     path('', include(router.urls)),

]



