__author__ = 'BlackSwan'

import poplib


def fitler_list( mail ):
    del mail[0]
    del mail[0]
    del mail[4]
    del mail[4]
    return mail


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


number_of_mails = pop3_stat[0]
for i in range(number_of_mails):
    recv = fitler_list(pop3_mail.retr(i+1)[1])
    for mail in recv:
        print mail
