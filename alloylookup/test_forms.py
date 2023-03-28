from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import (
    CreateAlloyForm,
    UpdateAlloyForm,
    CreateCategoryForm,
    UpdateCategoryForm,
    CreateSubCategoryForm,
    UpdateSubCategoryForm,
    CreateFootNoteForm,
    UpdateFootNoteForm,
    CreateCountryForm,
    UpdateCountryForm,
    RegisterUserForm,
)
User = get_user_model()

# Create your tests here.


class TestCreateAlloyForm(TestCase):
    """
    Tests for the Create Alloy Form
    """

    def test_alloy_code_is_required(self):
        """
        Test Alloy Code IS Required
        """
        form = CreateAlloyForm({
            'alloy_code': '',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertFalse(form.is_valid())
        self.assertIn('alloy_code', form.errors.keys())
        self.assertEqual(
            form.errors['alloy_code'][0],
            'This field is required.'
        )

    def test_category_is_not_required(self):
        """
        Test Category is NOT Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_subcategory_is_not_required(self):
        """
        Test Subcategory is NOT Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_alloy_description_is_required(self):
        """
        Test Alloy Description IS Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': '',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertFalse(form.is_valid())
        self.assertIn('alloy_description', form.errors.keys())
        self.assertEqual(
            form.errors['alloy_description'][0],
            'This field is required.'
        )

    def test_primary_footnote_id_is_not_required(self):
        """
        Test Primary Footnote Id is NOT Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_secondary_footnote_id_is_not_required(self):
        """
        Test Secondary Footnote Id is NOT Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_country_code_is_not_required(self):
        """
        Test Country Code is NOT Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_alloy_elements_is_required(self):
        """
        Test Alloy Elements IS Required
        """
        form = CreateAlloyForm({
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': '',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('alloy_elements', form.errors.keys())
        self.assertEqual(
            form.errors['alloy_elements'][0],
            'This field is required.'
        )

    def test_createalloyform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Create Alloy Fields Explicit in
        Form Meta Class
        """
        form = CreateAlloyForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'alloy_code',
                'category',
                'subcategory',
                'alloy_description',
                'primary_footnote_id',
                'secondary_footnote_id',
                'country_code',
                'alloy_elements'
            ]
        )


class TestUpdateAlloyForm(TestCase):
    """
    Tests for the Update Alloy Form
    """

    def test_alloy_code_is_required(self):
        """
        Test Alloy Id IS Required
        """
        form = UpdateAlloyForm({
            'id': '',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })

    def test_alloy_code_is_required(self):
        """
        Test Alloy Code IS Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertFalse(form.is_valid())
        self.assertIn('alloy_code', form.errors.keys())
        self.assertEqual(
            form.errors['alloy_code'][0],
            'This field is required.'
        )

    def test_category_is_not_required(self):
        """
        Test Category is NOT Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_subcategory_is_not_required(self):
        """
        Test Subcategory is NOT Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_alloy_description_is_required(self):
        """
        Test Alloy Description IS Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': '',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertFalse(form.is_valid())
        self.assertIn('alloy_description', form.errors.keys())
        self.assertEqual(
            form.errors['alloy_description'][0],
            'This field is required.'
        )

    def test_primary_footnote_id_is_not_required(self):
        """
        Test Primary Footnote Id is NOT Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_secondary_footnote_id_is_not_required(self):
        """
        Test Secondary Footnote Id is NOT Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_country_code_is_not_required(self):
        """
        Test Country Code is NOT Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': 'Alloy Description',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': [{}]
        })
        self.assertTrue(form.is_valid())

    def test_alloy_elements_is_required(self):
        """
        Test Alloy Elements IS Required
        """
        form = UpdateAlloyForm({
            'id': '1',
            'alloy_code': '5432',
            'category': '',
            'subcategory': '',
            'alloy_description': '',
            'primary_footnote_id': '',
            'secondary_footnote_id': '',
            'country_code': '',
            'alloy_elements': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('alloy_elements', form.errors.keys())
        self.assertEqual(
            form.errors['alloy_elements'][0],
            'This field is required.'
        )

    def test_createalloyform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Create Alloy Fields Explicit in
        Form Meta Class
        """
        form = UpdateAlloyForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'id',
                'alloy_code',
                'category',
                'subcategory',
                'alloy_description',
                'primary_footnote_id',
                'secondary_footnote_id',
                'country_code',
                'alloy_elements'
            ]
        )


class TestCreateCategoryForm(TestCase):
    """
    Tests for the Create Category Form
    """

    def test_category_id_is_required(self):
        """
        Test Category Id IS Required
        """
        form = CreateCategoryForm({
            'category_id': '',
            'category_name': 'test-category'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category_id', form.errors.keys())
        self.assertEqual(
            form.errors['category_id'][0],
            'This field is required.'
        )

    def test_category_name_is_required(self):
        """
        Test Category Name IS Required
        """
        form = CreateCategoryForm({
            'category_id': '1',
            'category_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category_name', form.errors.keys())
        self.assertEqual(
            form.errors['category_name'][0],
            'This field is required.'
        )

    def test_createcategoryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Create Category Fields Explicit in
        Form Meta Class
        """
        form = CreateCategoryForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'category_id',
                'category_name'
            ]
        )


class TestUpdateCategoryForm(TestCase):
    """
    Tests for the Update Category Form
    """

    def test_category_id_is_required(self):
        """
        Test Category Id IS Required
        """
        form = CreateCategoryForm({
            'category_id': '',
            'category_name': 'test-category'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category_id', form.errors.keys())
        self.assertEqual(
            form.errors['category_id'][0],
            'This field is required.'
        )

    def test_category_name_is_required(self):
        """
        Test Category Name IS Required
        """
        form = CreateCategoryForm({
            'category_id': '1',
            'category_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category_name', form.errors.keys())
        self.assertEqual(
            form.errors['category_name'][0],
            'This field is required.'
        )

    def test_updatecategoryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Update Category Fields Explicit in
        Form Meta Class
        """
        form = CreateCategoryForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'category_id',
                'category_name'
            ]
        )


class TestCreateSubCategoryForm(TestCase):
    """
    Tests for the Create Subcategory Form
    """

    def test_subcategory_category_is_not_required(self):
        """
        Test Subcategory Parent Category is NOT Required
        """
        form = CreateSubCategoryForm({
            'category': '',
            'subcategory_id': '10',
            'subcategory_name': 'test-subcategory'
        })
        self.assertTrue(form.is_valid())

    def test_subcategory_id_is_required(self):
        """
        Test Subcategory Id IS Required
        """
        form = CreateSubCategoryForm({
            'category': '',
            'subcategory_id': '',
            'subcategory_name': 'test-subcategory'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('subcategory_id', form.errors.keys())
        self.assertEqual(
            form.errors['subcategory_id'][0],
            'This field is required.'
        )

    def test_subcategory_name_is_required(self):
        """
        Test Subcategory Name IS Required
        """
        form = CreateSubCategoryForm({
            'category': 'test-category',
            'subcategory_id': '1',
            'subcategory_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('subcategory_name', form.errors.keys())
        self.assertEqual(
            form.errors['subcategory_name'][0],
            'This field is required.'
        )

    def test_updatesubcategoryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Update Subcategory Fields Explicit in
        Form Meta Class
        """
        form = CreateSubCategoryForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'category',
                'subcategory_id',
                'subcategory_name'
            ]
        )


class TestUpdateSubCategoryForm(TestCase):
    """
    Tests for the Update Subcategory Form
    """

    def test_subcategory_category_is_not_required(self):
        """
        Test Subcategory Parent Category is NOT Required
        """
        form = UpdateSubCategoryForm({
            'category': '',
            'subcategory_id': '10',
            'subcategory_name': 'test-subcategory'
        })
        self.assertTrue(form.is_valid())

    def test_subcategory_id_is_required(self):
        """
        Test Subcategory Id IS Required
        """
        form = UpdateSubCategoryForm({
            'category': '',
            'subcategory_id': '',
            'subcategory_name': 'test-subcategory'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('subcategory_id', form.errors.keys())
        self.assertEqual(
            form.errors['subcategory_id'][0],
            'This field is required.'
        )

    def test_subcategory_name_is_required(self):
        """
        Test Subcategory Name IS Required
        """
        form = UpdateSubCategoryForm({
            'category': 'test-category',
            'subcategory_id': '1',
            'subcategory_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('subcategory_name', form.errors.keys())
        self.assertEqual(
            form.errors['subcategory_name'][0],
            'This field is required.'
        )

    def test_updatesubcategoryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Update Subcategory Fields Explicit in
        Form Meta Class
        """
        form = UpdateSubCategoryForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'category',
                'subcategory_id',
                'subcategory_name'
            ]
        )


class TestCreateFootNoteForm(TestCase):
    """
    Tests for the Create Footnote Form
    """

    def test_footnote_id_is_required(self):
        """
        Test Footnote Id IS Required
        """
        form = CreateFootNoteForm({
            'footnote_id': '',
            'footnote': 'test-footnote'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('footnote_id', form.errors.keys())
        self.assertEqual(
            form.errors['footnote_id'][0],
            'This field is required.'
        )

    def test_footnote_is_required(self):
        """
        Test Footnote IS Required
        """
        form = CreateFootNoteForm({
            'footnote_id': '1',
            'footnote': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('footnote', form.errors.keys())
        self.assertEqual(
            form.errors['footnote'][0],
            'This field is required.'
        )

    def test_createfootnoteform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Create Footnote Fields Explicit in
        Form Meta Class
        """
        form = CreateFootNoteForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'footnote_id',
                'footnote'
            ]
        )


class TestUpdateFootNoteForm(TestCase):
    """
    Tests for the Update Footnote Form
    """

    def test_footnote_id_is_required(self):
        """
        Test Footnote Id IS Required
        """
        form = UpdateFootNoteForm({
            'footnote_id': '',
            'footnote': 'test-footnote'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('footnote_id', form.errors.keys())
        self.assertEqual(
            form.errors['footnote_id'][0],
            'This field is required.'
        )

    def test_footnote_is_required(self):
        """
        Test Footnote IS Required
        """
        form = UpdateFootNoteForm({
            'footnote_id': '1',
            'footnote': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('footnote', form.errors.keys())
        self.assertEqual(
            form.errors['footnote'][0],
            'This field is required.'
        )

    def test_updatefootnoteform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Update Footnote Fields Explicit in
        Form Meta Class
        """
        form = UpdateFootNoteForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'footnote_id',
                'footnote'
            ]
        )


class TestCreateCountryForm(TestCase):
    """
    Tests for the Create Country Form
    """

    def test_country_id_is_required(self):
        """
        Test Country Id IS Required
        """
        form = CreateCountryForm({
            'country_id': '',
            'country_name': 'test-country'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country_id', form.errors.keys())
        self.assertEqual(
            form.errors['country_id'][0],
            'This field is required.'
        )

    def test_country_name_is_required(self):
        """
        Test Country Name IS Required
        """
        form = CreateCountryForm({
            'country_id': '1',
            'country_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country_name', form.errors.keys())
        self.assertEqual(
            form.errors['country_name'][0],
            'This field is required.'
        )

    def test_createcountryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Create Country Fields Explicit in
        Form Meta Class
        """
        form = CreateCountryForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'country_id',
                'country_name'
            ]
        )


class TestUpdateCountryForm(TestCase):
    """
    Tests for the Country Footnote Form
    """

    def test_country_id_is_required(self):
        """
        Test Country Id IS Required
        """
        form = UpdateCountryForm({
            'country_id': '',
            'country_name': 'test-country'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country_id', form.errors.keys())
        self.assertEqual(
            form.errors['country_id'][0],
            'This field is required.'
        )

    def test_country_name_is_required(self):
        """
        Test Country Name IS Required
        """
        form = UpdateCountryForm({
            'country_id': '1',
            'country_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country_name', form.errors.keys())
        self.assertEqual(
            form.errors['country_name'][0],
            'This field is required.'
        )

    def test_updatecountryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Update Country Fields Explicit in
        Form Meta Class
        """
        form = UpdateCountryForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'country_id',
                'country_name'
            ]
        )


class TestRegisterUserForm(TestCase):
    """
    Test for the user registration form
    """

    def test_register_user_username_field_is_required(self):
        """
        Test User Registration - Username is Required
        """
        form = RegisterUserForm({
            'username': '',
            'email': 'test@email.com',
            'password1': 'TestPassword!',
            'password2': 'TestPassword!'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(
            form.errors['username'][0],
            'This field is required.'
        )

    def test_register_user_email_field_is_required(self):
        """
        Test User Registration - Email is Required
        """
        form = RegisterUserForm({
            'username': 'testuser',
            'email': '',
            'password1': 'testPassword1',
            'password2': 'testPassword1'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0],
            'This field is required.'
        )

    def test_register_user_password1_field_is_required(self):
        """
        Test User Registration - Password1 is Required
        """
        form = RegisterUserForm({
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': '',
            'password2': 'testPassword1'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(
            form.errors['password1'][0],
            'This field is required.'
        )

    def test_register_user_password2_field_is_required(self):
        """
        Test User Registration - Password2 is Required
        Password2 is confirmation of Password1
        """
        form = RegisterUserForm({
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'testPassword1',
            'password2': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(
            form.errors['password2'][0],
            'This field is required.'
        )

    def test_registeruserform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Register User Fields Explicit in
        Form Meta Class
        """
        form = RegisterUserForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'username',
                'email',
                'password1',
                'password2'
            ]
        )
