import unittest
from administration import Administration
from parameterized import parameterized
from employee import Person

class TestAdministration(unittest.TestCase):
    @parameterized.expand([
        ("Claudio","Pico", 30, 155858585,0),
        ("Claudio","Pico", 30, 155858585,1),
        ("Claudio","Pico", 30, 155858585,2)
    ])

    def test_add_employee(self, name, surname, age, phone, legajo):
        person = Person(name, surname, age, phone)
        personDict = person.get_person()

        administration = Administration()
        administration.add_employee(personDict)

        self.assertDictEqual(administration.listEmployee[legajo], personDict)  
 
if __name__ == '__main__':
    unittest.main()          