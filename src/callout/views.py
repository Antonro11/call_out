import os
import tempfile
import threading


from django.http import (HttpResponse, HttpResponseRedirect,
                         StreamingHttpResponse)
from django.shortcuts import render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.decorators import gzip
from django.views.generic import CreateView, TemplateView

from account.models import Customer
from callout.forms import BattleInvitationForm
from callout.models import Battle, BattleInvitation


class Invitation(CreateView):
    model = BattleInvitation
    form_class = BattleInvitationForm
    template_name = "callout/invitation.html"

    def get_context_data(self, **kwargs):
        self.extra_context = {"performer_pk": self.request.session["performer_pk"]}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.performer = Customer.objects.get(pk=self.request.session["performer_pk"])
        self.object.sender = Customer.objects.get(pk=self.request.user.pk)
        self.object.save()
        instance_user = Customer.objects.get(pk=self.request.user.pk)
        instance_performer = Customer.objects.get(pk=self.request.session["performer_pk"])
        instance_performer.invitations.add(self.object)
        instance_user.invitations.add(self.object)

        return HttpResponseRedirect(reverse_lazy("core:index"))


class BattleRoom(TemplateView):
    template_name = "callout/battle_room.html"


def video_feed(request):
    cap = cv2.VideoCapture(0)

    def frame_generator():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            _, jpeg = cv2.imencode(".jpg", frame)
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")

    response = StreamingHttpResponse(frame_generator(), content_type="multipart/x-mixed-replace; boundary=frame")

    response["Content-Length"] = -1

    return response
