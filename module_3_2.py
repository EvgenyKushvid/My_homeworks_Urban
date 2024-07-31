def send_email(message, recipient, *, sender="university.help@gmail.com"):
    conditions = ['.com', '.net', '.ru']
    if check_mail(recipient) and check_mail(sender):
        if recipient == sender:
            print(f'Нельзя отправить письмо самому себе!')
            return
        elif sender != "university.help@gmail.com":
            print(f'НЕСТАНДАРТНЫЙ ОТРАВИТЕЛЬ ! Письмo отправлено с адреса {sender} на адрес {recipient}')
            return
        else:
            print(f'Письмо успешно отправлено с адреса {sender}> на адрес {recipient}.')
            return
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return


def check_mail(mail_str):
    conditions = ['.com', '.net', '.ru']
    for i in conditions:
          if '@' in mail_str and mail_str.endswith(i):
            return True
    return False



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
