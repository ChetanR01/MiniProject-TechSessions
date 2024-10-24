import mysql.connector
import datetime
from datetime import date

global fine_per_day
fine_per_day=5

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="library"
)

def main_menu():
    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("\n1. Student Management")
        print("2. Book Management")
        print("3. Book Issue")
        print("4. Return Book")
        print("5. Lost Book ")
        print("0. Exit")
        choice=int(input("Enter your choice...... : "))

        if choice==1:
            stud_manage()
    
        if choice==2:
            book_manage()
    
        if choice==3:
            book_issue()

        if choice==4:
            book_return()

        if choice==5:
            book_lost()

        if choice==0:
            break

def stud_manage():
    print("\n1.Add student")
    print("2. Update Student")
    print("3. Delete Student")
    ch=int(input("Enter your choice...... : "))
    if ch==1:
        def add_stud():
            mycursor = mydb.cursor()
            id=int(input("Enter student ID: "))
            name=input("Enter student name: ")
            sql="INSERT INTO student(stud_id,stud_name)values(%s,%s)"
            val=(id,name)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nStudent details added successfully")
        add_stud()
    if ch==2:
        def update_stud():
            mycursor = mydb.cursor()
            old_id=int(input("Enter old student ID: "))
            new_name=input("Enter new student name: ")
            new_id=int(input("Enter new student ID: "))
            sql="UPDATE student SET stud_id=%s,stud_name=%s WHERE stud_id=%s"
            val=(old_id,new_name,new_id)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nStudent details updated successfully")
        update_stud()
    if ch==3:
        def del_stud():
            mycursor = mydb.cursor()
            id=int(input("Enter student ID: "))
            sql="DELETE FROM student WHERE stud_id=%s"
            val=[id]
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nStudent details deleted successfully")
        del_stud()

def book_manage():
     print("\n1.Add Book")
     print("2. Update Book")
     print("3. Delete Book")
     print("4. Display Books")
     choice=int(input("Enter your choice...... : "))
     if choice==1:
        def add_book():
             mycursor = mydb.cursor()
             book_id=int(input("Enter Book id: "))
             title=input("Enter Book Title: ")
             author=input("Enter Book Author: ")
             publisher=input("Enter Book Publisher: ")
             b_status=input("Enter Book Status: ")
             copies=int(input("Enter Book copies: "))
             sql="INSERT INTO book(book_id,title,author,publisher,b_status,copies)values(%s,%s,%s,%s,%s,%s)"
             val=(book_id,title,author,publisher,b_status,copies)
             mycursor.execute(sql,val)
             mydb.commit()
             print("\nBook added successfully")
        add_book()
     if choice==2:
        def update_book():
             mycursor = mydb.cursor()
             b_id=int(input("Enter book id: "))
             n_title=input("Enter Book Title: ")
             n_author=input("Enter Book Author: ")
             n_publisher=input("Enter Book Publisher: ")
             n_status=input("Enter Book Status: ")
             n_copies=int(input("Enter Book copies: "))
             sql="UPDATE book SET title=%s,author=%s,publisher=%s,b_status=%s,copies=%s WHERE book_id=%s"
             val=(n_title,n_author,n_publisher,n_status,n_copies,b_id)
             mycursor.execute(sql,val)
             mydb.commit()
             print("\nBook details updated successfully")
        update_book()
     if choice==3:
        def del_book():
            mycursor = mydb.cursor()
            id=int(input("Enter book ID: "))
            sql="DELETE FROM book WHERE book_id=%s"
            val=[id]
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nBook details deleted successfully")
        del_book()
     if choice==4:
        def display_book():
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM book")
            result=mycursor.fetchall()
            for res in result:
                print( print(f"{res[0]}\t{res[1]}\t{res[2]}\t{res[3]}\t{res[4]}\t"))

        display_book()
             
    
def book_issue():
    mycursor = mydb.cursor()
    id=int(input("Enter id of student: "))
    b_id=input("Enter book id: ")
    issue_date=datetime.date.today()
    return_date=issue_date + datetime.timedelta(days=14)
    sql="INSERT INTO book_issue(stud_id,book_id,issue_date,return_date) values(%s,%s,%s,%s)"
    val=(id,b_id,issue_date,return_date)
    mycursor.execute(sql,val)
    mydb.commit()
  


def book_return():
    mycursor = mydb.cursor()
    id=int(input("Enter id of student: "))
    b_id=int(input("Enter book id: "))
    mycursor.execute("DELETE FROM book_issue WHERE stud_id=%s,book_id=%s",(id,b_id))
    mydb.commit()
    current_date=current_date.today()
    mycursor.execute("SELECT return_date FROM book_issue WHERE stud_id=%s,book_id=%s",(id,b_id))
    mydb.commit()
    result=mycursor.fetchone()
    return_date=result
    if current_date > return_date:
        penalty=(current_date-return_date).days*fine_per_day
        mycursor.execute("INSERT INTO student(penalty)VALUES(%s)",(penalty))
        mydb.commit()

def book_lost():
    mycursor = mydb.cursor()
    s='lost'
    b_id=int(input("Enter book id: "))
    mycursor.execute("UPDATE book SET b_status=%s WHERE book_id=%s",(s,b_id))
    mydb.commit()
   


if __name__ == "__main__":
    main_menu()

