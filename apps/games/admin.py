from django.contrib import admin

from .models import Game, Action, GameImg, Faq, GameTag

# Register your models here.


class ActionInline(admin.TabularInline):
    model = Action


class GameImgInline(admin.TabularInline):
    model = GameImg


class FaqInline(admin.TabularInline):
    model = Faq


@admin.register(Game)
class GameModelAdmin(admin.ModelAdmin):
    inlines = (ActionInline, GameImgInline, FaqInline)


@admin.register(GameTag)
class GameTagModelAdmin(admin.ModelAdmin):
    pass
