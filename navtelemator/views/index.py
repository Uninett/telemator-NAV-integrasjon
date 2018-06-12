from django.shortcuts import render
from navtelemator import services


def render_index(request):
    return render(request,
                  'telemator/index_info.html',
                  )