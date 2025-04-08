class ClassName():
    def __init__(self,f_name=None):
        if f_name is None:
            f_name = input('Enter your porject name: ')
        self.f_name = f_name
        self.data = []
        self.load()
        self.noc = len(self.col_names)
        self.update_len()

    def __get_user_column(self):
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
                self.noc = len(self.col_names)

                for line in lines[1:]:
                    if line:
                        row = line.strip().split(',')
                        row = self.__scanner(row)
                        self.data.append(row)
            print("Data is loaded from file.csv")
    
        except:
            print("There is no previous data")
            self.__get_user_column()

    def update_len(self):
        self.max_len = list(map(len,self.col_names))
        for row in self.data:
            for i,cell in enumerate(row):
                self.max_len[i] = max(self.max_len[i],len(str(cell)))

    def __scanner(self,row):
        for j in range(len(row)):
            if row[j].isnumeric():
                row[j] = int(row[j])
            elif row[j].replace('.','',1).isnumeric():
                row[j] = float(row[j])
        return row
            
    def save(self):
        """
        save to file
        """
        with open(f'{self.f_name}.csv','w') as f:
            f.write(','.join(self.col_names)+'\n')
            for row in self.data:
                f.write(','.join(map(str,row))+'\n')
        #print('File is saved')
    
    def __get_col_no(self):
        for i,col in enumerate(self.col_names,1):
            print(f"{i}. {col}")
        col_no = int(input("Enter column number to search: ")) -1
        return col_no

    def show(self,rows): # show table format
        def formator(row,no=None):
            if no is None:
                no = 'No'
            #print(self.noc,self.max_len)
            return f"|{no:>3}|" + "|".join(map(lambda i:f"{row[i]:>{self.max_len[i]+1}}",range(self.noc))) + "|"
        title = formator(self.col_names)
        print("-"*len(title))
        print(title)
        print("-"*len(title))
        if rows:
            for i,row in enumerate(rows,1):
                print(formator(row,no=i))
        else:
            message = f"There is no {self.f_name}"
            print(f"{message:^{len(title)}}")
        print("-"*len(title))
    """
    def show(self,rows):
        for n,row in enumerate(rows,1):
            print(n,end=' ')
            for i,cell in enumerate(row):
                print(f"{self.col_names[i]}: {cell} ",end="")
            print()
    """
    def display_total_number(self,data = None):
        print(f"Total number of {self.f_name} is ",end='')
        print(0) if self.data == None else print(len(data))

    
    def add(self):
        """
        add new data
        """
        row = []
        for i,col_name in enumerate(self.col_names):
            col_value = input(f"Enter {col_name}: ")
            self.max_len[i] = max(self.max_len[i],len(col_value))
            row.append(col_value)
        row = self.__scanner(row)
        self.data.append(row)
        self.update_len()
        print('New Row is Added')

    
    def search(self):
        """
        search function
        """
        col_no = self.__get_col_no()
        condition = '1'
        isnum = False
        
        if type(self.data[0][col_no]) == int or type(self.data[0][col_no]) == float:
            condition = input("1. Equal to\n2. Greater than\n3. Less than\nEnter a number: ")
            isnum = True

        search_value = input("Enter the value to search: ")
        if isnum:
            search_value = float(search_value)
        result = []

        for row in self.data:

            if condition == '1':
                if isnum:
                    if row[col_no] == search_value:
                        result.append(row)
                else:
                    if row[col_no].lower() == search_value.lower():
                        result.append(row)
            elif condition == '2':
                if row[col_no] > search_value:
                    result.append(row)
            elif condition == '3':
                if row[col_no] < search_value:
                    result.append(row)
        self.show(result)
        self.display_total_number(result)

    def sort(self,):
        col_no = self.__get_col_no()
        s_data = sorted(self.data,key=lambda row:row[col_no])
        self.show(s_data)

    def delete(self):
        """
        delete data
        """
        self.show(self.data)
        row_no = int(input("Enter row number to delete: "))-1
        self.show([self.data[row_no]])
        comfirm = input("Are you sure (y/n): ")
        if comfirm == 'Y' or comfirm == 'y':
            _ = self.data.pop(row_no)
            print("Delete successfully")
            self.update_len()
            return
        print("Not Delete")

    def update(self):
        """
        update data
        """
        self.show(self.data)
        row_no = int(input("Enter row no to update: ")) -1
        col_no = self.__get_col_no()
        value = input("Enter value to update: ")

        self.data[row_no][col_no] = value
        self.update_len()
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
                self.show(self.data)
            elif user_input == '2':
                self.display_total_number(self.data)
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

