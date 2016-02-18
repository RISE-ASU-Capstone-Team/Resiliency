from django.shortcuts import render
from client.serialize import PowerSerializer
from client.models import Power
from client.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, response, status, settings, decorators


# Create your views here.
def index(request):
    return render(request, 'client/index.html')


class PowerViewSet(viewsets.ModelViewSet):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

    @decorators.detail_route(methods=['post'])
    def new_node(self, request, **kwargs):
        print(request.data)
        serializer = PowerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data,
                                 status=status.HTTP_201_CREATED,
                                 headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[settings.api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}
