from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu1 = Menu.objects.create(title="Item 1", price=10, inventory=100)
        self.menu2 = Menu.objects.create(title="Item 2", price=20, inventory=100)
        self.menu3 = Menu.objects.create(title="Item 3", price=30, inventory=100)

    def test_getall(self):
        url = reverse('menu')  # assuming you have a 'menu-list' endpoint
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
