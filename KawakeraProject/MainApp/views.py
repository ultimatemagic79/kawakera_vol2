import logging
import os.path as osp

from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CommentCreateForm
from .models import Result
from .chat import chat_knowledge

from .clip import image2text
from .classifier import image_classification
from .trans import deepl_translator
from .chara_converter import character_converter

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, "index.html")


def result(request, pk):
    result = Result.objects.get(pk=pk)
    if request.method == "POST":
        return redirect("MainApp:index")

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
        animal_name = image_classification(photo_path)

        # context -> chat
        # responses = chat
        knowledge = chat_knowledge(animal_name)

        # translation
        knowledge = deepl_translator(knowledge)

        # character converter
        knowledge = character_converter(knowledge, "normal")

        # responses -> result

        # 開発用
        # knowledge = {"name": "a", "mame": "b", "area": "c", "food": "d"}
        result = Result(
            photo_name=photo.name,
            name=knowledge["name"],
            mame=knowledge["mame"],
            area=knowledge["area"],
            food=knowledge["food"],
            user_id=self.request.user.username,
        )
        result.save()

        success_url = reverse("MainApp:result", kwargs={"pk": result.pk})
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = Result.objects.all()
        context["results"] = results
        return context
