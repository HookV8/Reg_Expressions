import csv
import re


def input_data():
    with open('phonebook_raw.csv', encoding='utf-8') as f:
        input_list = list(csv.reader(f))
    return input_list

def repair_list():
    contact_list = []
    pattern = re.compile(r"(8|\+7)?\s*\(*(\d{3})\)*(\s*|\-)(\d{3})\-*(\d{2})\-*(\d{2})(\s\(*(\доб.)\s*(\d{4})\)*)*")
    phone_sub = r"+7(\2)\4-\5-\6 \8\9"
    for l in input_data():
        lfs = " ".join(l[:3])
        person_list = lfs.split(" ", 2)
        person_list.append(l[3])
        person_list.append(l[4])
        person_list.append(pattern.sub(phone_sub, l[5]))
        person_list.append(l[6])
        contact_list.append(person_list)
    return contact_list

def delete_duplicates():
    contact_dict = {}
    for contact in repair_list():
        if contact[0] in contact_dict:
            contact_values = contact_dict[contact[0]]
            for i in range(len(contact_values)):
                if (contact_values[i]) == '':
                    contact_values[i] = contact[i]
        else:
            contact_dict[contact[0]] = contact
    return list(contact_dict.values())

def main():
    print(delete_duplicates())
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(delete_duplicates())

if __name__ == '__main__':
    main()


