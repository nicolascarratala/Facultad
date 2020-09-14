import os                                                                       
from multiprocessing import Pool 
from Server import play                                              
from BrowserEngine import start_window                                                                          
from multiprocessing import Process
import os


def func1():
    print("Tests")
    os.system('python src.test_producto.py')


def func2():
    print("playserver")
    play()


def func3():
    print("browser")
    start_window()


if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p3 = Process(target=func3)
  p3.start()
  p1.join()
  p2.join()
  p3.join()