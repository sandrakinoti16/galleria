from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Editor,Image,Category,Location
import datetime as dt


# Create your tests here.


class CategoryTestClass(TestCase):

    # set up method
    def setUp(self):
        self.sports = Category(category='sports')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))

    # test the save method
    def test_save_method(self):
        self.general.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    def tearDown(self):
        Category.objects.filter(category='sports').delete()

    def test_update_category(self):
        Category.objects.filter(category='sports').update(category='food')


class LocationTestClass(TestCase):

    # set up method
    def setUp(self):
        self.nairobi = Location(location='nairobi')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    # test the save method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def tearDown(self):
        Location.objects.filter(location='nairobi').delete()

    def test_update_location(self):
        Location.objects.filter(location='nairobi').update(location='mombasa')


class ImageTestClass(TestCase):

    def setUp(self):
         
        self.new_category = Category(category='general')
        self.new_category.save()

        self.new_location = Location(location='nairobi')
        self.new_location.save()

        self.new_image = Image(pic='bg.jpg',title='island',description='island vibes',category=self.new_category,location=self.new_location)
        self.new_image.save()

        


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()


    def test_search_by_category(self):
        search_by_category = Image.objects.filter(category__category=self)

        return search_by_category

    def test_search_by_location(self):
        search_by_location = Image.objects.filter(location__location=self)

        return search_by_location

    def test_get_by_id(self):
        get_by_id = Image.objects.filter(pic=self.id)

        return get_by_id

    def test_update_image(self):
     
        self.updated_category = Category(category='travel')
        self.updated_category.save()

        self.updated_location = Location(location='dubai')
        self.updated_location.save()

        self.updated_image = Image.objects.filter(pic=self.id).update(pic='bg2.jpg',title='travel',description='lets visit dubai',editor=self.janja,category=self.updated_category,location=self.updated_location)
