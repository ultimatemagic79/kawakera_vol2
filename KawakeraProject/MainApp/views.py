import logging

from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse

from .forms import CommentCreateForm
from .models import Result
from .chat import *
from .clip import *

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, "index.html")


def result(request):
    return render(request, "result.html")


# ホームページのビュークラス
class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = CommentCreateForm
    success_url = reverse_lazy("MainApp:result")

    def form_valid(self, form):
        photo = form.cleaned_data["photo"]
        self.request.session["photo_name"] = photo.name
        form.save()
        # input = form["nanka"]
        # img -> clip
        # context = clip
        context = image2text()

        # for
        # context -> chat
        # responses = chat
        knowledge = chat_knowledge(context)

        # responses -> result
        # セッションにresponsesを保存する

        a = {"name": "ぱんだ", "mame": "でかい", "area": "中国", "food": "笹"}
        name = a["name"]
        mame = a["mame"]
        area = a["area"]
        food = a["food"]
        self.request.session["name"] = name
        self.request.session["mame"] = mame
        self.request.session["area"] = area
        self.request.session["food"] = food
        messages.success(self.request, "解説を生成しました")
        return super().form_valid(form)


class ResultView(generic.TemplateView):
    model = Result
    template_name = "result.html"
    success_url = reverse_lazy("MainApp:index")

    # responses -> template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_name = self.request.session.get("photo_name")
        name = self.request.session.get("name")
        mame = self.request.session.get("mame")
        area = self.request.session.get("area")
        food = self.request.session.get("food")

        result = Result(
            photo_name=photo_name, name=name, mame=mame, area=area, food=food
        )

        result.save()  # モデルのインスタンスを保存
        # context["photo_name"] = self.photo_name
        # context["name"] = self.name
        # context["area"] = self.area
        # context["food"] = self.food
        context["result"] = result

        self.request.session.pop("photo_name")
        self.request.session.pop("name")
        self.request.session.pop("mame")
        self.request.session.pop("area")
        self.request.session.pop("food")
        return context

    # indexからresponsesを受け取る
    # セッションから取り出す
    def post(self, request, *args, **kwargs):
        # POSTリクエストの処理
        return redirect("MainApp:index")
