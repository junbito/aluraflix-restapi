from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restapi.models import Category, Video
from django.contrib.auth.models import User


class VideoListTests(APITestCase):
    request_url = reverse('video-list')
    
    def setUp(self):
        self.user = User.objects.create()
        self.client.force_authenticate(user=self.user)
        self.category1 = Category.objects.create(title='FREE', color='TEST color')
        self.category2 = Category.objects.create(title='TEST title', color='TEST color')
        self.video = Video.objects.create(title='TEST title', description='TEST description', url='TEST url', owner=self.user)

    def test_create_video(self):
        """
        Ensure we can create a video object.
        """
        # With the default category
        data = {'title': 'POST TEST title', 'description': 'POST TEST description', 'url':  'POST TEST url'}
        response = self.client.post(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 2)
        new_video = Video.objects.get(id=2)
        self.assertEqual(new_video.title, data['title'])
        self.assertEqual(new_video.description, data['description'])
        self.assertEqual(new_video.url, data['url'])
        self.assertEqual(new_video.category, self.category1)
        # With a specific category
        data['category_id'] = 2
        response = self.client.post(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 3)
        new_video = Video.objects.get(id=3)
        self.assertEqual(new_video.category, self.category2)
    
    def test_list_videos(self):
        """
        Ensure we can list video objects.
        """
        Video.objects.create(title='TEST title', description='TEST description', url='TEST url', owner=self.user)
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class VideoDetailTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create()
        self.client.force_authenticate(user=self.user)
        self.category1 = Category.objects.create(title='FREE', color='TEST color')
        self.category2 = Category.objects.create(title='TEST title', color='TEST color')
        self.video = Video.objects.create(title='TEST title', description='TEST description', url='TEST url', owner=self.user)
        self.request_url = reverse('video-detail', kwargs={'pk': self.video.pk})
    
    def test_retrieve_video(self):
        """
        Ensure we can retrieve a video object.
        """
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), self.video.pk)
    
    def test_update_video(self):
        """
        Ensure we can update a video object.
        """
        # PUT method
        data = {'title': 'PUT TEST title', 'description': 'PUT TEST description', 'url': 'PUT TEST url', 'category_id': 1}
        response = self.client.put(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Video.objects.count(), 1)
        updated_video = Video.objects.get()
        self.assertEqual(updated_video.title, data['title'])
        self.assertEqual(updated_video.description, data['description'])
        self.assertEqual(updated_video.url, data['url'])
        self.assertEqual(updated_video.category, self.category1)
        # PATCH method
        data['title'] = 'PATCH TEST title'
        response = self.client.patch(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data['description'] = 'PATCH TEST description'
        response = self.client.patch(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data['url'] = 'PATCH TEST url'
        response = self.client.patch(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data['category_id'] = 2
        response = self.client.patch(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Video.objects.count(), 1)
        updated_video = Video.objects.get()
        self.assertEqual(updated_video.title, data['title'])
        self.assertEqual(updated_video.description, data['description'])
        self.assertEqual(updated_video.url, data['url'])
        self.assertEqual(updated_video.category, self.category2)
    
    def test_delete_video(self):
        """
        Ensure we can delete a video object.
        """
        response = self.client.delete(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Video.objects.count(), 0)


class CategoryListTests(APITestCase):
    request_url = reverse('category-list')
    
    def setUp(self):
        self.category = Category.objects.create(title='FREE', color='TEST color')

    def test_create_category(self):
        """
        Ensure we can create a category object.
        """
        data = {'title': 'POST TEST title', 'color': 'POST TEST color'}
        response = self.client.post(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        new_category = Category.objects.get(id=2)
        self.assertEqual(new_category.title, data['title'])
        self.assertEqual(new_category.color, data['color'])

    def test_list_categories(self):
        """
        Ensure we can list video objects.
        """
        Category.objects.create(title='TEST title', color='TEST color')
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class CategoryDetailTests(APITestCase):
    
    def setUp(self):
        self.category = Category.objects.create(title='FREE', color='TEST color')
        self.request_url = reverse('category-detail', kwargs={'pk': self.category.pk})
    
    def test_retrieve_category(self):
        """
        Ensure we can retrieve a category object.
        """
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), self.category.pk)
    
    def test_update_category(self):
        """
        Ensure we can update a category object.
        """
        # PUT method
        data = {'title': 'PUT TEST title', 'color': 'PUT TEST color'}
        response = self.client.put(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        updated_category = Category.objects.get()
        self.assertEqual(updated_category.title, data['title'])
        self.assertEqual(updated_category.color, data['color'])
        # PATCH method
        data['title'] = 'PATCH TEST title'
        response = self.client.patch(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data['color'] = 'PATCH TEST color'
        response = self.client.patch(self.request_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        updated_category = Category.objects.get()
        self.assertEqual(updated_category.title, data['title'])
        self.assertEqual(updated_category.color, data['color'])

    def test_delete_category(self):
        """
        Ensure we can delete a category object.
        """
        response = self.client.delete(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 0)


class CategoryVideoDetailTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.category = Category.objects.create(title='FREE', color='TEST color')
        self.video1 = Video.objects.create(title='TEST title', description='TEST description', url='TEST url', owner=self.user)
        self.video2 = Video.objects.create(title='TEST title', description='TEST description', url='TEST url', owner=self.user)
        self.request_url = reverse('category-video-detail', kwargs={'pk': self.category.pk})
    
    def test_retrieve_category(self):
        """
        Ensure we can retrieve a category object.
        """
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('videos')), 2)


class UserListTests(APITestCase):
    request_url = reverse('user-list')
    
    def setUp(self):
        self.user = User.objects.create()
    
    def test_list_users(self):
        """
        Ensure we can list user objects.
        """
        User.objects.create(username='lauren', password='secret')
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class UserDetailTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create()
        self.request_url = reverse('user-detail', kwargs={'pk': self.user.pk})
    
    def test_retrieve_user(self):
        """
        Ensure we can retrieve a user object.
        """
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), self.user.pk)
