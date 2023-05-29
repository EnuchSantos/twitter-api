from .models import User, Tweet


class UserService():

    def create_user(request):
        new_user = User(
            username=request.data['username'],
            bio=request.data['bio'],
            email=request.data['email'],
            location=request.data['location'],
            website=request.data['website'],
            phone=request.data['phone'],
            birth_date=request.data['birth_date'],
        )
        new_user.set_password(request.data['password'])
        new_user.save()
        return new_user

    def follow_user(user_id, follow_id):
        user = User.objects.filter(pk=user_id).first()
        follow = User.objects.filter(pk=follow_id).first()
        if user and follow:
            if not user.follows.contains(follow) and not follow.followers.contains(user):
                user.follows.add(follow)
                follow.followers.add(user)
            else:
                user.follows.remove(follow)
                follow.followers.remove(user)
            user.save()
            follow.save()
            return user
        return None


class TweetService():

    def recent_tweets(request):
        last_tweets = Tweet.objects.all().exclude(
            user_tweet=request.data['user_id'])[:10]
        if last_tweets:
            return last_tweets
        return None

    def user_tweets(request):
        user = User.objects.filter(pk=request.data['user_id']).first()
        users_results = User.objects.filter(
            pk__in=request.data['users']).exclude(id=user.id)
        if users_results != None:
            users_tweets = []
            for user in users_results:
                tweet_result = Tweet.objects.filter(user_tweet=user.id)
                if tweet_result != None:
                    for tweet in tweet_result:
                        users_tweets.append(tweet)
            return users_tweets
        return None
