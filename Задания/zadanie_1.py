#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def get_train():
    destination = input("Пункт назначения: ")
    train_number = input("Номер поезда: ")
    departure_time = datetime.strptime(
        input("Время отправления (в формате HH:MM): "),
        "%H:%M"
    )

    return {
        'destination': destination,
        'train_number': train_number,
        'departure_time': departure_time,
    }


def display_trains(trains):
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 25,
            '-' * 15,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^25} | {:^15} | {:^20} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)

        for idx, train in enumerate(trains, 1):
            time_str = train.get('departure_time').strftime("%H:%M")

            print(
                '| {:>4} | {:<25} | {:<15} | {:<20} |'.format(
                    idx,
                    train.get('destination', ''),
                    train.get('train_number', ''),
                    time_str
                )
            )
            print(line)
    else:
        print("Список поездов пуст.")


def select_trains(trains, destination):
    result = []
    for train in trains:
        if train.get('destination').lower() == destination.lower():
            result.append(train)
    return result


def main():
    trains = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            train = get_train()
            trains.append(train)

            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('departure_time'))

        elif command == "list":
            display_trains(trains)

        elif command.startswith("select "):
            parts = command.split(" ", maxsplit=1)
            destination = parts[1]

            selected = select_trains(trains, destination)

            if selected:
                display_trains(selected)
            else:
                print("Поездов в пункт '{}' не найдено.".format(destination))

        elif command == "help":
            print("Список команд:\n")
            print("add - добавить поезд")
            print("list - вывести список всех поездов")
            print("select <пункт назначения> - найти поезда по пункту назначения")
            print("help - отобразить справку")
            print("exit - завершить работу с программой")

        else:
            print("Неизвестная команда {}".format(command), file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())


    