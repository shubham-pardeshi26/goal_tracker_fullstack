# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Goal_Users
from .serializers import UserRegistrationSerializer
from django.core.mail import send_mail


class UserRegistrationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Send an email confirmation
            subject = "Registration Confirmation"
            message = "Thank you for registering on MyWebsite. Your registration is successful."
            from_email = "your_email@gmail.com"  # Replace with your email
            recipient_list = [user.email]

            # send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)
