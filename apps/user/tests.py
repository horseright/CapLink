from django.test import TestCase

# Create your tests here.


class TestUser(TestCase):
    def test_user_login(self):
        self.client.login()
        pass
