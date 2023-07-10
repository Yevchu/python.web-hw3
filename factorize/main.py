import time
import multiprocessing

numbers = [128, 255, 99999, 10651060]

def factorize(numbers):
    factors = []
    for num in numbers:
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
    return factors


def factorize_process(numbers):
    factors = []
    for i in range(1, numbers + 1):
        if numbers % i == 0:
            factors.append(i)
    return factors

def process_number(numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(factorize_process, numbers)
    return result

if __name__ == '__main__':

    start_time_sinc = time.time() 
    result_sinc  = factorize(numbers)
    end_time_sinc = time.time() 
    execution_time_sinc = end_time_sinc - start_time_sinc 

    start_time_process = time.time() 
    result_process  = process_number(numbers)
    end_time_process = time.time() 
    execution_time_process = end_time_process - start_time_process 


    print(f'Sinc time: {execution_time_sinc}')
    print(f'Multiprocess time: {execution_time_process}')