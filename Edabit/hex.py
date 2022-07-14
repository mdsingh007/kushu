import string


def convert_to_hex(txt):
    # encoding = 'utf-8'
    hex1 = []
    for elem in txt:
        hex1.append(elem.encode('utf-8').hex())
    
    return " ".join(hex1)
    # return " ".join(hex)


# a = "hello world".encode('utf-8')

print(convert_to_hex("hello world"))