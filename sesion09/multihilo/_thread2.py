'''
multihilo

'''
import _thread
import time

def horaActual():
    print("hola")
    #print(time.strftime("%H:%M:%S"))
    #return time.strftime("%H:%M:%S")


#2 procesos a la vez
            #funcion paralela y parametros de la f() paralela
_thread.start_new_thread(horaActual, ())

_thread.start_new_thread(horaActual, ())

#hay que bloquear al programa para que se ejecute código paralelo

time.sleep(1)










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