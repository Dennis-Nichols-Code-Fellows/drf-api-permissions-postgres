# snippets/views.py
from rest_framework import generics
from .models import Paper
from .serializers import PaperSerializer
from .permissions import IsOwnerOrReadOnly


class PaperList(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class PaperDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
