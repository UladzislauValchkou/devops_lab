#!/bin/python
""" script for github API """
# pylint:disable=invalid-name
# pylint:disable=line-too-long
import argparse
import getpass
import calendar
from datetime import datetime
import requests

parser = argparse.ArgumentParser()
parser.add_argument("user", help="your username")
parser.add_argument("repowner", help="repository`s owner login")
parser.add_argument("repository", help="enter repository name")
parser.add_argument("--version", help='Prints programm version', action="store_true")
parser.add_argument("-l", "--label", help='Returns labels name', action="store_true")
parser.add_argument("-cc", "--comments_created", help="Prints comments quantity on each pull request", action="store_true")
parser.add_argument("-n", "--name", help="Prints repository name", action="store_true")
parser.add_argument("-cd", "--creationday", help="Prints creation day of week", action="store_true")
parser.add_argument("-cl", "--closed", help="Prints label name + close day + close date", action="store_true")

pars = parser.parse_args()

repo = pars.repository
user_name = pars.user
rep_own = pars.repowner
password = getpass.getpass(prompt="Enter your password: ")



url = "https://api.github.com/repos/" + rep_own + "/" + repo + "/" + "pulls"
request = requests.get(url, auth=(user_name, password))
json_dump = request.json()


if pars.label:
    for i in json_dump:
        print("Label name:", i.get("head").get("label"))
elif pars.version:
    print("Programm version: 1.0.0")
elif pars.name:
    print(json_dump[0].get("base").get("repo").get("name"))
elif pars.comments_created:
    for i in json_dump:
        print(i.get("comments"))
elif pars.creationday:
    date_creation = (json_dump[0].get("base").get("repo").get("created_at"))[:10]
    datetime_object = datetime.strptime(date_creation, '%Y-%m-%d')
    day_of_week = calendar.day_name[datetime_object.weekday()]
    print(day_of_week)
elif pars.closed:
    url_closed = url + "?state=closed"
    request_closed = requests.get(url_closed, auth=(user_name, password))
    json_dump_closed = request_closed.json()
    for i in json_dump_closed:
        date_creation = (i.get("closed_at"))[:10]
        datetime_object = datetime.strptime(date_creation, '%Y-%m-%d')
        day_of_week = calendar.day_name[datetime_object.weekday()]
        label_name = (i.get("head").get("label"))
        print(label_name, day_of_week, date_creation)
else:
    print("Enter correct key")
