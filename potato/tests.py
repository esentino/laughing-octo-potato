from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse

from potato.views import MainView, RegisterView


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

class RegisterPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_open_main_test_page(self):
        request = self.factory.get(reverse('register'))
        response = RegisterView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_form_valid_data(self):
        form = UserCreationForm({
            'username': 'John',
            'password1': 'testsuperpassword',
            'password2': 'testsuperpassword',
        })
        self.assertTrue(form.is_valid())
        user = form.save(commit=True)
        self.assertEqual(user.username, 'John')

    def test_form_invalid_data(self):
        form = UserCreationForm({
            'username': 'John',
            'password1': 'testsuperpassword',
            'password2': 'testsuperpasswor',
        })
        self.assertFalse(form.is_valid())

        form = UserCreationForm({
            'password1': 'testsuperpassword',
            'password2': 'testsuperpassword',
        })
        self.assertFalse(form.is_valid())
