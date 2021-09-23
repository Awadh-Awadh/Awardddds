from datetime import date
from django.test import TestCase
from .models import Project, Review,Rating
from accounts.models import Profile, CustomUSer

# Create your tests here.
class TestAppClass(TestCase):

    def setUp(self): 

       self.user = CustomUSer(id = 3,email ='awadh@gmail.com')
       self.profile = Profile(profilepic = 'img.jpg',bio ='awadh',contact = '071227377',user = self.user)      
       self.project =Project(id=6,title = 'Insta',image = 'insta.jpg', description = 'Nice to show', publisher = self.profile,location = 'kisumu', date_posted = 12-5-2021)
       self.review = Review(id=3, project = self.project, review = 'nice' , reviewer = self.user,  date_reviewed = 10-10-2020 )
       self.rating = Rating(id = 3, design =4, userbility = 4, creativity = 6, content = 5, project = self.project, rated_by = self.user  )
    
    def tearDown(self):
        CustomUSer.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Review.objects.all().delete()
        Rating.objects.all().delete()


      #instances
    def test_user(self):
        self.assertTrue(isinstance(self.user, CustomUSer))
    def test_project(self):
        self.assertTrue(isinstance(self.project,Project))
    def test_review(self):
         self.assertTrue(isinstance(self.review,Review))
    def test_rating(self):
         self.assertTrue(isinstance(self.rating,Rating))
    def test_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))
    
    
    #test save methods


    def tets_save_project(self):
        self.profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_save_review(self):
        self.review.save()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)
    
    def test_save_rating(self):
        self.rating.save()
        ratings = Rating.objects.all() 
        self.assertTrue(len(ratings)>0)
    def test_save_project(self):
        self.project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

        #Delete Methods
    def test_delete_project(self):
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertAlmostEqual(len(projects), 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertAlmostEqual(len(profiles), 0)

    def test_delete_review(self):
        self.review.delete_review()
        reviews = Review.objects.all()
        self.assertAlmostEqual(len(reviews), 0)

    def test_delete_rating(self):
        self.rating.delete_rating()
        rating = Rating.objects.all()
        self.assertAlmostEqual(len(rating), 0)