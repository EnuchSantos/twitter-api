from rest_framework import serializers

from .models import User, Tweet


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'email', 'location',
                  'website', 'phone', 'birth_date', 'follows', 'followers']

    def get_tweets(self, obj):
        tweet_validation = Tweet.objects.filter(user_tweet=obj.id)
        return [
            TweetSerializer(tweet).data
            for tweet in tweet_validation
        ] if tweet_validation else []


class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = '__all__'
