from django.test import SimpleTestCase
from django.urls import reverse


class snacksTests(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse("home")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")

    def test_about_page_status(self):
        url = reverse("about")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about.html")
