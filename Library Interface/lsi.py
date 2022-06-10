"""--- Gerekli modüller yüklendi ---"""

from tkinter import * 
import sqlite3 as s1
from tkinter import messagebox

"""--- Veritabanı oluşturuldu ve bağlantısı yapıldı. Veritabanı aracı olarak sqlite kullanıldı ---"""

libraryDB = s1.connect("libraryDatabase.db")
cursor = libraryDB.cursor()

"""--- Kitaplar için tablo oluşturuldu. Proje başlangıcı için tek tablo kullanılacaktır. Duruma göre ilişkili tablo sayısı artabilir ---"""

cursor.execute("CREATE TABLE IF NOT EXISTS Books (book_id INTEGER PRIMARY KEY ,book_name TEXT,book_genre TEXT,author_name TEXT)")

"""--- Kayıt ekleme ekranı için fonksiyon yazıldı  ---"""

def appendSection():
    appendPage = Tk()
    appendPage.title("Library Append Interface")
    appendPage.geometry("400x200")
    
    def appendControl():
        bookName = bookNameEntry.get()
        bookGenre = bookGenreEntry.get()
        authorName = authorNameEntry.get()
        cursor.execute("SELECT COUNT(*) FROM Books WHERE book_name = '"+bookName+"'")
        result = cursor.fetchone()
        
        if int(result[0])>0:
            messagebox.showwarning("Warning", "This record already exists.")
        
        else:
            cursor.execute("INSERT INTO Books(book_name,book_genre,author_name) VALUES(?,?,?)",(bookName,bookGenre,authorName))
            libraryDB.commit()
            libraryDB.close()
            messagebox.showinfo("Success", "Adding process was successful!")
        
    headerTitle = Label(appendPage,text="Adding Section",font=("Verdana",10,"bold"))
    headerTitle.grid(row=0,column=0)
    
    bookNameLabel = Label(appendPage,text="Book Name:")
    bookNameLabel.grid(row=1,column=0)
    
    bookGenreLabel = Label(appendPage,text="Book Genre:")
    bookGenreLabel.grid(row=2,column=0)
    
    authorNameLabel = Label(appendPage,text="Author Name:")
    authorNameLabel.grid(row=3,column=0)
    
    bookNameEntry= Entry(appendPage,width=20)
    bookNameEntry.grid(row=1,column=1)
    
    bookGenreEntry= Entry(appendPage,width=20)
    bookGenreEntry.grid(row=2,column=1)
    
    authorNameEntry = Entry(appendPage,width=20)
    authorNameEntry.grid(row=3,column=1)
    
    appendButton = Button(appendPage,text="Add",font=("Verdana",12),command=appendControl)
    appendButton.grid(row=4,column=0,pady=5,columnspan=5,rowspan=5,padx=10)
    
    appendPage.mainloop()
    
"""--- Kayıt silme arayüzü için fonksiyon yazıldı ---"""

def popSection():
    popPage=Tk()
    popPage.title("Library Delete Interface")
    popPage.geometry("400x200")
    
    def popControl():
        idNumber = idEntry.get()
        cursor.execute("SELECT COUNT(*) FROM Books WHERE book_id =?",idNumber)
        result = cursor.fetchone()
        print(result)
        
        if int(result[0])>0:
            cursor.execute("DELETE FROM Books WHERE book_id =?",idNumber)
            libraryDB.commit()
            libraryDB.close()
            messagebox.showinfo("Success","Deleting process was successful!")
        
        else:
            messagebox.showwarning("Warning","Record can't be found.")
    
    headerTitle = Label(popPage,text="Deleting Section",font=("Verdana",10,"bold"))
    headerTitle.grid(row=0,column=0)
    
    idLabel= Label(popPage,text="Book ID:")
    idLabel.grid(row=1,column=0)
    
    idEntry = Entry(popPage,width=20)
    idEntry.grid(row=1,column=1)
    
    deleteButton = Button(popPage,text="Delete",font=("Verdana",12),command=popControl)
    deleteButton.grid(row=2,column=0,pady=5,columnspan=5,rowspan=5,padx=10)
    
    popPage.mainloop()
    
"""--- Kayıt güncelleme arayüzü için fonksiyon yazıldı ---"""

def updateSection():
    updatePage = Tk()
    updatePage.title("Library Update Interface")
    updatePage.geometry("400x200")
    
    def updateControl():
        idNumber = idEntry.get()
        bookName = bookNameEntry.get()
        bookGenre = bookGenreEntry.get()
        authorName = authorNameEntry.get()
        
        cursor.execute("SELECT COUNT(*) FROM Books WHERE book_id = ?",idNumber)
        result = cursor.fetchone()
        print(result)
        
        if int(result[0])>0:
            cursor.execute("UPDATE Books SET book_name = ? , book_genre = ? , author_name = ? WHERE book_id = ?",(bookName,bookGenre,authorName,idNumber))
            libraryDB.commit()
            libraryDB.close()
            messagebox.showinfo("Success","Updating process was successful!")
            
        else:
            messagebox.showwarning("Warning","Record can't be found.")
            
    headerTitle = Label(updatePage,text="Updating Section",font=("Verdana",10,"bold"))
    headerTitle.grid(row=0,column=0,columnspan=3)
    
    idLabel= Label(updatePage,text="ID Number")
    idLabel.grid(row=1,column=0)
    
    idEntry = Entry(updatePage,width=20)
    idEntry.grid(row=1,column=1)
    
    bookNameLabel = Label(updatePage,text="Book Name:")
    bookNameLabel.grid(row=2,column=0)
    
    bookGenreLabel = Label(updatePage,text="Book Genre:")
    bookGenreLabel.grid(row=3,column=0)
    
    authorNameLabel = Label(updatePage,text="Author Name:")
    authorNameLabel.grid(row=4,column=0)
    
    bookNameEntry= Entry(updatePage,width=20)
    bookNameEntry.grid(row=2,column=1)
    
    bookGenreEntry= Entry(updatePage,width=20)
    bookGenreEntry.grid(row=3,column=1)
    
    authorNameEntry = Entry(updatePage,width=20)
    authorNameEntry.grid(row=4,column=1,sticky=W)
    
    updateButton = Button(updatePage,text="Update",font=("Verdana",12),command=updateControl)
    updateButton.grid(row=5,column=0,pady=30,columnspan=5)
    
    updatePage.mainloop()
    
"""--- Ana arayüz oluşturuldu ---"""

root = Tk()
root.title("Library System Interface")
root.geometry("400x200")

headerTitle=Label(root,text="Welcome to LSI",font=("Ariel",10,"bold"))
headerTitle.grid(row=0,column=0,pady=20,columnspan=5)

appendRowButton = Button(root,text="Add a record",command=appendSection)
appendRowButton.grid(row=1,column=0,pady=10,sticky=W,padx=20)

popRowButton = Button(root,text="Delete a record",command=popSection)
popRowButton.grid(row=1,column=1,padx=20,sticky=W)

updateRowButton = Button(root,text="Update a record",command=updateSection)
updateRowButton.grid(row=1,column=2,padx=20,sticky=E)

root.mainloop()