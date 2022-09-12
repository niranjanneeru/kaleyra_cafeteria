import threading
import datetime
from typing import Any

from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated

from kaleyra_cafeteria.foods.models import Snacks
from kaleyra_cafeteria.users.api.utils import sms


class BreakFastSMSAPIView(ListAPIView):
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if request.user.is_superuser:
            return Response(status=200)
        else:
            raise NotAuthenticated


class SnackSMSAPIView(ListAPIView):
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if request.user.is_superuser:
            snacks = Snacks.objects.filter(date=datetime.date.today()).first()
            if snacks:
                data = {}
                for user in snacks.users.all():
                    data[user.name] = user.phone_number
                x = threading.Thread(target=sms, args=(data,))
                x.start()
            return Response(status=200)
        else:
            raise NotAuthenticated
