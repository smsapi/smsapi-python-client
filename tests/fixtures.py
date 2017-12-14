# -*- coding: utf-8 -*-

from smsapi.models import SendResult


def create_send_result(number):
    return SendResult(
        id="1",
        points=0.1,
        number=number,
        date_sent=1460969712,
        submitted_number=number,
        status='QUEUE')