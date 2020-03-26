def primePrinter():
    end = int(input("What number do you wwant to go up to?\n>>>"))
    for i in range(end):
        if i > 1: 
           for j in range(2, i): 
               if (i % j) == 0: 
                   break
           else: 
               print(i)

primePrinter()
