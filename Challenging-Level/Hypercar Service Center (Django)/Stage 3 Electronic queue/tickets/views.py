from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from hypercar.settings import TICKETS_JSON_PATH
import json


class CustomersQueue:
    def __init__(self, change_oil, inflate_tires, diagnostic):
        self.change_oil = change_oil
        self.inflate_tires = inflate_tires
        self.diagnostic = diagnostic

    def add_client(self, procedure):
        ticket_num = len(self.change_oil['clients']) + \
                     len(self.inflate_tires['clients']) + \
                     len(self.diagnostic['clients']) + 1
        if procedure == 'change_oil':
            time = len(self.change_oil['clients']) * self.change_oil['processing_time']
            self.change_oil['clients'].append(ticket_num)
        elif procedure == 'inflate_tires':
            time = len(self.change_oil['clients']) * self.change_oil['processing_time'] + \
                   len(self.inflate_tires['clients']) * self.inflate_tires['processing_time']
            self.inflate_tires['clients'].append(ticket_num)
        elif procedure == 'diagnostic':
            time = len(self.change_oil['clients']) * self.change_oil['processing_time'] + \
                   len(self.inflate_tires['clients']) * self.inflate_tires['processing_time'] + \
                   len(self.diagnostic['clients']) * self.diagnostic['processing_time']
            self.diagnostic['clients'].append(ticket_num)
        # json.dump([self.change_oil, self.inflate_tires, self.diagnostic], open(TICKETS_JSON_PATH, 'w')) when need
        return ticket_num, time


# customers = CustomersQueue(*json.load(open(TICKETS_JSON_PATH))) when need
customers = CustomersQueue(*json.loads('[{"clients": [], "processing_time": 2}, {"clients": [], "processing_time": 5},'
                                       ' {"clients": [], "processing_time": 30}]'))


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/menu.html')


class GetTicketView(View):
    def get(self, request, procedure, *args, **kwargs):
        ticket_num, time = customers.add_client(procedure)
        return render(request, 'tickets/get_ticket.html', context={'ticket_num': ticket_num, 'time': time})
