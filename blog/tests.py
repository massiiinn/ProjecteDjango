from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Author, Post, Tag
from django.db.utils import IntegrityError
from django.db import transaction
from datetime import date

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Massin",
            last_name="Ouchen",
            email="massin@example.com"
        )

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, "Massin")

    def test_author_str(self):
        self.assertEqual(str(self.author), "Massin Ouchen")

    def test_author_email_unique(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Author.objects.create(
                    first_name="Test",
                    last_name="User",
                    email="massin@example.com"
                )

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(tag="Django")

    def test_tag_creation(self):
        self.assertEqual(self.tag.tag, "Django")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Django")

    def test_tag_unique(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Tag.objects.create(tag="Django")

class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Laura",
            last_name="Coder",
            email="laura@example.com"
        )
        self.tag = Tag.objects.create(tag="Python")

        self.post = Post.objects.create(
            title="Primera Entrada",
            excerpt="Un petit resum",
            image_name="post1.jpg",
            date=date.today(),
            slug="primera-entrada",
            content="Contingut del post",
            author=self.author
        )
        self.post.tags.add(self.tag)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Primera Entrada")
        self.assertEqual(self.post.author.email, "laura@example.com")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Primera Entrada")

    def test_post_has_tags(self):
        self.assertIn(self.tag, self.post.tags.all())

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(
            first_name="Sara",
            last_name="Python",
            email="sara@example.com"
        )
        self.post = Post.objects.create(
            title="Test Post",
            excerpt="Excerpt...",
            image_name="post1.jpg",
            date=date.today(),
            slug="test-post",
            content="Contingut test",
            author=self.author
        )

    def test_starting_page_view(self):
        response = self.client.get(reverse('starting_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_posts_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_authors_view(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sara")
        self.assertContains(response, "Python")
