import pywhatkit
def send_what(date):
    message=f"face detected at {date}"
    pywhatkit.sendwhatmsg_instantly(reciver,message)