from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    time_start = datetime.now()
    with open(file_name, 'w', encoding= 'utf8') as f:
       for i in range(1,word_count+1):
            f.write(f"Какое-то слово № {i}"+'\n')
            sleep(0.1)

    time_end = datetime.now()
    print (f"Завершилась запись в файл {file_name} time: {time_end - time_start}")


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Общее время выполнения {time_end - time_start}')

time_start = datetime.now()
thr_5 =  Thread(target = write_words,args = (10, 'example5.txt'))
thr_6=  Thread(target = write_words,args = (30, 'example6.txt'))
thr_7 =  Thread(target = write_words,args = (200, 'example7.txt'))
thr_8 =  Thread(target = write_words,args = (100, 'example8.txt'))

thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()

thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()
time_end = datetime.now()
print(f'Общее время выполнения {time_end - time_start}')










