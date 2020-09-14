from person import Person
from personService import PersonService

if __name__ == '__main__':
   
    personService = PersonService()

    #Agregamos una persona
    p1 = Person()
    p1.name = 'federico'
    p1.surname = 'gonzalez'
    p1.age = '20'
    personService.add_person(p1)

    #Agregamos una persona
    p1 = Person()
    p1.name ='claudio'
    p1.surname = 'pico'
    p1.age = '33'
    personService.add_person(p1)

    #Agregamos al hermano
    p2 = p1
    p2.name = 'nicolas'
    p2.age = 30
    personService.add_person(p2)
    
    print (personService.get_personList()) # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}}

    #Update person
    p2.age = 41
    personService.update_person(1, p2)
    
    print (personService.get_personList()) 
    

    #delte person
    personService.delete_person(2)
    print (personService.get_personList()) #{0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'NICOLAS', '_surname': 'NICOLAS', '_age': 41}}
