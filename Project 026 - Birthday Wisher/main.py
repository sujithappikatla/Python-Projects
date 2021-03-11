import datetime as dt
import smtplib
import random
import pandas


def send_email(to_address, subject):
    my_email = "your_email@gmail.com"
    my_password = "email_password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject:Happy Birthday!!!\n\n{subject}"
        )


now = dt.datetime.now()
month = now.month
day = now.day

df = pandas.read_csv("birthdays.csv")

for index, row in df.iterrows():
    if int(row["month"]) == month and int(row["day"] == day):
        letter_choice = random.randint(1, 3)
        filename = "letter_templates/letter_"+str(letter_choice)+".txt"
        with open(filename, "r") as file:
            template = file.read()
        template = template.replace("[NAME]", row["name"])
        send_email(row["email"], template)
