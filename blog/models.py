from django.db import models

# from taggit.managers import TaggableManager


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publication date', auto_now_add=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    # tags = TaggableManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=300)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.text
