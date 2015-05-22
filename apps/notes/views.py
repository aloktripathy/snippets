from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Note
from .serializers import NoteSerializer, UserSerializer


class NoteList(APIView):
    """
    List all the notes or create a new one
    """
    @staticmethod
    def get(request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
    Perform various operations on note objects
    """
    @staticmethod
    def get_object(pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Fetch
        :param pk: Primary Key
        :return:
        """
        serializer = NoteSerializer(self.get_object(pk))
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        Update Object
        """
        serializer = NoteSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk, format=None):
        """
        Destroys db tuple
        """
        serializer = NoteSerializer(self.get_object(pk))
        note = self.get_object(pk)
        note.delete()
        return Response({'success': True}, status.HTTP_202_ACCEPTED)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer