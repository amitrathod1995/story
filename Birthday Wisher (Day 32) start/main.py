# import smtplib

# my_email ="amitrathod857@gmail.com"
# password ="pjan gnlk jutr omdt"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=["amitrathod9834@gmail.com", "amit101rathod@gmail.com"],
#         msg="Subject:Hello\n\n This is the Body of my email"
#     )
# import datetime as dt

# now =dt.datetime.now()
# year=now.year 
# month=now.month
# dayofweek=now.weekday()
# print(month)
# print(year)
# print(dayofweek)
import smtplib
import datetime as dt
import random
my_email ="amitrathod857@gmail.com"
password ="pjan gnlk jutr omdt"
now =dt.datetime.now()
dayofweek=now.weekday()
if dayofweek == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
     connection.starttls()
     connection.login(user=my_email, password=password)
     connection.sendmail(
        from_addr=my_email,
        to_addrs=["amitrathod9834@gmail.com", "amit101rathod@gmail.com"],
        msg=f"Subject:Hello\n\n{quote}"
    )
