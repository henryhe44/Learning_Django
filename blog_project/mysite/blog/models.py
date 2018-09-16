from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """
    Post should have a foreign key connecting it to the 
    superuser who created the post.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Because publish_date can be blank and/or null,
        the user should be able to edit in the future.

        Ideally, the user will hit a 'publish' button
        which will take the set publish_date to the current 
        time. Of course, it'll be saved to the database.
        """
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        """
        There will be a list of comments, but only the
        approved comments should show - hence the filter.
        """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        """
        After recreating an instance of the Post, the user
        should be redirected to the post_detail page with
        the primary key of the post that was just created.
        """
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    """
    Comment should have a foreign key linking it to post.
    """
    post = models.ForeignKey('blog.Post', related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        """
        After recreating an instance of the comment, the
        user should be redirected to the post_list page.
        """
        return reverse('post_list')
    
    def __str__(self):
        return self.text