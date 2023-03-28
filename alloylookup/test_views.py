from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    Group,
    Permission
    )
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from .models import (
    Alloy,
    Category,
    Subcategory,
    Footnote,
    Country
    )

# Create your tests here.

# Test for loading pages & templates


class TestViews(TestCase):
    """
    Test Views
    """

    def setUp(self):
        """
        Sets up a users for running the tests
        """
        
        # Regular User
        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user(
            'rick',
            'allen@defleppard.com',
            'ThunderGod!'
        )

        # Admin User
        AdminUser = get_user_model()
        self.client = Client()
        self.user = AdminUser.objects.create_superuser(
            'joe',
            'elliot@defleppard.com',
            'Zeff!'
        )

    def test_login(self):
        """
        Tests user login
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_admin_login(self):
        """
        Tests admin user login
        """
        self.client.login(username='joe', password='Zeff!')
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_alloy_search_page(self):
        """
        Successfully loading the Alloy Search page
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/alloy_search/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/alloy_search.html')

    def test_get_alloy_list_page(self):
        """
        Successfully loading the Alloy List page
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/alloys/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/alloy_list.html')

    def test_get_categories_list_page(self):
        """
        Successfully loading the Categories List page
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/categories/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/categories_list.html')

    def test_get_subcategories_list_page(self):
        """
        Successfully loading the Subcategories List page
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/subcategories/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/subcategories_list.html')

    def test_get_footnotes_list_page(self):
        """
        Successfully loading the Footnotes List page
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/footnotes/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/footnotes_list.html')

    def test_get_countries_list_page(self):
        """
        Successfully loading the Countries List page
        """
        self.client.login(username='rick', password='ThunderGod!')
        response = self.client.get('/countries/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/countries_list.html')

    def test_create_alloy_page(self):
        """
        Successfully loading the Create Alloy page
        """
        self.client.login(username='joe', password='Zeff!')
        response = self.client.get('/create_alloy/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/create_alloy.html')

    def test_update_alloy_page(self):
        """
        Successfully loading the Update Alloy page
        """
        self.client.login(username='joe', password='Zeff!')
        alloy = Alloy.objects.create(alloy_code='5432')
        response = self.client.get(f'/update_alloy/{alloy.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/update_alloy.html')

    def test_delete_alloy_page(self):
        """
        Successfully loading the Update Alloy page
        """
        self.client.login(username='joe', password='Zeff!')
        alloy = Alloy.objects.create(alloy_code='5432')
        response = self.client.get(
            f'/delete_alloy/{alloy.alloy_code}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/delete_alloy.html')

    def test_delete_category_page(self):
        """
        Successfully loading the Category Delete page
        """
        self.client.login(username='joe', password='Zeff!')
        category = Category.objects.create(
            category_id='1',
            category_name='test-category'
        )
        response = self.client.get(reverse('delete_category/', category.category_id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/delete_category.html')