# Лабораторная №13 на создание базы данных.
# В качестве базы данных выбрана база данных пациентов больницы.
# Выполнил Белый Виктор, студент МГТУ им. Н.Э. Баумана.
from os import path


def choose(new):
    while True:
        file_path = input('Введите путь файла, пожалуйста: ')
        if file_path[-4:] != '.txt':
            print('Упс... Файл должен быть с расширением \".txt\".')
        elif not new and not path.exists(file_path):
            print('Такого файла нет на комьпьютере.')
        elif new:
            try:
                with open(file_path, 'a'):
                    pass
                return file_path
            except OSError:
                print('Некорректный относительный или абсолютный путь файла.')
        else:
            return file_path


def add_to_base(path):
    with open(path, 'a') as base:
        while True:
            try:
                people = int(input('Сколько полей планируете вставить? '))
            except ValueError:
                print('Количество полей - целое неотрицательное число.')
                continue
            break
        for i in range(people):
            data = []
            print(f'Введите, пожалуйста, данные \
{i + 1}ого пациента:')
            while True:
                name = input('Введите его ФИО: ')
                if len(name) >= 50:
                    print('Имя не может быть таким большим.')
                    continue
                data.append(name)
                break
            while True:
                try:
                    number = input('Введите его телефон: ')
                    if len(number) >= 14:
                        print('Простите, но номер телефона \
не может быть таким большим.')
                        continue
                    data.append(int(number))
                    break
                except ValueError:
                    print('Номер должен являться числовым типом.')
                    continue
                break
            while True:
                male = input('Введите его пол(М/Ж): ')
                if male != 'М' and male != 'Ж':
                    print('Обратите внимание: пол - одна буква М или Ж.')
                    continue
                data.append(male)
                break
            while True:
                try:
                    while True:
                        age = int(input('Введите его возраст: '))
                        if not 0 <= age <= 100:
                            print('Обратите внимание: возраст - число от 1 до 100.')
                            continue
                        data.append(age)
                        break
                except ValueError:
                    print('Возраст должен являться числовым типом.')
                    continue
                break

            base.write('{0:^50}'.format(data[0]))
            base.write('{0:^15}'.format(data[1]))
            base.write('{0:^10}'.format(data[2]))
            base.write('{0:^20}'.format(data[3]))
            base.write('\n')


def initialize():
    file_path = choose(True)
    with open(file_path, 'w') as base:
        example = '{0:^50}'.format('ФИО') + '{0:^15}'.format('Телефон') + '{0:^10}'.format('Пол(М/Ж)') \
                  + '{0:^20}'.format('Возраст')
        base.write(example + '\n')
    add_to_base(file_path)
    return file_path


def read_base(file_path):
    with open(file_path, 'r') as base:
        print('Содержимое базы данных:')
        while True:
            line = base.readline()
            if line == '':
                return
            print(line)


def print_results(results):
    print('Результаты поиска:')
    for line in results:
        print(line)


def find_in_base1(file_path):
    name = input('Введите, пожалуйста, \
инициалы, по которым ищем: ')
    with open(file_path, 'r') as base:
        results = []
        while True:
            line = base.readline()
            if line == '':
                print_results(results)
                return
            if line.split()[0] == name:
                results.append(line)


def find_in_base2(file_path):
    male = input('Введите, пожалуйста, \
пол, по которому ищем: ')
    age = input('Введите, пожалуйста, возраст, по которому ищем: ')
    with open(file_path) as base:
        results = []
        while True:
            line = base.readline()
            if line == '':
                print_results(results)
                return
            fields = line.split()
            if fields[-1] == age and fields[-2] == male:
                results.append(line)


def menu(file_path):
    if file_path != '':
        print('                 Меню')
        print('=======================================')
        print('    1. Выбрать файл для работы')
        print('    2. Инициализировать БД')
        print('    3. Вывести содержимое БД')
        print('    4. Добавить запись в конец БД')
        print('    5. Поиск по одному полю')
        print('    6. Поиск по двум полям')
        print('    7. Выход')
        print('=======================================')
        mode = int(input('Выберете, пожалуйста, режим работы: '))
        kill = False
        if mode == 1:
            file_path = choose(False)
        elif mode == 2:
            file_path = initialize()
        elif mode == 3:
            read_base(file_path)
        elif mode == 4:
            add_to_base(file_path)
        elif mode == 5:
            find_in_base1(file_path)
        elif mode == 6:
            find_in_base2(file_path)
        elif mode == 7:
            kill = True
        else:
            print('Простите, но ожидается число от 1 до \
7 в качестве режима работы программы.')
        return file_path, kill
    else:
        print('                 Меню')
        print('=======================================')
        print('    1. Выбрать файл для работы')
        print('    2. Инициализировать БД')
        print('    3. Выход')
        print('=======================================')
        mode = int(input('Выберете, пожалуйста, режим работы: '))
        kill = False
        if mode == 1:
            file_path = choose(False)
        elif mode == 2:
            file_path = initialize()
        elif mode == 3:
            kill = True
        else:
            print('Простите, но ожидается число от 1 до \
3 в качестве режима работы программы.')
        return file_path, kill


def main():
    file_path = ''
    while True:
        file_path, kill = menu(file_path)
        if kill:
            return


main()
