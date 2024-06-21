from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category, Tag, Comment
from accounts.models import Profile

# Create your tests here.



class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Test12345')
        self.profile = Profile.objects.get(user=self.user)
        self.category = Category.objects.create(name='Django')
        self.tag = Tag.objects.create(name='Tutorial')
        self.post = Post.objects.create(
            title='Django Testing',
            content='Content of the post',
            author=self.profile
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.profile,
            content='This is a comment'
        )

    def test_create_post(self):
        # Test creating a new post
        new_post = Post.objects.create(
            title='New Post',
            content='New content',
            author=self.profile
        )
        new_post.categories.add(self.category)
        new_post.tags.add(self.tag)

        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(new_post.title, 'New Post')

    def test_read_post(self):
        # Test retrieving a post
        retrieved_post = Post.objects.get(id=self.post.id)

        self.assertEqual(retrieved_post.title, 'Django Testing')
        self.assertEqual(retrieved_post.content, 'Content of the post')

    def test_update_post(self):
        # Test updating a post
        updated_data = {
            'title': 'Updated Title',
            'content': 'Updated content',
        }
        updated_post = Post.objects.filter(id=self.post.id).update(**updated_data)
        self.post.refresh_from_db()

        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated content')

    def test_delete_post(self):
        # Test deleting a post
        post_count_before_delete = Post.objects.count()
        self.post.delete()

        self.assertEqual(Post.objects.count(), post_count_before_delete - 1)

    def test_create_comment(self):
        # Test creating a new comment
        new_comment = Comment.objects.create(
            post=self.post,
            author=self.profile,
            content='New comment'
        )

        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(new_comment.content, 'New comment')

    def test_read_comment(self):
        # Test retrieving a comment
        retrieved_comment = Comment.objects.get(id=self.comment.id)

        self.assertEqual(retrieved_comment.content, 'This is a comment')

    def test_update_comment(self):
        # Test updating a comment
        updated_data = {
            'content': 'Updated comment content',
        }
        updated_comment = Comment.objects.filter(id=self.comment.id).update(**updated_data)
        self.comment.refresh_from_db()

        self.assertEqual(self.comment.content, 'Updated comment content')

    def test_delete_comment(self):
        # Test deleting a comment
        comment_count_before_delete = Comment.objects.count()
        self.comment.delete()

        self.assertEqual(Comment.objects.count(), comment_count_before_delete - 1)

