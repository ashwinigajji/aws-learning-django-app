from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    send_mail("Heloooo", "Updated...............","kambalapallysrinivas2@gmail.com",["kambalapallysrinivas2@gmail.com"])
    queryset = Note.objects.all()
