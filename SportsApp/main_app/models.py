
from django.db import models
from accounts.models import *

CATEGOTY_CHOICES = (
    ('tennis', 'Tennis'),
    ('football', 'Football'),
    ('boxing', 'Boxing'),
    ('wrestling', 'Wrestling'),
    ('weightlifting', 'Weightlifting'),
    ('gymnastics', 'Gymnastics'),
    ('squash', 'Squash'),
    ('shooting', 'Shooting'),
    ('badminton', 'Badminton')
)


GENDER_CHOICES = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Other', 'OTHER'),)

SPECIALISATION_CHOICES =(
    ('cardio', 'cardio'),
    ('strength', 'strength')
)

SERVICES_CHOICES =(
    ('strength', 'strength'),
    ('cardio', 'cardio')
)

DAYS_OF_WEEK = (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
)

# Super_Admin_Sports_Center_Owner_Model
class SportsCenterOwner(models.Model):
    ownername = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    sportcenter = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    opentimings = models.CharField(max_length=30)
    closetimings = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=11)
    # logo = models.FileField()
    # document = models.FileField()

    def __str__(self):
        return self.ownername

# Sports_center_Owner_Sports_Center_Model
class SportsCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    timefrom = models.CharField(blank=True, null=True, max_length=10)
    timeto = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=11)

    def __str__(self):
        return self.name

# Sports_Center_Owner_Coaches_Model
class Coaches(models.Model):
    sports_center = models.ForeignKey(SportsCenter, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    speciallsation = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=11)

    def __str__(self):
        return self.name



# Super_Admin_Coach_Management_Model
class CoachManagement(models.Model):
    owner_name = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='owner_name')
    coach_name = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="coach_name")

    def __str__(self):
        return f"{self.owner_name}-----{self.coach_name}"


# Super_Admin_User_Management_Model
class UserManagement(models.Model):
    sports_center_owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='sports_center_owner')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="normal_user")

    def __str__(self):
        return f"{self.sports_center_owner}----{self.user}"



# Sports_Center_Owner_Schedule_Model
class Schedule(models.Model):
    username = models.CharField(max_length=30)
    coach = models.CharField(max_length=40)
    sportcenter = models.CharField(max_length=50)
    timings = models.CharField(max_length=60)
    package = models.CharField(max_length=60)

    def __str__(self):
        return self.username

# Sports_Center_Owner_Transcations_Model
class Transcations(models.Model):
    username = models.CharField(max_length=40)
    role = models.CharField(max_length=50)
    sport_center = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

# Sports_Center_Owner_Transcations_Detail_Model
class TranscationsDetail(models.Model):
    date = models.DateField(auto_now_add=True)
    package = models.CharField(max_length=70)
    package_base_value = models.CharField(max_length=40)
    discount_given = models.CharField(max_length=70)
    payment_mode = models.CharField(max_length=50)
    amount = models.CharField(max_length=60)

    def __str__(self):
        return self.package


# Sports_Center_Owner_Categories_Model
class Categories(models.Model):
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sport_center = models.CharField(max_length=70)
    sport = models.CharField(max_length=60, choices=CATEGOTY_CHOICES)

    def __str__(self):
        return self.category

# Sports_Center_Owner_Subscription_Plans_Model
class SubscriptionPlans(models.Model):
    sport_center = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    amount = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.category




# Coaches_Assigned_Pending_Sports_Center_Model
class AssignedPendingSportsCenter(models.Model):
    center_name = models.CharField(max_length=70)
    location = models.CharField(max_length=50)
    services = models.CharField(max_length=20, choices=SERVICES_CHOICES)
    owner = models.CharField(max_length=90)
    phone_no = models.CharField(max_length=11)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.center_name



# User_Images_Videos_Upload_Model
class UploadPost(models.Model):
    title = models.CharField(max_length=100)
    upload_post = models.FileField()



# User_Subscription_Model
class Subscription(models.Model):
    one_month_plan = models.CharField(max_length=100)
    three_months_plan = models.CharField(max_length=100)
    six_months_plans = models.CharField(max_length=100)
    one_year_plan = models.CharField(max_length=100)

# Super_Admin_Setting_Model
class Setting(models.Model):
    sport_center_owner = models.IntegerField()
    coach = models.IntegerField()
    end_user = models.IntegerField()

# User_Sports_Center_Model
class UserSportCenter(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    owner = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    timings = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Coaches_Schedule_Model

class ScheduleCoaches(models.Model):
    username = models.CharField(max_length=30)
    sport = models.CharField(max_length=100)
    sport_center = models.CharField(max_length=100)
    timings = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Weekdays(models.Model):
    days = models.CharField(max_length=20, choices=DAYS_OF_WEEK)

# User_Diet_Plan_Model
class DietPlan(models.Model):
    weekdays = models.ForeignKey(Weekdays, on_delete=models.CASCADE)
    breakfast = models.TextField()
    lunch = models.TextField()
    eveningsnacks = models.TextField()
    dinner = models.TextField()
    def __str__(self):
        return self.breakfast









