from repository import Repository
from person import Person
class PersonService:

    def get_personList(self):
        return Repository.person

    def add_person(self, person):
        lastKey = -1
        for key in Repository.person:
            lastKey = key
        lastKey = lastKey + 1
        Repository.person [lastKey] = person.__dict__
    
    def update_person(self ,key , person): 
        Repository.person[key]['_name'] = person.name
        Repository.person[key]['_surname'] = person.surname
        Repository.person[key]['_age']= person.age

    def delete_person(self ,key):
        del Repository.person[key]
       

