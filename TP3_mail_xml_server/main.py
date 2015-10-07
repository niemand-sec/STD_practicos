__author__ = 'BlackSwan'

import poplib
import xml.etree.cElementTree as ET
from ClassEmails import Email
import easygui
import sys
import re
import time


from Tkinter    import Tk
from contextlib import contextmanager

@contextmanager
def tk(timeout=5):
    root = Tk() # default root
    root.withdraw() # remove from the screen

    # destroy all widgets in `timeout` seconds
    func_id = root.after(int(1000*timeout), root.quit)
    try:
        yield root
    finally: # cleanup
        root.after_cancel(func_id) # cancel callback
        root.destroy()


def fitler_list( mail ):
    del mail[0]
    del mail[0]
    del mail[4]
    del mail[4]
    return mail


def check_valid_email( email ):
    e = ET.parse('email_list.xml').getroot()
    email_from = email[0].split(" ",1)[1]
    pattern = re.compile('>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2};-*[0-9]+;-*[0-9]+;[0-9]+;[0-9]+;[0-9]+<')
    for email_xml in e.findall('email'):
        if email_from == email_xml.text :
            if pattern.match(recv[5]) :
                print "VALID EMAIL PROCESSED from " + email_from
                return True
            else :
                print "EMAIL DROPPED DUE TO INVALID FRAME -- (" + recv[5] + ")"
                #pop3_mail.dele(i+1) #BORRAR MAIL INVALIDO
                return False
    print "EMAIL DROPPED DUE TO INVALID ADDRESS from " + email_from
    #pop3_mail.dele(i+1) #BORRAR MAIL INVALIDO
    return False


while(True) :

    msg = "Mail Server"
    title = "Mail Server POP3 Config "
    fieldNames = ["Verification Time(seg)","Address","User Name","User Password" ]
    fieldValues_mail = ["10","127.0.0.1","joel@sdtdd", "perritoo"]  # we start with blanks for the values
    fieldValues_mail = easygui.multpasswordbox(msg,title, fieldNames,fieldValues_mail)
    if fieldValues_mail == None:
        break

    vTime = int(fieldValues_mail[0])
    pop3_user = fieldValues_mail[2]
    pop3_pass = fieldValues_mail[3]
    pop3_server = fieldValues_mail[1]

    while (True):

        # connect to server

        pop3_mail = poplib.POP3(pop3_server)


        # send user
        pop3_mail.user(pop3_user)

        # send password
        try :
            pop3_mail.pass_(pop3_pass)
        except :
            easygui.msgbox("Invalid Email/Password", title="Error")
            break

        ## get mail stats
        pop3_stat = pop3_mail.stat()

        sys.stdout = open('output', 'w')

        root = ET.Element("mails")

        valid_email_list = 0
        number_of_mails = pop3_stat[0]
        #GUARDAR MAILS EN UN ARREGLO Y BORRAR LOS QUE NO SON VALIDOS
        for i in range(number_of_mails):
            recv = fitler_list(pop3_mail.retr(i+1)[1])
            if check_valid_email(recv) :
                valid_email_list += 1
                doc = ET.SubElement(root, "mail")
                ET.SubElement(doc, "From").text = recv[0]
                ET.SubElement(doc, "To").text = recv[1]
                ET.SubElement(doc, "Subject").text = recv[2]
                ET.SubElement(doc, "Date").text = recv[3]
                xml_trame =  ET.SubElement(doc, "trama",)
                trama = recv[5].strip(">").strip("<").split(";")
                ET.SubElement(xml_trame, "timestamp").text = trama[0]
                ET.SubElement(xml_trame, "temperatura").text = trama[1]
                ET.SubElement(xml_trame, "tension").text = trama[2]
                ET.SubElement(xml_trame, "corriente").text = trama[3]
                ET.SubElement(xml_trame, "potencia").text = trama[4]
                ET.SubElement(xml_trame, "presion").text = trama[5]
            else :
                pass

        tree = ET.ElementTree(root)
        tree.write("mails.xml")

        e = ET.parse('mails.xml').getroot()

        emails = []

        for mail in e.findall('mail'):
            email = Email()
            email.a_from = mail.find('From').text
            email.a_to = mail.find('To').text
            email.a_subject = mail.find('Subject').text
            email.a_date = mail.find('Date').text
            for campo_trama in mail.findall('trama'):
                email.a_timestamp = campo_trama.find('timestamp').text
                email.a_temperatura = campo_trama.find('temperatura').text
                email.a_tension = campo_trama.find('tension').text
                email.a_corriente = campo_trama.find('corriente').text
                email.a_potencia = campo_trama.find('potencia').text
                email.a_presion =campo_trama.find('presion').text
            emails.append(email)


        #msg = "Mailbox"
        #title = "Select the email to open"
        #choices = []
        #for mail in emails :
        #      choices.append(vars(mail).get('a_subject'))




        #choice = easygui.choicebox(msg, title, choices) ##Si pasan 10 segundos en esta linea refrezcar

        #if choice == None:
        #    break

        for mList in range(len(emails)):
            #if  choice in vars(emails[mList]).get('a_subject') :
            values_correo = vars(emails[mList])
            print "========== INIT EMAIL =========="
            print values_correo.get('a_from')
            print values_correo.get('a_to')
            print values_correo.get('a_subject')
            print "Values:"
            print "\t Timestamp: \t\t" + values_correo.get('a_timestamp')
            print "\t Temperature: \t\t" + values_correo.get('a_temperatura') + "[C]"
            print "\t Tension: \t\t\t" + values_correo.get('a_tension') + "[V]"
            print "\t Corriente: \t\t" + values_correo.get('a_corriente') + "[A]"
            print "\t Potencia: \t\t\t" + values_correo.get('a_potencia') + "[W]"
            print "\t Presion: \t\t\t" + values_correo.get('a_presion') + "[PSI]"
            print "========== END EMAIL =========="





        #print "New Mails : %s (%s bytes)" % pop3_stat

        ## fetching last mail
        #print "\n\n===\tLatest Mail\t===\n\n"
        #latest_email = pop3_mail.retr(pop3_stat[0])

        #email = fitler_list(latest_email[1])

        #for lines in range(len(email)):
        #    print email[lines]

        ## Showing all messages
        #print "\n\n===\tShowing all mails\t===\n\n"



        """
        for correo in emails:
            values_correo = vars(correo)
            print "========== INIT EMAIL =========="
            print values_correo.get('a_from')
            print values_correo.get('a_to')
            print values_correo.get('a_subject')
            print "Values:"
            print "\t Timestamp: \t\t" + values_correo.get('a_timestamp')
            print "\t Temperature: \t\t" + values_correo.get('a_temperatura') + "[C]"
            print "\t Tension: \t\t\t" + values_correo.get('a_tension') + "[V]"
            print "\t Corriente: \t\t" + values_correo.get('a_corriente') + "[A]"
            print "\t Potencia: \t\t\t" + values_correo.get('a_potencia') + "[W]"
            print "\t Presion: \t\t\t" + values_correo.get('a_presion') + "[PSI]"
            print "========== END EMAIL =========="
        """

        #msg = choice
        title = "Mailbox"
        sys.stdout = open ('output', 'r')


        with tk(timeout=vTime):
            easygui.codebox(msg, title, sys.stdout.readlines()  )

        #YYYY-MM-DDTHH:MM:SS
        #datetime.isoformat([sep])
        #Return a string representing the date and time in ISO 8601 format, YYYY-MM-DDTHH:MM:SS.mmmmmm or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS
        #time.sleep(vTime)
        pop3_mail.quit()
