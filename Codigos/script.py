import time
import numpy

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number + 1):
        if number % i == 0:
            return False
        return True

def is_prime2(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_prime3(number):
    sieve = numpy.ones(number + 1, dtype=bool)
    sieve[:2] = False
    for num in range(2, int(number ** 0.5) + 1):
        if sieve[num]:
            sieve[num * num::num] = False
    return numpy.nonzero(sieve)[0]

# print("Digite um numero: ")
# number = int(input())
# print(f'o numero {number} é primo -> {is_prime(number)}')

print("is_prime1")
start = time.time()
for i in range(1, 100):
    (is_prime(i))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')

start = time.time()
for i in range(1, 1000):
    (is_prime(i))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')

start = time.time()
for i in range(1, 1000000):
    (is_prime(i))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')


print("is_prime2")
start = time.time()
for i in range(1, 100):
    (is_prime2(i))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')

start = time.time()
for i in range(1, 1000):
    (is_prime2(i))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')

start = time.time()
for i in range(1, 1000000):
    (is_prime2(i))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')


print("is_prime3")
start = time.time()
(is_prime3(100))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')

start = time.time()
(is_prime3(1000))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')

start = time.time()
(is_prime3(1000000))
end = time.time()
print(f'Tempo de execução: {(end-start)*1000}')
