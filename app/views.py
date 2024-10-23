from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def hey_you(request: HttpRequest, name):
    return HttpResponse(f"Hey, {name}!")


def how_old(request, end, birthyear):
    total = end - birthyear
    return HttpResponse(total)


def take_order(request, burger: int, fries: int, drinks: int):
    burger_p = float(4.50 * burger)
    fries_p = float(1.50 * fries)
    total = float(burger_p) + float(fries_p) + float(drinks)

    return HttpResponse(total)