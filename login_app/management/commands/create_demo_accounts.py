from rest_framework.authtoken.models import Token
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from registration_app.models import CustomProfile


class Command(BaseCommand):
    help = "Creats Demo-Accounts und Dummy-Data for Tests"


    def add_arguments(self, parser):
        parser.add_argument("--username_1", type=str, required=True, help="The Username from the User 1")
        parser.add_argument("--email_1", type=str, required=True, help="The E-Mail-Address from the User 1")
        parser.add_argument("--password_1", type=str, required=True, help="The Password from the User 1")
        parser.add_argument("--username_2", type=str, required=True, help="The Username from the User 2")
        parser.add_argument("--email_2", type=str, required=True, help="The E-Mail-Address from the User 2")
        parser.add_argument("--password_2", type=str, required=True, help="The Password from the User 2")


    def handle(self, *args, **kwargs):
        users = [
            {"username": kwargs["username_1"], "email": kwargs["email_1"], "password": kwargs["password_1"]},
            {"username": kwargs["username_2"], "email": kwargs["email_2"], "password": kwargs["password_2"]},
        ]


        for user in users:
            username = user.get("username")
            email = user.get("email")
            password = user.get("password")
            try:
                test_user = User.objects.get(username=username, email=email)
                last_login_was_more_than_ten_minutes_ago = datetime.datetime.now() - datetime.datetime.now(test_user.last_login) > datetime.timedelta(minutes=10)
                if test_user.last_login and last_login_was_more_than_ten_minutes_ago:
                    test_user.delete()
                    self.stdout.write(self.style.SUCCESS(f"User {test_user} deleted, last activity was more than 10 minutes ago"))
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"No User with the name {username} found. Create new User!"))


            try:
                new_user = User.objects.create_user(username=username, email=email)
                new_user.set_password(password)
                new_user.last_login = timezone.now()
                new_user.save()
                CustomProfile.objects.create(single_user=new_user, user=new_user.id, type="business" if new_user.username == "kevin" else "customer")
                Token.objects.get_or_create(user=new_user)
                self.stdout.write(self.style.SUCCESS(f"New User created: {new_user}"))
            except:    
                new_user.last_login = timezone.now()
                self.stdout.write(self.style.WARNING(f"The User {user["username"]} already exist!"))