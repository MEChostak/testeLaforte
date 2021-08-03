from nose.tools import eq_
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from testeLaforte.urls import router


class TrackingTests(APITestCase):
    urlpatterns = router.urls
    print(urlpatterns)
    username = 'fe142559-1955-429f-9b0d-4a2f81758b6a'
    token = 'e582efb4-a780-4e25-ad17-4ecdc238273e'
    newToken = ''
    id = ''
    tracking_number = '23568978'
    order_id = '23568978'

    def setUp(self):
        client = APIClient()
        url = reverse('tracking-list')
        data = {
            "tracking_number": self.tracking_number,
            "order_id": self.order_id,
        }
        print("data", data)
        response = client.post(url, data, format='json')
        print(response)
        print("response", response)
        eq_(response.status_code, status.HTTP_201_CREATED)

    def test_get_data_(self):

        client = APIClient()

        url = reverse('tracking-list')
        # print("url", url)

        client.credentials(HTTP_AUTHORIZATION='token ' + self.newToken)
        response = client.get(url, format='json')
        eq_(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        # Dealing with the results now
        results = response.data
        # Seeing the if the user created inside setup is the same here
        print(results)
