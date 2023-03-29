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
        response = self.client.get('/alloy-search/', follow=True)
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
        self.assertTemplateUsed(
            response,
            'alloylookup/subcategories_list.html'
        )

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
        response = self.client.get('/create-alloy/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/create_alloy.html')

    def test_update_alloy_page(self):
        """
        Successfully loading the Update Alloy page
        """
        self.client.login(username='joe', password='Zeff!')
        alloy = Alloy.objects.create(alloy_code='5432')
        response = self.client.get(f'/update-alloy/{alloy.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/update_alloy.html')

    def test_delete_alloy_page(self):
        """
        Successfully loading the Delete Alloy page
        """
        self.client.login(username='joe', password='Zeff!')
        alloy = Alloy.objects.create(alloy_code='5432')
        response = self.client.get(
            f'/delete-alloy/{alloy.id}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/delete_alloy.html')

    def test_add_category_page(self):
        """
        Successfully loading the Add Category page
        """
        self.client.login(username='joe', password='Zeff!')
        response = self.client.get('/create-category/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/create_category.html')

    def test_update_category_page(self):
        """
        Successfully loading the Update Category page
        """
        self.client.login(username='joe', password='Zeff!')
        category = Category.objects.create(
            category_id='1',
            category_name='test-category'
        )
        response = self.client.get(
            f'/update-category/{category.category_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/update_category.html')

    def test_delete_category_page(self):
        """
        Successfully loading the Category Delete page
        """
        self.client.login(username='joe', password='Zeff!')
        category = Category.objects.create(
            category_id='1',
            category_name='test-category'
        )
        response = self.client.get(
            f'/delete-category/{category.category_id}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/delete_category.html')

    def test_add_subcategory_page(self):
        """
        Successfully loading the Add Subcategory page
        """
        self.client.login(username='joe', password='Zeff!')
        response = self.client.get('/create-subcategory/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'alloylookup/create_subcategory.html'
        )

    def test_update_subcategory_page(self):
        """
        Successfully loading the Update Subcategory page
        """
        self.client.login(username='joe', password='Zeff!')
        subcategory = Subcategory.objects.create(
            subcategory_id='1',
            subcategory_name='test-subcategory'
        )
        response = self.client.get(
            f'/update-subcategory/{subcategory.subcategory_id}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'alloylookup/update_subcategory.html'
        )

    def test_delete_subcategory_page(self):
        """
        Successfully loading the Category Delete page
        """
        self.client.login(username='joe', password='Zeff!')
        subcategory = Subcategory.objects.create(
            subcategory_id='1',
            subcategory_name='test-category'
        )
        response = self.client.get(
            f'/delete-subcategory/{subcategory.subcategory_id}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'alloylookup/delete_subcategory.html'
        )

    def test_add_footnote_page(self):
        """
        Successfully loading the Add Footnote page
        """
        self.client.login(username='joe', password='Zeff!')
        response = self.client.get('/create-footnote/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/create_footnote.html')

    def test_update_footnote_page(self):
        """
        Successfully loading the Update Footnote page
        """
        self.client.login(username='joe', password='Zeff!')
        footnote = Footnote.objects.create(
            footnote_id='1',
            footnote='test-footnote'
        )
        response = self.client.get(
            f'/update-footnote/{footnote.footnote_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/update_footnote.html')

    def test_delete_footnote_page(self):
        """
        Successfully loading the Footnote Delete page
        """
        self.client.login(username='joe', password='Zeff!')
        footnote = Footnote.objects.create(
            footnote_id='1',
            footnote='test-footnote'
        )
        response = self.client.get(
            f'/delete-footnote/{footnote.footnote_id}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/delete_footnote.html')

    def test_add_country_page(self):
        """
        Successfully loading the Add Country page
        """
        self.client.login(username='joe', password='Zeff!')
        response = self.client.get('/create-country/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/create_country.html')

    def test_update_country_page(self):
        """
        Successfully loading the Update Country page
        """
        self.client.login(username='joe', password='Zeff!')
        country = Country.objects.create(
            country_id='1',
            country_name='test-country'
        )
        response = self.client.get(
            f'/update-country/{country.country_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/update_country.html')

    def test_delete_country_page(self):
        """
        Successfully loading the Country Delete page
        """
        self.client.login(username='joe', password='Zeff!')
        country = Country.objects.create(
            country_id='1',
            country_name='test-country'
        )
        response = self.client.get(
            f'/delete-country/{country.country_id}',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alloylookup/delete_country.html')
