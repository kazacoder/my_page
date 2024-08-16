from django.shortcuts import render
from django.views import View


# Create your views here.


class CameraGo(View):
    def get(self, request):
        return render(request, 'camera/camera_go.html')