# 9 Python program to print all the items in a dictionary
phone_book = {
    'Naruto': ['1234567890', 'konoha@gmail.com'],
    'Itachi': ['0987654321', 'akatsuki@mail.com'],
    'Sasuke': ['7777777777', 'sakura@itachi.com']
}
for k, v in phone_book.items():
    print(k, ":", v)
