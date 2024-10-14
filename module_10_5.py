import  multiprocessing
from datetime import datetime

filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while (line := file.readline()):
            all_data.append(line)

def linejn():
    res = []
    time_start = datetime.now()
    res = list(map(read_info,filenames))
    time_end = datetime.now()
    time_res = time_end - time_start
    print(f'{time_res} (линейный)')

def multiproc():
    time_start1 = datetime.now()
    results = []
    if __name__ == "__main__":
        pool = multiprocessing.Pool()
        results = pool.map(read_info,filenames)
        pool.close()
        pool.terminate()
        if results != []:
            time_end1 = datetime.now()
            time_res1 = time_end1 - time_start1
            print(f'{time_res1} (многопроцессный)')


#linejn()
multiproc()
