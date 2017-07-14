from django.shortcuts import render


def index(request):
    # room = get_object_or_404(Room, id=roomid)
    #circuit_details = CircuitDetail.objects.filter(end=roomid)
    # cables = Cable.objects.all()
    # cables = [{id: "Kabel1"}, {id:"Kabel2"}]
    return render(request,
                  'telemator/index.html',
                  {
                  }
                  )