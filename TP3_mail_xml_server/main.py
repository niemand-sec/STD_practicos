__author__ = 'BlackSwan'

import poplib
import xml.etree.cElementTree as ET

def fitler_list( mail ):
    del mail[0]
    del mail[0]
    del mail[4]
    del mail[4]
    return mail


def check_valid_email( email ):
    e = ET.parse('email_list.xml').getroot()
    email = email.split(" ",1)[1]
    for email_xml in e.findall('email'):
        if email == email_xml.text :
            return True
    return False



pop3_host = 'sdtdd.com'
pop3_user = 'joel@sdtdd'
pop3_pass = 'perritoo'

# connect to server
pop3_mail = poplib.POP3('127.0.0.1')

# print msg from server
print pop3_mail.getwelcome()

# send user
pop3_mail.user(pop3_user)

# send password
pop3_mail.pass_(pop3_pass)

## get mail stats
pop3_stat = pop3_mail.stat()

print "New Mails : %s (%s bytes)" % pop3_stat

## fetching last mail
print "\n\n===\tLatest Mail\t===\n\n"
latest_email = pop3_mail.retr(pop3_stat[0])

email = fitler_list(latest_email[1])

for lines in range(len(email)):
    print email[lines]

## Showing all messages
print "\n\n===\tShowing all mails\t===\n\n"

root = ET.Element("mails")


number_of_mails = pop3_stat[0]
for i in range(number_of_mails):
    recv = fitler_list(pop3_mail.retr(i+1)[1])
    doc = ET.SubElement(root, "mail")
    if check_valid_email(recv[0]) :
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

    print trama

tree = ET.ElementTree(root)
tree.write("mails.xml")


e = ET.parse('mails.xml').getroot()

for mail in e.findall('mail'):
    field1 = mail.find('From')
    field2 = mail.find('To')
    field3 = mail.find('Subject')
    field4 = mail.find('Date')
    for campo_trama in mail.find('trama'):
        timestamp = campo_trama.find('timestamp')
        temperatura = campo_trama.find('temperatura')
        tension = campo_trama.find('tension')
        corriente = campo_trama.find('corriente')
        potencia = campo_trama.find('potencia')
        presion =campo_trama.find('presion')





#YYYY-MM-DDTHH:MM:SS
#datetime.isoformat([sep])
#Return a string representing the date and time in ISO 8601 format, YYYY-MM-DDTHH:MM:SS.mmmmmm or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS