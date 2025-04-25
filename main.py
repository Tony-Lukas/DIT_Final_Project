import os

class ClassName():
    def __init__(self,f_name=None,table=None):
        if f_name is None:
            f_name = input('Enter your porject name: ')
        if table is None:
            t = input('Show Table Format? (y/n) ')
            table = True if t == 'y' else False

        self.f_name = f_name
        self.data = []
        self.load()
        if table:
            self.show = self.show_table
        else:
            self.show = self.show_dic


    def __get_user_column(self):
        N = int(input("Enter number of columns: "))
        col_names = []
        for i in range(N):
            col = input(f"Enter name of column {i+1}: ")
            self.col_names.append(col)

    def load(self):
        try:
            with open(self.f_name+'.csv','r') as f:
                lines = f.readlines()
                self.col_names = lines[0].strip().split(',')

                for line in lines[1:]:
                    if line:
                        row = line.strip().split(',')
                        row = self.__scanner(row)
                        self.data.append(row)
            print("Data is loaded from file.csv")
    
        except:
            print("There is no previous data")
            self.__get_user_column()
    
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

    def show_table(self,rows,col_names=None): # show table format
        if col_names is None :
            col_names = self.col_names

        def formator(row,no=None):
            if no is None:
                no = 'No'
            return f"|{no:>3}|" + "|".join(map(lambda i:f"{row[i]:>{max_len[i]+1}}",range(noc))) + "|"
        
        max_len = list(map(len,col_names))
        noc = len(col_names)
        for row in rows:
            for i,cell in enumerate(row):
                max_len[i] = max(max_len[i],len(str(cell)))
        
        title = formator(col_names)
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
    
    def show_dic(self,rows,col_names=None):
        if col_names == None:
            col_names = self.col_names
        print()
        for n,row in enumerate(rows,1):
            print(n,end='. ')                
            for i,cell in enumerate(row):
                print(f"{col_names[i]}: {cell} ",end="")
            print()
        print()

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
            row.append(col_value)
        row = self.__scanner(row)
        self.data.append(row)
        print(f'New {self.f_name} is Added')

    
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
                    if row[col_no].lower().startswith(search_value.lower()):
                        result.append(row)
            elif condition == '2':
                if row[col_no] > search_value:
                    result.append(row)
            elif condition == '3':
                if row[col_no] < search_value:
                    result.append(row)
        self.show(result)
        self.display_total_number(result)

    def sort(self):
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
        print("Update Successfully")
    def developer_info(self): 
        col_names = ['Name','NickName','StudentID']
        rows = [['Phone Pyae Kyaw','Mr. Ligma','6709453'],
                ['Tin Maung Maung Htwe','Tide','6709755'],
                ['Thiha Nyein','Luka','6709515']]
        self.show(rows,col_names)

    def key_feature(self):
        features = ["Content Independent",
                    "Search can be different depend on numerical and categorical value",
                    "Show function with two style",
                    "Use functional Programming( join , map, lambda)"]
        for f in features:
            print(f)
            _ = input()
    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1. Display All")
            print("2. Display Total Number")
            print("3. Add")
            print("4. Search")
            print("5. Delete")
            print("6. Update")
            print("7. Sort")
            print("8. Developer Info")
            print("9. Key Features")
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
            elif user_input == '8':
                self.developer_info()
            elif user_input == '9':
                self.key_feature()
            elif user_input == '0':
                user_input = input(f"Save {self.f_name}.csv? (yes/no/cancle)")
                if user_input == 'yes' or user_input == 'y':
                    self.save()
                    break
                elif user_input == 'no' or user_input == 'n':
                    break
                else:
                    continue
    
if __name__ == '__main__':
    myclass = ClassName()
    myclass.run()
