# = REST Framework =#
from django.contrib.auth.models import User, Group
import rest_framework as REST
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, PostSerializer, ChangePasswordSerializer
from blog.models import *
from rest_framework.decorators import action
from .security import permissions

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [REST.permissions.IsAdminUser]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [REST.permissions.IsAuthenticated]

class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for retrieving all posts
    """
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer
    permission_classes = [REST.permissions.IsAuthenticated]

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAdminOrSelf,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
