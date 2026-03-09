from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    """List all rooms Or create a new room"""
    serializer_class= RoomSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Room.objects.all()
    
    def perform_create(self,serializer):
        room=serializer.save(created_by=self.request.user)
        room.members.add(self.request.user)

class RoomDetailView(generics.RetrieveAPIView):
    """Get details of single room"""
    serializer_class=RoomSerializer
    permission_classes=[IsAuthenticated]
    queryset=Room.objects.all()

class JoinRoomView(APIView):
    """Join class"""
    permission_classes=[IsAuthenticated]
    def post(self,request,pk):
        try:
            room=Room.objects.get(pk=pk)
            room.members.add(request.user)
            return Response({'detail':f'Joined Room:{room.name}'})
        except Room.DoesNotExist:
            return Response({'detail':f'Room not found'}, status=status.HTTP_404_NOT_FOUND)
        
class LeaveRoomView(APIView):
    """Leave room """
    permission_classes=[IsAuthenticated]
    
    def post(self,request,pk):
        try:
            room=Room.objects.get(pk=pk)
            room.members.remove(request.user)
            return Response({'detail':f'Left room: {room.name}'})
        except Room.DoesNotExist:
            return Response({'detail':f'Room not found'}, status=status.HTTP_404_NOT_FOUND)

class MessageListView(generics.ListAPIView):
    """Get all messages for a specific room """
    serializer_class=MessageSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        room_id=self.kwargs['pk']
        return Message.objects.filter(room_id=room_id).select_related('sender','room')
    