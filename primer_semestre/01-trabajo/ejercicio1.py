import unittest
from sorting import Sort

def InserLista (lista):
    for j in range (1,len(lista)):
        valor = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > valor:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = valor
    return lista

class SortListaTest(unittest.TestCase):
    def testList1(self):
        lista1 = [36,71,16,21,73,9,0,40,66,7]
        bub1 = Sort().BubbleSort(lista1)
        self.assertEqual(InserLista(lista1), bub1)
    
    def testList2(self):
        lista2 = [0,2,23,4,2,8,1,25,6,9]
        bub2 = Sort().BubbleSort(lista2)
        self.assertEqual(InserLista(lista2), bub2)

    def testList3 (self):
        lista3 = [5,0,15,25,21,35,40,25,6,9]
        bub3 = Sort().BubbleSort(lista3)
        self.assertEqual(InserLista(lista3), bub3)

if __name__ == "__main__":
    unittest.main()