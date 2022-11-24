import re
print(""" 1 - Считать имена и фамилии,
 2 - Считать все емайлы,
 3 - Считать названия файлов,
 4 - Считать цвета,
 5 - Выход""")

while True:
    user = int(input('выберите опцию: '))
    if user ==  1 :
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            name_list = re.findall(r"\b[A-Z][A-Za-z\]+\s[A-Za-z'\-]+\b\s", content)
            with open('name.txt', 'w', encoding='utf-8') as file_1:
                for i in name_list:
                    file_1.write(f"{i}\n")



    elif user == 2:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            emeil_list = re.findall(r"\b[a-z][a-z0-9]+@[a-z0-9-]+\.[a-z]+", content)
            with open('emeil.txt', 'w', encoding='utf-8') as file_2:
                for i in emeil_list:
                    file_2.write(f"{i}\n")

    elif user == 3:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            name_fail = re.findall(r"\t[A-Za-z][a-zA-Z]+\.[a-z]+", content)
            with open('name_fil.txt', 'w', encoding='utf-8') as file_3:
                for i in name_fail:
                    file_3.write(f"{i}\n")


    elif user == 4:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            color = re.findall(r"#[a-z0-9]+", content)
            with open('color.txt', 'w', encoding='utf-8') as file_4:
                for i in color:
                    file_4.write(f"{i}\n")


    elif user == 5:
        break












