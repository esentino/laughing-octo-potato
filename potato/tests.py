from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse

from potato.views import MainView


class MainPageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.logged_user = User.objects.create_user(username='bob',
                                                    email='bob@email.bob',
                                                    password='bobtobob')

    def test_main_page_logged_user(self):
        request = self.factory.get(reverse('main'))
        request.user = self.logged_user
        response = MainView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        pass

    def test_main_page_no_user(self):
        request = self.factory.get(reverse('main'))
        request.user = AnonymousUser()
        response = MainView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        pass
