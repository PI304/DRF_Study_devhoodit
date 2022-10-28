from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import User, UserProfile
from django.http import Http404

class User(APIView):
    def get(self, request, user_uuid=None):
        if user_uuid is None:
            raise Http404

        user_instance = get_object_or_404(UserProfile, uuid=user_uuid)
        user_serializer = UserProfileSerializer(user_instance)

        return Response(user_serializer.data)

    def put(self, request, user_uuid=None):
        if user_uuid is None:
            raise Http404

        user_instacne = get_object_or_404(UserProfile, uuid=user_uuid)
        user_serializer = UserProfileSerializer(user_instacne)

        return Response(user_serializer)

    def post(self, request):
        pass

    def delete(self, request, user_uuid=None):
        if user_uuid is None:
            raise Http404
        
        user_private_instance = get_object_or_404(User, uuid=user_uuid)
        user_private_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
