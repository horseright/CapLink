from django.contrib.auth import authenticate, login
from django.contrib.auth.views import get_user_model
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied

from .serializers import LoginSerializer, RegisterSerializer
from .forms import IdentityCertificationForm

# Create your views here.


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        ser = LoginSerializer(data=request.data)
        if ser.is_valid():
            user = authenticate(**ser.validated_data)
            if user is not None:
                login(request, user)
                return Response(data={
                    'code': 0,
                    'msg': 'ok',
                    'data': {}
                })
            return Response(data={
                'code': -1,
                'msg': 'username or password does not exist',
                'data': {}
            })
        return Response(data=ser.errors)


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        ser = RegisterSerializer(data=request.data)
        if ser.is_valid():
            data = ser.validated_data
            username = data['username']
            try:
                get_user_model().objects.get(username=username)
            except get_user_model().DoesNotExist:
                user = get_user_model().objects.create_user(username)
                user.set_password(data['password'])
                user.email = data['email']
                user.first_name = data['fullname']
                user.save()
                return Response(data={
                    'code': 0,
                    'msg': 'ok',
                    'data': {}
                })
            return Response(data={
                'code': -1,
                'msg': 'username existed',
                'data': {}
            })

        return Response(data=ser.errors)


class IdentityCertificationView(FormView):
    form_class = IdentityCertificationForm
    template_name = 'frontend/user/identitycertification.html'
    success_url = reverse_lazy('user:identitycertification')

    def form_valid(self, form):
        if hasattr(self.request.user, 'aml'):
            raise PermissionDenied
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()

        return super(IdentityCertificationView, self).form_valid(form)


class DashboardView(TemplateView):
    template_name = 'frontend/user/dashboard.html'
