class ClassName():
    def __init__(self):
        self.data = load()

    def load(self):
        """
        load data form csv file
        """
        pass

    def save(self):
        """
        save to file
        """  

    def displsy_all(self):
        """
        display all entry form data
        """
        pass

    def display_total_number(self):
        """
        display total number of entry
        """
        pass

    def add(self):
        """
        add new data
        """
        pass

    def search(self):
        """
        search function
        """
        pass

    def delete(self):
        """
        delete data
        """
        pass

    def update(self):
        """
        update data
        """
        pass

if __name__ == '__main__':
    myclass = ClassName()

    while True:
        print("1. Display All")
        print("2. Display Total Number")
        print("3. Add")
        print("4. Search")
        print("5. Delete")
        print("6. Update")
        print("7. Exit")
        user_input = input("Enter a number: ")
        if user_input == '1':
            myclass.display_all()
        elif user_input == '2':
            myclass.display_total_number()
        elif user_input == '3':
            myclass.add()
        elif user_input == '4':
            myclass.search()
        elif user_input == '5':
            myclass.delete()
        elif user_input == '6':
            myclass.update()
        elif user_input == '7':
            myclass.save()
            break

