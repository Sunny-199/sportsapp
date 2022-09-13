from django.contrib import admin

from main_app.models import SportsCenter, Coaches, Schedule, Transcations, TranscationsDetail, Categories, SubscriptionPlans, SportsCenterOwner,\
    CoachManagement, UserManagement, AssignedPendingSportsCenter, UploadPost, Subscription, Setting, UserSportCenter, ScheduleCoaches, DietPlan, Weekdays


admin.site.register(SportsCenter)
admin.site.register(Coaches)
admin.site.register(Schedule)
admin.site.register(Transcations)
admin.site.register(TranscationsDetail)
admin.site.register(Categories)
admin.site.register(SubscriptionPlans)
admin.site.register(SportsCenterOwner)
admin.site.register(CoachManagement)
admin.site.register(UserManagement)
admin.site.register(AssignedPendingSportsCenter)
admin.site.register(UploadPost)
admin.site.register(DietPlan)
admin.site.register(Subscription)
admin.site.register(Setting)
admin.site.register(UserSportCenter)
admin.site.register(ScheduleCoaches)
admin.site.register(Weekdays)
