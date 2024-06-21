
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Tag, Post, Comment
from accounts.models import Profile
import random

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        # Create Users and Profiles
        for i in range(10):
            user = User.objects.create_user(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password='password123'
            )
            profile=Profile.objects.get(user=user)
            profile.bio=f'This is bio of user{i}'
            profile.save()

        users = Profile.objects.all()

        # Create Categories
        category_names = ['Django', 'Python', 'API', 'Web Development', 'Tutorial']
        categories = []
        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)

        # # Create Tags
        tag_names = ['Beginner', 'Advanced', 'Tips', 'Tricks', 'Examples']
        tags = []
        for name in tag_names:
            tag = Tag.objects.create(name=name)
            tags.append(tag)

        # Create Posts
        

        for i in range(30):
            post = Post.objects.create(
                title=f'Post {i}',
                content=f'This is the content of post {i}.',
                author=random.choice(users)
            )
            post.categories.add(random.choice(categories))
            post.tags.add(random.choice(tags))

        posts = Post.objects.all()

        # Create Comments
        for post in posts:
            for i in range(3):
                Comment.objects.create(
                    post=post,
                    author=random.choice(users),
                    content=f'This is a comment {i} on {post.title}.'
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
