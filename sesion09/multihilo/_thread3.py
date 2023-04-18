'''
multihilo

'''
import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    count = 0
    while count < 5:
        time.sleep(tiempo_de_espera)
        print(f'hilo {nombre_thread} - {time.ctime(time.time())} - {count} terminado')
        count += 1
    
        #print(time.strftime("%H:%M:%S"))
        #return time.strftime("%H:%M:%S")


#2 procesos a la vez
            #funcion paralela y parametros de la f() paralela
_thread.start_new_thread(horaActual, ("thread1", 1)) # ejecutar hora actual cada 1 seg

_thread.start_new_thread(horaActual, ("thread2", 2)) #ejecutar hora actual cada 2 seg

print('fin ejecucion... he disparado ya los hilos')

#hay que bloquear al programa para que se ejecute código paralelo

#bucle infinito... el progrma no finaliza
while True:
    time.sleep(0.1)



'''
fin ejecucion... he disparado ya los hilos
hilo thread1 - Tue Apr 18 01:34:10 2023 - 0 terminado
hilo thread2 - Tue Apr 18 01:34:11 2023 - 0 terminado
hilo thread1 - Tue Apr 18 01:34:11 2023 - 1 terminado
hilo thread1 - Tue Apr 18 01:34:12 2023 - 2 terminado
hilo thread2 - Tue Apr 18 01:34:13 2023 - 1 terminado
hilo thread1 - Tue Apr 18 01:34:13 2023 - 3 terminado
hilo thread1 - Tue Apr 18 01:34:14 2023 - 4 terminado
hilo thread2 - Tue Apr 18 01:34:15 2023 - 2 terminado
hilo thread2 - Tue Apr 18 01:34:17 2023 - 3 terminado
hilo thread2 - Tue Apr 18 01:34:19 2023 - 4 terminado
'''

'''
def hilo1():
    print('hilo1')
    time.sleep(1)
    print('hilo1 terminado')

def hilo2():
    print('hilo2')
    time.sleep(1)
    print('hilo2 terminado')
'''

