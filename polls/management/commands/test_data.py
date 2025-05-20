from django.core.management.base import BaseCommand
from polls.models import Survey, Question, Choice  # Replace 'your_app' with your actual app name
from django.db import transaction

class Command(BaseCommand):
    help = 'Populates the database with test survey data'

    def handle(self, *args, **options):
        def create_test_data():
            # Survey 1: Restaurant Customer Feedback
            restaurant_survey = Survey.objects.create(
                title="Restaurant Service Feedback",
                owner="RestaurantAdmin",
                purpose="To gather customer feedback about our restaurant service and food quality"
            )
            
            # Questions for Restaurant Survey
            q1 = Question.objects.create(
                survey=restaurant_survey,
                title="How would you rate the quality of food served?"
            )
            Choice.objects.create(
                qn=q1,
                one="Very Poor",
                two="Poor",
                three="Average",
                four="Good",
                five="Excellent"
            )
            
            q2 = Question.objects.create(
                survey=restaurant_survey,
                title="How satisfied were you with the service speed?"
            )
            Choice.objects.create(
                qn=q2,
                one="Very Slow",
                two="Slow",
                three="Moderate",
                four="Fast",
                five="Very Fast"
            )
            
            # Survey 2: Hotel Stay Experience
            hotel_survey = Survey.objects.create(
                title="Hotel Stay Feedback",
                owner="HotelManager",
                purpose="To evaluate guest satisfaction with our hotel amenities and services"
            )
            
            q3 = Question.objects.create(
                survey=hotel_survey,
                title="How would you rate the cleanliness of your room?"
            )
            Choice.objects.create(
                qn=q3,
                one="Unsatisfactory",
                two="Needs Improvement",
                three="Adequate",
                four="Very Clean",
                five="Exceptionally Clean"
            )
            
            q4 = Question.objects.create(
                survey=hotel_survey,
                title="How comfortable was your bed?"
            )
            Choice.objects.create(
                qn=q4,
                one="Very Uncomfortable",
                two="Uncomfortable",
                three="Neutral",
                four="Comfortable",
                five="Very Comfortable"
            )
            
            # Survey 3: Salon Services
            salon_survey = Survey.objects.create(
                title="Beauty Salon Experience",
                owner="SalonOwner",
                purpose="To gather feedback about our salon services and staff performance"
            )
            
            q5 = Question.objects.create(
                survey=salon_survey,
                title="How satisfied are you with your styling result?"
            )
            Choice.objects.create(
                qn=q5,
                one="Very Unsatisfied",
                two="Unsatisfied",
                three="Neutral",
                four="Satisfied",
                five="Very Satisfied"
            )
            
            # Survey 4: Car Repair Service
            mechanic_survey = Survey.objects.create(
                title="Auto Repair Service Feedback",
                owner="ServiceManager",
                purpose="To evaluate customer satisfaction with our auto repair services"
            )
            
            q6 = Question.objects.create(
                survey=mechanic_survey,
                title="How would you rate the transparency of our cost estimates?"
            )
            Choice.objects.create(
                qn=q6,
                one="Very Unclear",
                two="Unclear",
                three="Moderate",
                four="Clear",
                five="Very Clear"
            )
            
            # Survey 5: Dental Clinic
            dental_survey = Survey.objects.create(
                title="Dental Care Experience",
                owner="DentalAdmin",
                purpose="To improve our dental care services based on patient feedback"
            )
            
            q7 = Question.objects.create(
                survey=dental_survey,
                title="How would you rate your overall experience?"
            )
            Choice.objects.create(
                qn=q7,
                one="Terrible",
                two="Poor",
                three="Fair",
                four="Good",
                five="Excellent"
            )

            self.stdout.write(self.style.SUCCESS('Successfully created test data'))

        try:
            with transaction.atomic():
                create_test_data()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating test data: {e}'))