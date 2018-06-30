import datetime
import random

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from faker import Faker
from rest_framework import generics

from service.generate_api_credentials import spreadsheet_service
from service.models import Member
from service.serializer import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


def create_test_people(request):
    fake = Faker('hu_HU')
    for i in range(100):
        u = User.objects.create_user(username=''.join(fake.name()), password=fake.password)
        u.save()
        p = Member(user=u, name=fake.name(), phone=fake.phone_number(), button_id=i,
                   should_be_contacted=random.choice([True, False]))
        p.save()
    return JsonResponse({"Success": "True"})


def generate_call_list(request):
    spreadsheet = spreadsheet_service.spreadsheets()
    body = {'properties': {'title': 'Call List {}'.format(datetime.date.today())}}

    request = spreadsheet.create(body=body)
    response = request.execute()

    print(response)

    spreadsheet_id = response['spreadsheetId']

    column_names = ["Name", "Phone number"]
    call_list_entries = [[member.name, member.phone] for member in Member.objects.all() if member.should_be_contacted]

    batch_update_values_request_body = {
        "valueInputOption": "RAW",

        'data': [
            {
                "values": [column_names] + call_list_entries,
                "range": "Sheet1!A1"
            }
        ],
    }

    request2 = spreadsheet.values().batchUpdate(spreadsheetId=spreadsheet_id,
                                                body=batch_update_values_request_body)
    response2 = request2.execute()

    print(response2)

    json_response = {
        "Success": "True"
    }
    return JsonResponse(json_response)


@login_required
def button(request):
    u = User.objects.get(id=request.user.pk)
    m = Member.objects.get(user=u)
    return render(request, 'button.html', {'user': u, 'member': m})


def howto(request):
    return render(request, 'howto.html')


def logout_view(request):
    logout(request)
