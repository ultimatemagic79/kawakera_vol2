import logging
import os.path as osp

from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CommentCreateForm
from .models import Result
from .chat import *
from .clip import *
from .classifier import *
from .trans import deepl_translator
from .chara_converter import *

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, "index.html")


def result(request, pk):
    result = Result.objects.get(pk=pk)
    return render(request, "result.html", context={"result": result})


# ホームページのビュークラス
class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = CommentCreateForm

    def form_valid(self, form):
        photo = form.cleaned_data["photo"]
        # self.request.session["photo_name"] = photo.name
        photo_path = osp.abspath(
            osp.join(
                __file__, osp.pardir, osp.pardir, "static", "media", f"{photo.name}"
            )
        )

        form.save()
        # input = form["nanka"]
        # img -> clip
        # context = clip
        # context = image2text(photo_path)
        # animal_name = image_classification(photo_path)

        # for
        # context -> chat
        # responses = chat
        # knowledge = chat_knowledge(animal_name)

        # # translation
        # knowledge = deepl_translator(knowledge)

        # # character converter
        # knowledge = character_converter(knowledge, "normal")

        # responses -> result
        # セッションにresponsesを保存する

        knowledge = {"name": "a", "mame": "b", "area": "c", "food": "d"}
        result = Result(
            photo_name=photo.name,
            name=knowledge["name"],
            mame=knowledge["mame"],
            area=knowledge["area"],
            food=knowledge["food"],
            user_id=self.request.user.username
        )
        result.save()

        # a = knowledge
        # name = a["name"]
        # mame = a["mame"]
        # area = a["area"]
        # food = a["food"]
        # self.request.session["name"] = name
        # self.request.session["mame"] = mame
        # self.request.session["area"] = area
        # self.request.session["food"] = food

        # success_url = reverse("MainApp:result", args=[str(result.pk)])
        success_url = reverse("MainApp:result", kwargs={"pk": result.pk})
        # messages.success(self.request, "解説を生成しました")
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = Result.objects.all()
        context["results"] = results
        return context


class ResultView(generic.TemplateView):
    # model = Result
    template_name = "result.html"
    # success_url = reverse_lazy("MainApp:index")
    # pk_url_kwarg = "pk"

    # responses -> template
    # def get(self, request, pk):
    #     result = Result.objects.get(pk=pk)
    #     return render(request, "result.html", {"result": result})
    # context["result"] = result
    # photo_name = self.request.session.get("photo_name")
    # name = self.request.session.get("name")
    # mame = self.request.session.get("mame")
    # area = self.request.session.get("area")
    # food = self.request.session.get("food")

    # result = Result(
    #     photo_name=photo_name, name=name, mame=mame, area=area, food=food
    # )

    # result.save()  # モデルのインスタンスを保存
    # context["photo_name"] = self.photo_name
    # context["name"] = self.name
    # context["area"] = self.area
    # context["food"] = self.food
    # context["result"] = result

    # self.request.session.pop("photo_name")
    # self.request.session.pop("name")
    # self.request.session.pop("mame")
    # self.request.session.pop("area")
    # self.request.session.pop("food")
    # return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        result = Result.objects.get(pk=pk)
        context["result"] = result

        return context

    # photo_name = self.request.session.get("photo_name")
    # name = self.request.session.get("name")
    # mame = self.request.session.get("mame")
    # area = self.request.session.get("area")
    # food = self.request.session.get("food")

    # result = Result(
    #     photo_name=photo_name, name=name, mame=mame, area=area, food=food
    # )

    # result.save()  # モデルのインスタンスを保存
    # context["photo_name"] = self.photo_name
    # context["name"] = self.name
    # context["area"] = self.area
    # context["food"] = self.food
    # context["result"] = result

    # self.request.session.pop("photo_name")
    # self.request.session.pop("name")
    # self.request.session.pop("mame")
    # self.request.session.pop("area")
    # self.request.session.pop("food")

    # indexからresponsesを受け取る
    # セッションから取り出す
    def post(self, request, *args, **kwargs):
        # POSTリクエストの処理
        return redirect("MainApp:index")
