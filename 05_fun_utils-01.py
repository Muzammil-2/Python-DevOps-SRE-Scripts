# import os

# command = "df -h"
# command = "uptime"
# command = "date"
# def check_cpu(command):
#    print(os.system(command))

# def check_date(command):
#   print(os.system(command))

# def run_command(command):
#   print(os.system(command))

# run_command("date")

# WAP to print Today date and time
import os
import datetime

def run_command(command):
    return os.system(command)
def show_date():
    return datetime.datetime.today()
today = show_date()
print (today)