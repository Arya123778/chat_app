from django.urls import path
from .views import RoomListCreateView, RoomDetailView, JoinRoomView, LeaveRoomView,MessageListView
urlpatterns = [
    path('rooms/', RoomListCreateView.as_view()),
    path('rooms/<int:pk>/',RoomDetailView.as_view()),
    path('rooms/<int:pk>/join/',JoinRoomView.as_view()),
    path('rooms/<int:pk>/leave/',LeaveRoomView.as_view()),
    path('rooms/<int:pk>/messages/',MessageListView.as_view()),
]
