class ClassName():
    def __init__(self,f_name=None):
        if f_name is None:
            f_name = input('Enter your porject name: ')
        self.f_name = f_name
        self.col_names = []
        self.max_len = []
        self.noc = 0
        self.data = []
        self.load()
        self.scanner()

    def get_user_column(self):
        N = int(input("Enter number of columns: "))
        col_names = []
        for i in range(N):
            col = input(f"Enter name of column {i+1}: ")
            self.col_names.append(col)
            self.max_len.append(len(col))

    def load(self):
        try:
            with open(self.f_name+'.csv','r') as f:
                lines = f.readlines()
                self.col_names = lines[0].strip().split(',')

                for line in lines[1:]:
                    if line:
                        row = line.strip().split(',')
                        self.data.append(row)
            #print("Data is loaded from file.csv")
    
        except:
            #print("There is no previous data")
            self.get_user_column()

    def scanner(self):
        self.noc = len(self.col_names)
        self.max_len = list(map(len,self.col_names))

        for i,row in enumerate(self.data):
            for j in range(self.noc):
                self.max_len[j] = max(self.max_len[j],len(row[j]))
                if row[j].isnumeric():
                    self.data[i][j] = int(row[j])
                elif row[j].replace('.','').isnumeric():
                    self.data[i][j] = float(row[j])
                
    def save(self):
        """
        save to file
        """
        with open(f'{self.f_name}.csv','w') as f:
            f.write(','.join(self.col_names)+'\n')
            for row in self.data:
                f.write(','.join(map(str,row))+'\n')
        #print('File is saved')
    
    def get_col_no(self):
        for i,col in enumerate(self.col_names,1):
            print(f"{i}. {col}")
        col_no = int(input("Enter column number to search: ")) -1
        return col_no

    def show(self,rows): # show table format
        def formator(row,no=None):
            if no is None:
                no = 'No'
            return f"|{no:>3}|" + "|".join(map(lambda i:f"{row[i]:>{self.max_len[i]+1}}",range(self.noc))) + "|"
        title = formator(self.col_names)
        print("-"*len(title))
        print(title)
        print("-"*len(title))
        for i,row in enumerate(rows,1):
            print(formator(row,no=i))
        print("-"*len(title))
    """
    def show(self,rows):
        for n,row in enumerate(rows,1):
            print(n,end=' ')
            for i,cell in enumerate(row):
                print(f"{self.col_names[i]}: {cell} ",end="")
            print()
    """
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
            print(f"Total number of {self.f_name} is {len(self.data)}")
        else:
            print(f"Total number of {self.f_name} is {len(data)}")
    
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
            if row[col_no].lower() == search_value.lower():
                result.append(row)
        self.show(result)
        self.display_total_number(result)

    def sort(self):
        col_no = self.get_col_no()
        s_data = sorted(self.data,key=lambda row:row[col_no])
        self.show(s_data)

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
    
    def run(self):
        while True:
            print("1. Display All")
            print("2. Display Total Number")
            print("3. Add")
            print("4. Search")
            print("5. Delete")
            print("6. Update")
            print("7. Sort")
            print("0. Exit")
            user_input = input("Enter a number: ")
            print()
            if user_input == '1':
                self.display_all()
            elif user_input == '2':
                self.display_total_number()
            elif user_input == '3':
                self.add()
            elif user_input == '4':
                self.search()
            elif user_input == '5':
                self.delete()
            elif user_input == '6':
                self.update()
            elif user_input == '7':
                self.sort()
            elif user_input == '0':
                self.save()
                break
    
if __name__ == '__main__':
    myclass = ClassName()
    myclass.run()

