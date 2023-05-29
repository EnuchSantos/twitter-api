from django.test import TestCase
import requests


ACCESS_TOKEN_VALUE = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MzgxNTE2LCJpYXQiOjE2ODUzNzk3MTYsImp0aSI6IjIwMGJiMzc5NTA4ZjQ2MDk4OGFhNWM4NGUzZTM3MDRhIiwidXNlcl9pZCI6MX0.0YtGNFLXgBmd6E7oFHaL7wl7l6r-4xWQrWQWd7gH3Rw'
REFRESH_TOKEN_VALUE = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTM4Mzg4OSwiaWF0IjoxNjg1Mzc2Njg5LCJqdGkiOiIwZTQ0YzU4MGViM2I0NzNkOWM2YTIwZmQyNGMzMjc0ZiIsInVzZXJfaWQiOjF9.zKbSCZzlT3aAx5Us8hc2tulEWS4tusfZ4PQkPScKlj0'
SERVER = 'http://localhost:8000/'
HEADERS = {'Authorization': f'Bearer {ACCESS_TOKEN_VALUE}'}


class TestLogin(TestCase):

    def test_login_get_token(self):
        result = requests.post(
            url=f'{SERVER}token/',
            json={
                "username": "admin",
                "password": "admin"
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(list(result.json().keys()), ['refresh', 'access'])

    def test_login_get_new_token(self):
        result = requests.post(
            url=f'{SERVER}token/refresh/',
            json={
                "refresh": REFRESH_TOKEN_VALUE
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(list(result.json().keys()), ['access', 'refresh'])


class TestUser(TestCase):

    def test_list_users(self):
        result = requests.get(
            url=f'{SERVER}users/'
        )

        self.assertEqual(result.status_code, 200)
        self.assertNotEqual(result.json(), [])

    def test_get_user(self):
        user_id = 1
        username = "admin"
        result = requests.get(
            url=f'{SERVER}users/{user_id}/'
        )

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()['username'], username)

    def test_create_user(self):
        username = "era pedro123456"
        result = requests.post(
            url=f'{SERVER}users/',
            json={
                "username": f"{username}",
                "password": "erika",
                "bio": "",
                "email": "erika",
                "location": "",
                "website": "",
                "phone": "",
                "birth_date": '2020-01-01'
            }
        )
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json()['username'], username)

    def test_follow_user(self):
        user_id = 1
        follow_id = 2
        result = requests.post(
            url=f'{SERVER}users/follow_user/',
            json={
                "user_id": user_id,
                "follow_id": follow_id
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()['follows'][0], follow_id)


class TestTweet(TestCase):

    def test_create_tweet(self):
        result = requests.post(
            url=f'{SERVER}tweets/',
            headers=HEADERS,
            json={
                "user_tweet": 1,
                "text": "au au asdasdasd"
            }
        )
        self.assertEqual(result.status_code, 201)
        self.assertNotEqual(result.json(), [])

    def test_get_tweet(self):
        tweet_id = 1
        result = requests.get(
            url=f'{SERVER}tweets/{tweet_id}/',
            headers=HEADERS
        )
        self.assertEqual(result.status_code, 200)
        self.assertNotEqual(result.json(), [])
        self.assertEqual(result.json()['id'], tweet_id)

    def test_list_tweets(self):
        result = requests.get(
            url=f'{SERVER}tweets/',
            headers=HEADERS
        )
        self.assertEqual(result.status_code, 200)
        self.assertNotEqual(result.json(), [])

    def test_follows_tweets(self):
        user_id = 2
        users = [1]
        result = requests.post(
            url=f'{SERVER}tweets/users_tweets/',
            headers=HEADERS,
            json={
                "user_id": user_id,
                "users": users
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertNotEqual(result.json(), [])
