def add(number1,number2):
    return number1 + number2

def sub(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def crypting_password(key,text):
    textEncoded = text.encode('utf-8')
    token = key.encrypt(textEncoded)
    return token