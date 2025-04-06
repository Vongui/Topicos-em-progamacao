from datetime import datetime
class Agenda:
    def __init__(self):
        self.data = ''
        self.idagenda = 0
        self.horario = ''
        self.compromisso = ''
        self.status = ''
        self.usuario = ''

    def get_data(self):
        return self.data

    def set_data(self, value):
        value = value.strftime("%Y-%m-%d")
        self.data = value

    def get_idagenda(self):
        return self.idagenda

    def set_idagenda(self, value):
        self.idagenda = value

    def get_horario(self):
        return self.horario

    def set_horario(self, value):
        self.horario = value

    def get_compromisso(self):
        return self.compromisso

    def set_compromisso(self, value):
        self.compromisso = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, value):
        self.usuario = value

    def __str__(self):
        return f"Agenda(data={self.data}, horario={self.horario}, compromisso={self.compromisso}, status={self.status}, usuario={self.usuario})"
