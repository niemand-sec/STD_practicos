__author__ = 'BlackSwan'


class Email:

    # def __init__(self, a_from, a_to, a_date, a_timestamp, a_temperatura, a_tension, a_corriente, a_potencia, a_presion) :
    #     self.a_from = a_from
    #     self.a_to = a_to
    #     self.a_date = a_date
    #     self.a_timestamp = a_timestamp
    #     self.a_temperatura = a_temperatura
    #     self.a_tension = a_tension
    #     self.a_corriente = a_corriente
    #     self.a_potencia = a_potencia
    #     self.a_presion = a_presion

    def email(self, a_from, a_to, a_subject, a_date, a_timestamp, a_temperatura, a_tension, a_corriente, a_potencia, a_presion) :
        self.a_from = a_from
        self.a_to = a_to
        self.a_subject = a_subject
        self.a_date = a_date
        self.a_timestamp = a_timestamp
        self.a_temperatura = a_temperatura
        self.a_tension = a_tension
        self.a_corriente = a_corriente
        self.a_potencia = a_potencia
        self.a_presion = a_presion