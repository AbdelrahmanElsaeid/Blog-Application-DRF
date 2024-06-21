from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .serializers import SignUpSerializer,ProfileSerializer
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from .models import Profile

# Create your views here.



class SignUp(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        
        email = request.data.get('email')
        username = request.data.get('username')

        user = User.objects.filter(Q(email=email) | Q(username=username)).first()
       
        if user:
            if user.email == email:
                return Response({'status': 'error', "message": _("Email already exists")}, status=status.HTTP_400_BAD_REQUEST)
            if user.username == username:
                return Response({'status': 'error', "message": _("Username already exists")}, status=status.HTTP_400_BAD_REQUEST)
        
       
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            user = serializer.save()

            return Response(
                {"status":"success", "message": _("Account created successfully, ")}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    









class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.user_profile 

    def perform_update(self, serializer):
        if self.request.user.user_profile  == serializer.instance:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.user_profile  == instance:
            instance.delete()
