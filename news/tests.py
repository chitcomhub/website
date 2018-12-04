from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Post



class NewsApiTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='tornado')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.post_data = {
            'title':'Docker', 'content':'Docker is very powerful', 'author':user.id
        }
        self.response = self.client.post(
            reverse('news'),
            self.post_data,
            format='json'
        )

    def test_api_can_get_posts(self):
        response = self.client.get(
            reverse('news')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK )


    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_post(self):
        post = Post.objects.get()
        response = self.client.get(
            reverse('news-detail',
            kwargs={'pk': post.id}), format="json")

    def test_api_can_update_a_post(self):
        post = Post.objects.get()
        change_post = {'title':'RestApi', 'content':'RestApiIsGood'}
        response = self.client.put(
            reverse('news-detail', kwargs={'pk':post.id}),
            change_post, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_api_can_delete_a_post(self):
        post = Post.objects.get()
        response = self.client.delete(
            reverse('news-detail', kwargs={'pk':post.id}),
            format='json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



