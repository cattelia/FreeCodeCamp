def numbers():
    
    for i in range(1, 101):
        case = {'Go': i%4 == 0, 'Figure': i%5==0, 'Go Figure': i%4==0 and i%5==0}
        print(case.get(i))
    
#numbers()

def numbers():
    
    for i in range(1, 101):
        response = 'Go Figure' if i % 4 == 0 and i % 5 == 0 else 'Go' if i % 4 == 0 else 'Figure' if i % 5 == 0 else False
        if response == False:
            continue
        else:
            print(response)


numbers() 
    

#python

def countDown():
  for i in range(100, -1, -2):
    print(i)

countDown()