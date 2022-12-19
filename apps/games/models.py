from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField


# Create your models here.


class GameTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "游戏标签"
        verbose_name_plural = verbose_name


class Game(models.Model):
    name = models.CharField(max_length=255)
    description = MDTextField()
    disclaimer = MDTextField()
    tags = models.ManyToManyField(GameTag)
    short_desc = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("games:detail", kwargs={"pk": self.pk})

    @property
    def main_img(self):
        return self.gameimg_set.filter(main=True).first()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "游戏"
        verbose_name_plural = verbose_name


class Action(models.Model):
    text = models.CharField(max_length=255)
    url = models.TextField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = "动作"
        verbose_name_plural = verbose_name


class GameImg(models.Model):
    img = models.ImageField(upload_to="gameimages")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = "游戏图片"
        verbose_name_plural = verbose_name


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "faq"
        verbose_name_plural = verbose_name


"""
text
url
"""
