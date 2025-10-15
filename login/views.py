from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from .serializers import RegistrSerializer

logger = logging.getLogger(__name__)

class Registration(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegistrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("New user registered")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Registration failed")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)