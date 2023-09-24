from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone = models.PositiveBigIntegerField()
    is_admin = models.BooleanField()
    prod_user_access = models.ManyToManyField(Product, through="Product_user_access", through_fields=("product", "user"), )


class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("User", on_delete=models.RESTRICT)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_url = models.URLField(max_length=250, unique=True)
    video_duration_in_sec = models.PositiveSmallIntegerField()
    prod_less = models.ManyToManyField(Product, through="Product_lesson", through_fields=("product", "lesson"),)
    user_less = models.ManyToManyField(User, through="User_lesson", through_fields=("user", "lesson"),)


class Product_lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    models.UniqueConstraint(fields=['product', 'lesson'], name='prod_less_unique_entering')


class User_lesson_views(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    watched_seconds = models.PositiveSmallIntegerField()
    view_status = models.BooleanField(default=False)
    date_last_update = models.DateTimeField(auto_now_=True)
    models.UniqueConstraint(fields=['user', 'lesson'], name='user_les_unique_entering')


class Product_user_access(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    date_access_granted = models.DateTimeField(auto_now_add=True)
    models.UniqueConstraint(fields=['product', 'user'], name='prod_user_unique_entering')