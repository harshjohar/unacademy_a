for _ in range(int(input())):
    n = int(input())
    database = {} # roll no. vs no. of hrs
    students = 0
    dates = {}
    for i in range(n):
        name= input()
        time = int(input())
        date = input()
        dates.add(date)
        action = input() # Entry or Exit
        roll_no = int(input())


        if roll_no in database:
            pass

        else:
            database[roll_no] = 0
        if action == 'Entry':
            database[roll_no][i][]



    
