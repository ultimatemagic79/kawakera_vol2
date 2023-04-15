import logging

from django.shortcuts import render
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
        photo = form.cleaned_data['photo']
        self.request.session['photo_name'] = photo.name
        form.save()
        # input = form["nanka"]
        # img -> clip
        # context = clip

        # for
        # context -> chat
        # responses = chat

        # responses -> result
        # セッションにresponsesを保存する
        
        a = {"name": "ぱんだ", "area": "中国", "food": "笹"}
        name = a["name"]
        area = a["area"]
        food = a["food"]
        self.request.session['name'] = name
        self.request.session['area'] = area
        self.request.session['food'] = food
        
        messages.success(self.request, "解説を生成しました")
        return super().form_valid(form)


class ResultView(generic.TemplateView):
    model = Result
    template_name = "result.html"
    success_url = reverse_lazy("MainApp:index")

    # indexからresponsesを受け取る
    # セッションから取り出す
    # responses -> template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.photo_name = self.request.session.get('photo_name')
        self.name = self.request.session.get('name')
        self.area = self.request.session.get('area')
        self.food = self.request.session.get('food')
        
        context["photo_name"] = self.photo_name
        context["name"] = self.name
        context["area"] = self.area
        context["food"] = self.food
        
        self.request.session.pop('photo_name')
        self.request.session.pop('name')
        self.request.session.pop('area')
        self.request.session.pop('food')
        return context
