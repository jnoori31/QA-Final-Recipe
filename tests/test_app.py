# Import the necessary modules
from flask import url_for
from flask_testing import TestCase
from application.models import User, Recipe

# import the app's classes and objects
from application import app, db

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        sample1 = User(username="MrMan", email_address="mrman@gmail.com", password_hash="password123")
        sample2 = Recipe(name="mrmanpie", description="hot baked pie", ingredients="eggs, flour, beef, potatoes", instructions="200 degress 30 mins", cooked=False)
        # save users to database
        db.session.add(sample2)
        db.session.add(sample1)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Test Home template cant be accessed without loging in.
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 302)


class TestC_R_U_D(TestBase):

    def test_read_recipe(self):
        response = self.client.get(url_for('read'))
        #self.assertEqual(response.status_code, 200)
        self.assertIn('mrmanpie', str(response.data))
        self.assertIn('hot baked pie', str(response.data))
        self.assertIn('eggs, flour, beef, potatoes', str(response.data))
        self.assertIn('200 degress 30 mins', str(response.data))

    def test_create_recipe(self):
        response = self.client.post(url_for('create'), data=dict(name="created recipe", description="warm recipe", 
        ingredients="recipe1", instructions= "cook for 20 mins", cooked=True),
        follow_redirects=True
        )
        #self.assertEqual(response.status_code, 200)
        self.assertIn('created recipe', str(response.data))
        self.assertIn('warm recipe', str(response.data))
        self.assertIn('recipe1', str(response.data))
        self.assertIn('cook for 20 mins', str(response.data))

    def test_update_recipe(self):
        response = self.client.post(url_for('update', name='mrmanpie'), 
        data=dict(name="updated recipe", description="cold recipe", 
        ingredients="recipe2", instructions= "cook for 30 mins", cooked=True),
        follow_redirects=True
        )
        #self.assertEqual(response.status_code, 200)
        self.assertIn('updated recipe', str(response.data))
        self.assertIn('cold recipe', str(response.data))
        self.assertIn('recipe2', str(response.data))
        self.assertIn('cook for 30 mins', str(response.data))
    
    def test_delete_recipe(self):
        response = self.client.post(url_for('delete', name="mrmanpie"),
        follow_redirects=True
        )
        #self.assertEqual(response.status_code, 200)
        self.assertNotIn('mrmanpie', str(response.data))
    #Test each template
    #Test Login
    #Test Logout
    #Test read
    #Test create
    #Test you can update
    #Test you can delete