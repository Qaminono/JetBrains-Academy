from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from hypercar.settings import TICKETS_JSON_PATH
import json


class CustomersQueue:
    def __init__(self, change_oil, inflate_tires, diagnostic):
        self.change_oil = change_oil
        self.inflate_tires = inflate_tires
        self.diagnostic = diagnostic
        self.next_ticket = None

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

    def next_client(self):
        if self.change_oil['clients']:
            self.next_ticket = self.change_oil['clients'].pop(0)
        elif self.inflate_tires['clients']:
            self.next_ticket = self.inflate_tires['clients'].pop(0)
        elif self.diagnostic['clients']:
            self.next_ticket = self.diagnostic['clients'].pop(0)
        else:
            self.next_ticket = None


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


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        context = {'change_oil_len': len(customers.change_oil['clients']),
                   'inflate_tires_len': len(customers.inflate_tires['clients']),
                   'diagnostic_len': len(customers.diagnostic['clients'])}
        return render(request, 'tickets/processing.html', context=context)

    def post(self, request, *args, **kwargs):
        customers.next_client()
        return redirect('/next')


class NextTicketView(View):
    def get(self, request, *args, **kwargs):
        if customers.next_ticket:
            return HttpResponse(f'<div>Next ticket #{customers.next_ticket}</div>')
        return HttpResponse('<div>Waiting for the next client</div>')
