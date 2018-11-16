from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
import random


def main(req):
    return render(req, 'r_umetea/index.html')


def response_test(req):
    return HttpResponse("レスポンステスト")


class About(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'r_umetea/about.html')


about = About.as_view()


class Omikuji:
    def tenki(self):
        ran = random.choice(list(range(5)))
        if ran == 0:
            result = "たぶん晴れ"
        elif ran == 1:
            result = "曇りかも"
        elif ran == 2:
            result = "わかんない"
        elif ran == 3:
            result = "雨だったら嫌"
        elif ran == 4:
            result = "知らんけどそんなことよりお寿司食べたい"
        return result

    def unsei(self):
        ran = random.choice(list(range(10)))
        list_message = {0: "大吉", 1: "結構ハッピー", 2: "ちょっとはいいことあるかも", 3: "平凡ないつも通りの一日",
                        4: "凶なのでガチャは爆死", 5: "大凶", 6: "絶望", 7: "悪夢", 8: "地獄", 9: "終末"}
        result = list_message[ran]
        return result


class Front(TemplateView):
    template_name = "r_umetea/front.html"
    c = Omikuji()
    tenki = c.tenki
    unsei = c.unsei
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tenki"] = self.tenki
        context["unsei"] = self.unsei
        return context

front = Front.as_view()


def error(req):
    return render(req, 'r_umetea/error.html')
