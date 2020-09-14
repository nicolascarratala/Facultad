import unittest
from employee import Employee, Person
from parameterized import parameterized

class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ("Claudio", 30,["Claudio", 30])
    ])

    def test_get_person(self, name, age, result):
        person = Person(name, age)
        listPerson = person.get_person()
        self.assertEqual(listPerson, result)  

class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ("Claudio", 30, 40000,["Claudio", 30, 40000])
    ])

    def test_get_employee(self, nombre, edad, salario, result):
        employee = Employee(nombre, edad, salario)
        listEmployee = employee.get_employee()
        self.assertEqual(listEmployee, result) 

    @parameterized.expand([
        ("Claudio", 40, 20000, "No paga impuestos"),
        ("Claudio", 30, 40000, "Paga impuestos")
    ])
    
    def test_pay_tax_pay(self, nombre, edad, salario, result):
        employee = Employee(nombre, edad, salario)
        tax = employee.pay_tax()
        self.assertEqual(tax, result)
        
if __name__ == '__main__':
    unittest.main()     