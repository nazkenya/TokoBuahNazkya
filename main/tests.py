from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_non_existent_url(self):
        response = Client().get('/non_existent_url/')
        self.assertEqual(response.status_code, 404)

    def test_main_contains_specific_data(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Toko Buah Nazkya')



    
