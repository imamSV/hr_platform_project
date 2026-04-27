from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import IsRoleBasedAccess  


class ResumeViewSet(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    permission_classes = [IsRoleBasedAccess]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Resume.objects.none()

        if user.role in ['admin', 'hr']:
            return Resume.objects.all()

        return Resume.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
