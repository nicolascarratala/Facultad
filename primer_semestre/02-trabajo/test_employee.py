import unittest
from employee import Employee, Person
from parameterized import parameterized

class TestPerson(unittest.TestCase):

    def test_get_person(self):
        person = Person("Claudio", 32)
        listPerson = person.get_person()
        self.assertEqual(listPerson, ["Claudio", 32])  

class TestEmployee(unittest.TestCase):
     
    def test_get_employee(self):
        employee = Employee("Claudio", 30, 40000)
        listEmployee = employee.get_employee()
        self.assertEqual(listEmployee, ["Claudio", 30, 40000]) 
    
    def test_pay_tax_pay(self):
        employee = Employee("Claudio", 30, 20000)
        tax = employee.pay_tax()
        self.assertEqual(tax, "No paga impuestos")

    def test_pay_tax_no_pay(self):
        employee = Employee("Claudio", 30, 40000)
        tax = employee.pay_tax()
        self.assertEqual(tax, "Paga impuestos")    

if __name__ == '__main__':
    unittest.main()     