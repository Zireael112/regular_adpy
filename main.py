import re
import csv
with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
contacts_list_new = list()
pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)' \
        r'(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)' \
        r'(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'

pattern_new_update = r'+7(999)999-99-99\15\17\18'

#Заменяем значения номеров по шаблону и объединяем их
for page in contacts_list:
    page_string = ','.join(page)
    format_page = re.sub(pattern, pattern_new_update, page_string)
    page_list = format_page.split(',')
    contacts_list_new.append(page_list)

name_pattern = r'^(\w+)(\s*)(\,?)(\w+)' \
                   r'(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = list()

#Заменяем значения имён по шаблону и объединяем их
for page in contacts_list_new:
    page_string = ','.join(page)
    format_page = re.sub(name_pattern, name_pattern_new, page_string)
    page_list = format_page.split(',')
    contacts_list.append(page_list)

#Цикл для обнаружения и замены дубликатов
for i in contacts_list:
    for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1] and i is not j:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]
            if i[-1] == '':
                trash = j
    contact_list = list()
    for page in contacts_list:
        if page not in contact_list:
            contact_list.append(page)


contact_list.remove(trash)

for l in contact_list:
    if l[5] != r'+7(999)999-99-99':
        l[5] = r'+7(999)999-99-99 доб.9999'


#Запись результата в файл
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list)