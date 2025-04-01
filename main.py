class ClassName():
    def __init__(self):
        self.col_names , self.data = self.load()
    
    def get_user_column(self):
        N = int(input("Enter number of columns: "))
        col_names = []
        for i in range(N):
            col = input(f"Enter name of column {i+1}: ")
            col_names.append(col)
        return col_names

    def load(self):
        """
        load data form csv file
        """
        try:
            f = open('file.csv','r')
            lines = f.readlines()
            col_names = lines[0].strip().split(',')
            rows = []
            for line in lines[1:]:
                line = line.strip()
                if line:
                    row = line.split(',')
                    rows.append(row)
            f.close()
            print("Data is loaded from file.csv")
            return col_names, rows
        except:
            print("There is no previous data")
            return self.get_user_column() , []

    def save(self):
        """
        save to file
        """
        with open('file.csv','w') as f:
            f.write(','.join(self.col_names)+'\n')
            for row in self.data:
                f.write(','.join(row)+'\n')
        print('File is saved')
    
    def get_col_no(self):
        for i,col in enumerate(self.col_names,1):
            print(i,col)
        col_no = int(input("Enter column number to search: ")) -1
        return col_no

    def show(self,rows):
        for n,row in enumerate(rows,1):
            print(n,end=' ')
            for i,cell in enumerate(row):
                print(f"{self.col_names[i]}: {cell} ",end="")
            print()

    def display_all(self):
        """
        display all entry form data
        """
        if self.data:
            self.show(self.data)
        else:
            print("There is no data")

    def display_total_number(self,data = None):
        if data == None:
            print("Total number of rows is",len(self.data))
        else:
            print("Total number of rows is",len(data))
    
    def add(self):
        """
        add new data
        """
        row = []
        for col_name in self.col_names:
            col_value = input(f"Enter {col_name}: ")
            row.append(col_value)
        self.data.append(row)
        print('New Row is Added')

    
    def search(self):
        """
        search function
        """
        col_no = self.get_col_no()
        search_value = input("Enter the value to search: ")
        result = []
        for row in self.data:
            if row[col_no] == search_value:
                result.append(row)
        self.show(result)
        self.display_total_number(result)


    def delete(self):
        """
        delete data
        """
        self.display_all()
        row_no = int(input("Enter row number to delete: "))-1
        self.show([self.data[row_no]])
        comfirm = input("Are you sure (y/n): ")
        if comfirm == 'Y' or comfirm == 'y':
            _ = self.data.pop(row_no)
            print("Delete successfully")
            return 
        print("Not Delete")

    def update(self):
        """
        update data
        """
        self.display_all()
        row_no = int(input("Enter row no to update: ")) -1
        col_no = self.get_col_no()
        value = input("Enter value to update: ")

        self.data[row_no][col_no] = value
        print("Update Successfully")

if __name__ == '__main__':
    myclass = ClassName()

    while True:
        print("-"*25)
        print("1. Display all dinosaurs")
        print("2. Display total Number of dinosaurs")
        print("3. Add dinosaur")
        print("4. Search dinosaur")
        print("5. Delete dinosaur")
        print("6. Update dinosaur")
        print("7. Exit")
        user_input = input("Enter a number: ")
        print()
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

#hello just testing

    
