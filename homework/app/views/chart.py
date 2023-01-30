from django.shortcuts import render
from django.http import JsonResponse
""" 图表 """


def chart_list(request):
    return render(request, "chart_list.html")


# 柱状图


def chart_bar(request):
    legend = ["销量", "业绩"]

    series_list = [
        {
            "name": '销量',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20],
        },
        {
            "name": '业绩',
            "type": 'bar',
            "data": [15, 29, 46, 40, 60, 20],
        },
    ]

    x_axis = ['一月', '二月', '三月', '四月', '五月', '六月']
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    result = {
        "status":
        True,
        "data": [
            {
                "value": 2048,
                "name": 'Search Engine'
            },
            {
                "value": 735,
                "name": 'Direct'
            },
            {
                "value": 580,
                "name": 'Email'
            },
        ]
    }
    return JsonResponse(result)


def chart_line(request):
    legend = ['Line 1', 'Line 2']

    series_list = [
        {
            "data": [140, 232, 101, 264, 90, 340, 250]
        },
        {
            "data": [100, 132, 201, 104, 80, 440, 150],
        },
    ]

    x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "x_axis": x_axis,
            "series_list": series_list,
        }
    }
    return JsonResponse(result)
