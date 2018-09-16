# Django Blog Project

### About
Create your run-of-the-mill social media blog with Django and rainbows. As a superuser, you should be able to create posts. Those posts will wait in the drafts section for approval. Once they're approved, they can be seen by all and can commented on by other individuals. These comments will also require approval from the superuser.

### Issues
The features I described in the about section has been achieved. There is a minor issue about the time field in one of the Django Models and the medium editor not wanting to work for whatever reason. 

### Running it
You should be able to just use the command "python manage.py runserver" and it should work right off the bat. Though, I would recommend first using "python manage.py makemigrations" then "python manage.py migrate" just to be extra sure. You may also want to create your own superuser via "python manage.py createsuperuser" to interact with the blog.
