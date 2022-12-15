from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from celery_tasks.tasks import test_task
from apps.musics.models import Music
from apps.musics import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    # [GET] /api/musics/{pk}/detail/
    @action(detail=True, methods=['get'], url_path='detail')
    def detail_action(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song
        }
        return Response(result, status=status.HTTP_200_OK)

    # [GET] /api/musics/all_singer/
    @action(detail=False, methods=['get'], url_path='all_singer')
    def all_singer(self, request):
        test_task.delay()
        music = Music.objects.values_list('singer', flat=True).distinct()
        return Response(music, status=status.HTTP_200_OK)
