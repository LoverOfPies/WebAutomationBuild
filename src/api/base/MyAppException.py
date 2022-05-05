class MyAppException(Exception):
    def __init__(self, message):
        if message:
            self.message = message
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Ошибка, {self.message}'
        else:
            return 'Ошибка без сообщения'
