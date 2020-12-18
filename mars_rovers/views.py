from mars_rovers.models import Plane, Rover
from mars_rovers.serializers import PlaneSerializer, RoverSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view


class RoverList(generics.ListCreateAPIView):
    # TODO: Get user, limit list to rovers of user
    # TODO: check if this is necessary if I get the owner from the auth session in the model.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        print("self", self)
        return Rover.objects.filter(owner=self.request.user)
    serializer_class = RoverSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoverDetail(generics.RetrieveUpdateDestroyAPIView):
    # TODO: Get user, limit list to rovers of user
    def get_queryset(self):
        return Rover.objects.filter(owner=self.request.user)
    serializer_class = RoverSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# TODO: not sure these crud endpoints should stay as none of these are really needed
class PlaneList(generics.ListCreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    def get_queryset(self):
        return Plane.objects.filter(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlaneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    def get_queryset(self):
        return Plane.objects.filter(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['POST'])
def deploy_rovers(request):
    """
    Deploy rovers!
    Give coordinates of the rovers to deploy and the size of the plane,
    and give them movement instructions.
    Returns new coordinates of the rovers and the direction they're facing.
    """