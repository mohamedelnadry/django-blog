from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username = "testuser",email="test@email.com",password="secret")
        cls.post = Post.objects.create(
            title = "this is a title",
            body = "this is body testing",
            author = cls.user
        )
    def test_post_model(self):
        self.assertEqual(self.post.title, "this is a title")
        self.assertEqual(self.post.body, "this is body testing")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "this is a title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_usrl_listview(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)
    def test_usrl_detailview(self):
        res = self.client.get('/post/1/')
        self.assertEqual(res.status_code,200)

    def test_post_listview(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code,200)
        self.assertContains(res,"this is a title")
        self.assertTemplateUsed(res,"pages/home.html")
    def test_post_detailview(self):
        res = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_res = self.client.get("/post/100000/")
        self.assertEqual(res.status_code,200)
        self.assertEqual(no_res.status_code,404)
        self.assertContains(res,"this is body testing")
        self.assertTemplateUsed(res,"pages/detail_view.html")
    def test_post_createview(self):
        res = self.client.post(reverse("post_add"),{
            "title":"new title",
            "body":"New body",
            "author":self.user.id
        },)
        self.assertEqual(res.status_code,302)
        self.assertEqual(Post.objects.last().title, "new title")
        self.assertEqual(Post.objects.last().body, "New body")
        self.assertTemplateUsed("pages/post_create.html")
    def test_post_updateview(self):
        res = self.client.post(reverse("post_edit",args="1"),{
            "title":"updated title",
            "body":"updated body",
        },)
        self.assertEqual(res.status_code,302)
        self.assertEqual(Post.objects.last().title, "updated title")
        self.assertEqual(Post.objects.last().body, "updated body")
        self.assertTemplateUsed("pages/post_edit.html")
    def test_post_deleteview(self): 
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)