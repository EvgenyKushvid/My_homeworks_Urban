
def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    conditions = ['.com', '.net', '.ru']
    if  '@'  in recipient and '@' in sender:
        flag_post = True
        flag_rec = False
        flag_sen = False
        for i in conditions:
            if i in recipient:
                flag_rec = True
            if i  in sender:
                flag_sen = True
        if flag_rec and flag_sen:
            if recipient == sender:
                flag_rs = True
                print(f'Нельзя отправить письмо самому себе!')
                return
            elif sender != "university.help@gmail.com":
                print(f'НЕСТАНДАРТНЫЙ ОТРАВИТЕЛЬ ! Письмo отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'Письмо успешно отправлено с адреса {sender}> на адрес {recipient}.')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')






