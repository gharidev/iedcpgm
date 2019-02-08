class Students:
    name=""
    age=""

    def display(self,x,y):
        Students.name=x
        Students.age=y
        print(Students.name)
        print(Students.age)

s=Students()
s.display("Haridev","18")