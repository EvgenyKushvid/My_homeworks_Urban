

import  datetime
import multiprocessing

#0:00:08.637999 линейный
#0:00:03.586923 многопроцессный

def read_info(name):
    all_data = []
    with open (f'{name}', "r", encoding= "UTF8") as file:
        while file.readline():
            string = file.readline()
            all_data.append(string)

start = datetime.datetime.now()

file_names = [f'./test_files/file {i}.txt' for i in range(1,5)]

for name in file_names:
    read_info(name)

end = datetime.datetime.now()
print(end - start, 'линейный')

if __name__ == '__main__':

    with multiprocessing.Pool(processes=4) as pool:

        start = datetime.datetime.now()

        pool.map(read_info,file_names)

        end = datetime.datetime.now()
        print(end - start, 'многопроцессный')
