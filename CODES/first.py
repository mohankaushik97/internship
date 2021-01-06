import csv
import datetime


def main(name):
    filename = 'jan.csv'

    x = datetime.datetime.now()
    month = x.strftime("%b")
    day = x.strftime("%d")
    day = day.lstrip("0")
    date = month + " " + day

    time = x.strftime("%X")

    entryAndExit(name, date, time, filename)


def entryAndExit(name, date, time, filename):
    with open(filename) as file:
        read_data = [row for row in csv.DictReader(file)]
        for i in range(len(read_data)):
            if read_data[i]['Emp Names'] == name:
                if read_data[i][date] == 'Present':
                    read_data[i + 2][date] = time
                else:
                    read_data[i][date] = 'Present'
                    read_data[i + 1][date] = time

    read_header = read_data[0].keys()
    writer(read_header, read_data, filename, "update")


def writer(header, data, filename, option):
    with open(filename, "w") as csvfile:
        if option == "write":

            w = csv.writer(csvfile)
            w.writerow(header)
            for x in data:
                w.writerow(x)
        elif option == "update":
            write = csv.DictWriter(csvfile, fieldnames=header)
            write.writeheader()
            write.writerows(data)
        else:
            print("Option is not known")


# def updater(filename):
#     with open(filename) as file:
#         read_data = [row for row in csv.DictReader(file)]
#         print(read_data)
#         read_data[1]['Jan 1'] = 'Abesnt'
#         print(read_data[1])
#
#     read_header = read_data[0].keys()
#     writer(read_header, read_data, filename, "update")


main("Chandana Deepthi Mahanthi")
