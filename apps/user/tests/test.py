from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

LIST_RESOURCE = "ListUserView"
SHOW_EDIT_DELETE_RESOURCE = "RetrieveUpdateDestroyUserView"
PASS = 'passed'
TOTAL = 'total'
RESOURCE = 'user'


class UserAPITestCase(APITestCase):
    test_results = {
        LIST_RESOURCE:
            {PASS: 0, TOTAL: 0},
        SHOW_EDIT_DELETE_RESOURCE:
            {PASS: 0, TOTAL: 0}
    }

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_list_users(self):
        url = reverse(RESOURCE)  # Replace 'list-users' with the actual URL name for list user view
        response = self.client.get(url)

        track_total_result(LIST_RESOURCE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        track_test_result(LIST_RESOURCE, response.status_code == status.HTTP_200_OK)

    def test_retrieve_user(self):
        user_id = self.user.id
        url = reverse(RESOURCE, args=[
            user_id])  # Replace 'retrieve-update-destroy-user' with the actual URL name for retrieve user view
        response = self.client.get(url)

        track_total_result(SHOW_EDIT_DELETE_RESOURCE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        track_test_result(SHOW_EDIT_DELETE_RESOURCE, response.status_code == status.HTTP_200_OK)

    def test_update_user(self):
        user_id = self.user.id
        url = reverse(RESOURCE, args=[
            user_id])  # Replace 'retrieve-update-destroy-user' with the actual URL name for retrieve user view
        data = {'username': 'newusername'}
        response = self.client.patch(url, data, format='json')

        track_total_result(SHOW_EDIT_DELETE_RESOURCE)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()  # Refresh user instance from the database
        self.assertEqual(self.user.username, 'newusername1')

        track_test_result(SHOW_EDIT_DELETE_RESOURCE, self.user.username == 'newusername')

    def test_delete_user(self):
        user_id = self.user.id
        url = reverse(RESOURCE, args=[
            user_id])  # Replace 'retrieve-update-destroy-user' with the actual URL name for retrieve user view
        response = self.client.delete(url)

        track_total_result(SHOW_EDIT_DELETE_RESOURCE)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        track_test_result(SHOW_EDIT_DELETE_RESOURCE, response.status_code == status.HTTP_204_NO_CONTENT)


def track_test_result(test_name, is_passed):
    # Store the test result in the dictionary
    UserAPITestCase.test_results[test_name][PASS] += 1 if is_passed else 0


def track_total_result(test_name):
    UserAPITestCase.test_results[test_name][TOTAL] += 1


def retrieve_test_results():
    # Return the dictionary of test results
    return UserAPITestCase.test_results
