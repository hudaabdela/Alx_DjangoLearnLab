from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all().order_by('-timestamp')
        unread_notifications = notifications.filter(read=False)

        return Response({
            'unread_count': unread_notifications.count(),
            'notifications': [
                {
                    'id': notification.id,
                    'actor': notification.actor.username,
                    'verb': notification.verb,
                    'timestamp': notification.timestamp,
                    'read': notification.read,
                }
                for notification in notifications
            ]
        })

class MarkNotificationAsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk, recipient=request.user)
            notification.read = True
            notification.save()
            return Response({'detail': 'Notification marked as read.'}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
