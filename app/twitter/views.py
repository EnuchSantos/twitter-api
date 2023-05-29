from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer, TweetSerializer
from .models import User, Tweet
from .services import UserService, TweetService


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        new_user = UserService.create_user(request)
        serializer = self.get_serializer(new_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'], url_path='follow_user')
    def follow_user(self, request):
        user = UserService.follow_user(
            request.data['user_id'], request.data['follow_id'])
        if user:
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "follow process fail"}, status=status.HTTP_400_BAD_REQUEST)


class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    @action(detail=False, methods=["POST"], url_path='recent_tweets')
    def recent_tweets(self, request):
        last_tweets = TweetService.recent_tweets(request)
        if last_tweets:
            serializer = self.get_serializer(last_tweets, many=True)
            return Response(serializer.data)
        return Response({'error': 'no tweets'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'], url_path='users_tweets')
    def users_tweets(self, request):
        users_tweets = TweetService.user_tweets(request)
        if users_tweets:
            serializer = self.get_serializer(users_tweets, many=True)
            return Response(serializer.data)
        elif users_tweets == None:
            return Response({'erros': 'users donts have tweets'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'erros': 'users no extis'}, status=status.HTTP_400_BAD_REQUEST)
