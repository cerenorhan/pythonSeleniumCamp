# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


studentList = []

# Listedeki tüm öğrencileri tek tek ekrana yazdıran
def printStudentList():
    for student in studentList:
        print(student.title())

printStudentList()

# Aldığı isim soy isim ile listeye öğrenci ekleyen
def addStudent ():
    name = input("Please add student's name: ")
    surname = input("Please add student's surname: ")
    if not name.isalpha() and not surname.isalpha():
        print("Please use only letters!")
    else:
        studentList.append(name + " " + surname)
        print(name.title() + " " + surname.title() + " added the student list. ")
    
addStudent()
printStudentList()

# Listeye birden fazla öğrenci eklemeyi mümkün kılan
def addMultipleStudent():
    numberOfStudents =input("Please enter the number of students you want to add: ")
    for i in range(int(numberOfStudents)):
        addStudent()

addMultipleStudent()
printStudentList()

# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def removeStudent():
    nameRemove = input("Please type the name of the student you want to delete: ")
    surnameRemove = input("Please type the surname of the student you want to delete: ")
    studentName = nameRemove + " " + surnameRemove
    studentList.remove(studentName)
    print(studentName.title() + " removed from the student list")

removeStudent()
printStudentList()

#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def removeMultipleStudent():
    numberOfStudentsRemove = input("Please enter the number of students you want to remove: ")
    i = 0
    while (i < int(numberOfStudentsRemove)):
        removeStudent()
        i += 1
    print("Students deleted.")

removeMultipleStudent()
printStudentList()

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def studentNo():
  whichStudent=input("Please enter the name and surname of the student whose number you want to see: ")
  print((studentList.index(whichStudent))+1)

studentNo()
