from django.test import TestCase
from django.contrib.auth.models import User as auth_user
from . import models

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        user = auth_user.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        user_instance = auth_user.objects.get(id=1)
        models.SuggestionModel.objects.create(suggestion="lion", author=user_instance)
        models.SuggestionModel.objects.create(suggestion="cat", author=user_instance)

    def test_suggestion_to_string(self):
        lion = models.SuggestionModel.objects.get(suggestion="lion")
        cat = models.SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(str(lion),"john lion")
        self.assertEqual(str(cat),"john cat")

class CommentTestCase(TestCase):
    def setUp(self):
        user = auth_user.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        user_instance = auth_user.objects.get(id=1)
        sugg = models.SuggestionModel.objects.create(suggestion="lion", author=user_instance)
        models.CommentModel.objects.create(comment="cat", suggestion=sugg, author=user_instance)

    def test_suggestion_to_string(self):
        cat = models.CommentModel.objects.get(comment="cat")
        self.assertEqual(str(cat),"john cat")
