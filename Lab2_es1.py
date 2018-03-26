print("1 for inserting task ")
print("2 for removing task ")
print("3 for showing all tasks ")
print("4 end programm ")

choice = int(input())
todo=[]
i=0

while choice!=4 :
    if choice == 1 :
        print("put a task: ")
        task[i]=input()
        todo.append(task)
        i=i+1
    elif

    if choice==2:
        print("remove what?: type it")
        delete = input()
        task.remove(delete)
        print("remove success")

    else :
        print("choose a number between 1 and 4")
    print("1 for inserting task ")
    print("2 for removing task ")
    print("3 for showing all tasks ")
    print("4 end programm ")
    choice=int(input())