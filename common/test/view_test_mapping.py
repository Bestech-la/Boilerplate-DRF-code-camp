from apps.user.api.v1.views import RetrieveUpdateDestroyUserView
from apps.user.tests.test import UserAPITestCase

views_to_update = [
    (UserAPITestCase),
    (RetrieveUpdateDestroyUserView, UserAPITestCase)
]
