# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader


def singUp(request):
    template = loader.get_template("singupForm.html")
    return HttpResponse(template.render())


def singIn(request):
    template = loader.get_template("singInForm.html")
    return HttpResponse(template.render())