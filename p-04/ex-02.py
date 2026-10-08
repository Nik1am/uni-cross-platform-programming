#!/usr/bin/env python

def mail_provider(url):
    def print_mail(addr):
        print(f"{addr}@{url}")
    return print_mail


my_mail = mail_provider("gmail.com")
my_mail("mykyta.parus")
