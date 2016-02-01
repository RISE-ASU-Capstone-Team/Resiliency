from django.shortcuts import render
from client.serialize import PowerSerializer
from client.models import Power
from client.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets


# Create your views here.
def index(request):
    return render(request, 'client/index.html')


class PowerViewSet(viewsets.ModelViewSet):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
