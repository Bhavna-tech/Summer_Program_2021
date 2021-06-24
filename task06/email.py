from email.message import EmailMessage
import smtplib
# from decouple import config
import imghdr
# from django.conf import settings


# To = "bhavnalatare@gmail.com"
# Subject = "Face Detetcted !!"
# Message = f"Encountered Timestamp : {date}"
# filename = "photo.jpg"

def send_email(To, Subject, Message, files):
    print("######## Alert system !! ########\n ")
    email = "################"
    password = "##############"
    # contact-list
    contacts = []
    contacts.append(To)
    image_file = []
    for image in files:
        image_file.append(image)
    # subject
    subject = Subject

    # Mail sending initiator

    def start_service(msg):
        # Context manager to start SMTP server
        print("Starting the SMTP server\n")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            print("Loggedin to server\n")
            # Login to server
            smtp.login(email, password)
            print("sending messages\n")
            # sending email
            smtp.send_message(msg)

    # setting up msg content

    def msg_content(image_file):

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = ','.join(contacts)
        msg.set_content(Message)

        # msg.add_alternative("""\
        # <!DOCTYPE html>
        #     <html>
        #         <body>
        #             <h1>Hello</h1>
        #         </body>
        #     </html>
        # """, subtype='html')

        def upload_img(image_file):
            #img_file is list
            for file in image_file:
                # opening attachment file
                with open(file, 'rb') as f:
                    #loading file in ram -- >var f =type(dict) f{name, mem_size,file_type,encoding} is the varibale --> mulitple attributes 
                    file_data = f.read()

                    # file type (Image type )
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                msg.add_attachment(file_data, maintype='image',
                                   subtype=file_type, filename=file_name)
                # uploading files (Images)
                print('Image uploaded successfully\n')

        upload_img(image_file)
        start_service(msg)

    msg_content(image_file)
    print("Exiting mail sender")
