i=0
Board=[["_","_","_"],
       ["_","_","_"],
       ["_","_","_"]]
def check(board,a):
    #checking the row sides if they are won
    for row in range(3):
        if (board[row][0] == "X" and board[row][1]== "X" and board[row][2] == "X" )or (board[row][0] == "O" and board[row][1] == "O" and board[row][2] == "O"):
            print(f"{a} won at {row} row")
            exit()
    #checking for column sides if they are won
    for col in range(3):
        if (board[0][col] == "X" and board[2][col] == "X" and board[2][col] == "X") or  (board[0][col] == "O" and board[2][col] == "O" and board[2][col] == "O"):
            print(f'{a} won at {col} column')
            exit()
    #Checking for diagnols
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        print(f'{a} won at left diagnol')
        exit()
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        print(f'{a} won at right diagnol')
        exit()

while(i<9):
    for x in range(3):
        print(Board[x])
    if i%2==0:
        a='X'
    else:
        a='O'
    try :
        x=int(input(f"Enter X- plane coordinates of place to put {a}  :"))
        y=int(input(f"Enter Y- plane coordinates of place to put {a}  :"))
        if Board[x][y]=='X' or Board[x][y]=='O':
            print("Already Played at this position")
            continue
        Board[x][y]=a
    except IndexError:
        print("Both Co-ordinated must be below 3")
        continue
    except ValueError:
        print("Enter Proper Values")
        continue
    check(Board,a)   
    i+=1
