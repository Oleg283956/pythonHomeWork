def send_email(message,recipient,*,sender = "university.help@gmail.com"):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса: '+sender+' на адрес: '+recipient)
    if korrektnost_address(recipient) * korrektnost_address(sender) == 0:
        print('Невозможно отправить письмо с адреса: '+sender+' на: '+ recipient)
    elif sender != "university.help@gmail.com" and sender != recipient:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: '+sender+' на адрес \n'
              +recipient+'.')

def korrektnost_address(s):
    result = 1
    if s.find('@') == -1:
        result = 0
    if s[-4:] != '.com' and s[-3:] != '.ru' and s[-4:] != '.net':
        result = 0
    return result

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



