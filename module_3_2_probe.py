# ЗАДАЧА - "РАССЫЛКА ПИСЕМ."
# 1) Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель
# и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
def send_email(message, recipient, *, sender="uversity.help@gmail.com"): # "sender" помечен как именнованный параметр.
    """Создал функцию с двумя обычными аргументами и одним именованным"""
    # Проверка наличия ключевых символов перед отправкой письма.
    error = ""
    if sender == recipient:
        error = "Нельзя отправить письмо самому себе!"
        print(error)
        return
    if recipient.count("@") == 1 \
        and recipient.count(".") == 1 \
        and recipient[0] != "@" \
        and recipient.rfind(".") > recipient.find("@") \
        and recipient.count("com") \
        or recipient.count("net") \
        or recipient.count("ru"):
        print("Valid_email")
    else:
        print("Invalid")
    print(message, recipient, sender)
    print(recipient.count(".com"))
send_email("Доброго времени суток, поступил в ваше распоряжение, письмо для проверки связи",
           "nanatoliy26@gmail.com")
send_email("Доброго времени суток, в задании есть ошибки - поработайте над этим!",
           "nanatoliy26@gmail.com", sender="urban.fan@mail.ru")

mess = "nanatoliy26@gmail.com.com.com"
print(mess.count(".com"))
# check_symbols = set("@.com.ru.net")
#     if any((c in check_symbols) for c in recipient) and any((c in check_symbols) for c in sender):
#         print(f"Письмо успешно отправлено на адрес {recipient} с адреса {sender}.")
#     else:
#         print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
