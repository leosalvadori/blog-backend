from rest_framework import views, permissions
from rest_framework.response import Response
from authentication.serializers import UserSerializer


class RegisterUserView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username}, status=201)
        return Response(serializer.errors, status=400)
