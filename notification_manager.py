import smtplib, datetime


# This class is responsible for sending notifications with the deal flight details:
#   - User logins are a private variables.
#   - API end points are constant from nikolay.irov@gmail.com accounts.

class NotificationManager:
    def __init__(self, host, user, password, good_deals):
        self.HOST = host
        self.USER = user
        self.PASS = password
        self.message = 'Hi Nikolay! \nHere are some good flight deals:'
        for flight in good_deals:
            self.message += f"\n - to {flight['cityTo']} on " \
                            f"{flight['local_departure']} will cost {flight['price']}"

    # ----------------- SEND MESSAGE FUNCTION ------------------------#
    def notification(self):
        with smtplib.SMTP(host=self.HOST) as connection:
            connection.starttls()
            connection.login(user=self.USER, password=self.PASS)
            connection.sendmail(from_addr=self.USER, to_addrs=self.USER,
                                msg=f'Subject:Cheap flights\n\n{self.message}')

    def show_notification(self):
        print(self.message)
