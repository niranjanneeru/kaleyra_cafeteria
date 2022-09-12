import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from kaleyra_cafeteria.foods.models import Breakfast, Snacks


class HomeView(View):
    def get(self, request):
        context = {
            'breakfast': None,
            'snacks': None
        }
        if request.user.is_authenticated:
            breakfast = Breakfast.objects.filter(date=datetime.date.today()).first()
            if breakfast:
                context['breakfast'] = breakfast
                context['breakfast_count'] = breakfast.users.all().count()
            else:
                # TODO
                # WARNING PART OF TESTING
                # AUTOMATIC BREAKFAST GENERATION
                breakfast = Breakfast.objects.create(date=datetime.date.today(),
                                                     title="Dish of the Day",
                                                     description="Dummy Description",
                                                     price=10)
                context['breakfast'] = breakfast
                context['breakfast_count'] = 0

            snacks = Snacks.objects.filter(date=datetime.date.today()).first()
            if snacks:
                context['snacks'] = snacks
                context['snacks_count'] = snacks.users.all().count()
            else:
                # TODO
                # WARNING PART OF TESTING
                # AUTOMATIC BREAKFAST GENERATION
                snacks = Snacks.objects.create(date=datetime.date.today(),
                                               title="Dish of the Day",
                                               description="Dummy Description",
                                               price=10)
                context['snacks'] = snacks
                context['snacks_count'] = 0
        return render(request, 'pages/home.html', context)


class OptView(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            breakfast = Breakfast.objects.filter(date=datetime.date.today()).first()
            if breakfast:
                context['breakfast'] = breakfast
                context['breakfast_count'] = breakfast.users.all().count()
                context['b_opt_in'] = request.user in breakfast.users.all()
            snacks = Snacks.objects.filter(date=datetime.date.today()).first()
            if snacks:
                context['snacks'] = snacks
                context['snacks_count'] = snacks.users.all().count()
                context['s_opt_in'] = request.user in snacks.users.all()
        return render(request, 'pages/about.html', context)

    def post(self, request):
        context = {}
        if request.user.is_authenticated:
            if 'snacks-accept' in request.POST:
                snacks = Snacks.objects.filter(date=datetime.date.today()).first()
                if snacks:
                    snacks.users.add(request.user)
                    snacks.save()
            if 'break-fast-accept' in request.POST:
                breakfast = Breakfast.objects.filter(date=datetime.date.today()).first()
                if breakfast:
                    breakfast.users.add(request.user)
                    breakfast.save()
            if 'snacks-reject' in request.POST:
                snacks = Snacks.objects.filter(date=datetime.date.today()).first()
                if snacks:
                    snacks.users.remove(request.user)
                    snacks.save()
            if 'break-fast-reject' in request.POST:
                breakfast = Breakfast.objects.filter(date=datetime.date.today()).first()
                if breakfast:
                    breakfast.users.remove(request.user)
                    breakfast.save()
        return redirect('/opt')


class ProfileView(View):
    def post(self, request):
        if request.user.is_authenticated:
            phone_number = request.POST.get('phone')
            if phone_number:
                if phone_number != request.user.phone_number:
                    request.user.phone_number = phone_number
                    request.user.is_profile_complete = True
                    request.user.save()
            return redirect('users:detail', request.user.username)
        return HttpResponse("Unauthorized", status=401)


profile_view = ProfileView.as_view()
