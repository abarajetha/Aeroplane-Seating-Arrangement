Booked = 0
NoP =int(input("Enter the number of passengers: "))
row = 0
tempBooked = -1


def construct(SeatsArrangement):
    seats = []
    for i in SeatsArrangement:
        rows = i[1]
        cols = i[0]
        # mat = [[-1]*cols]*rows
        mat = []
        for i in range(rows):
            mat.append([-1]*cols)
        seats.append(mat)
    #print(seats)    
    return seats

def printSeats(seats):
    blksize = len(str(NoP))
    rows = [x[1] for x in SeatsArrangement]
    cols = [x[0] for x in SeatsArrangement]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*blksize
                    rowl += ' '*blksize
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*blksize
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(blksize - len(str(k))))
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
           
            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))

               
def fill_aisle_seats():
    # Booked = 0
    global Booked
    row = 0
    tempBooked = -1
    while Booked < NoP and Booked != tempBooked:
        tempBooked = Booked
        for i in range(length):
            if SeatsArrangement[i][1] > row:
                if i == 0 and SeatsArrangement[i][0] > 1:
                    Booked += 1
                    aisleCol = SeatsArrangement[i][0] - 1
                    seats[i][row][aisleCol] = Booked
                    if Booked >= NoP:
                        break
                elif i == length - 1 and SeatsArrangement[i][0] > 1:
                    Booked += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = Booked
                    if Booked >= NoP:
                        break
                else:
                    Booked += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = Booked
                    if Booked >= NoP:
                        break
                    if SeatsArrangement[i][0] > 1:
                        Booked += 1
                        aisleCol = SeatsArrangement[i][0] - 1
                        seats[i][row][aisleCol] = Booked
                        if Booked >= NoP:
                            break
        row += 1


def fill_window_seats():
    row = 0
    global Booked
    global NoP
    tempBooked = 0
    while Booked < NoP and Booked != tempBooked:
        tempBooked = Booked
        if SeatsArrangement[0][1] > row:
            Booked += 1
            window = 0
            seats[0][row][window] = Booked
            if Booked >= NoP:
                break
        if SeatsArrangement[length-1][1] > row:
            Booked += 1
            window = SeatsArrangement[length-1][0] - 1
            seats[length-1][row][window] = Booked
            if Booked >= NoP:
                break
        row += 1

def fill_middle_seats():
    row = 0
    tempBooked = 0
    global Booked
    while Booked < NoP and Booked != tempBooked:
        tempBooked = Booked
        for i in range(length):
            if SeatsArrangement[i][1] > row:
                if SeatsArrangement[i][0] > 2:
                    for col in range(1, SeatsArrangement[i][0] - 1):
                        Booked += 1
                        seats[i][row][col] = Booked
                        if Booked >= NoP:
                            break
        row += 1


SeatsArrangement = [[3,4], [4,5], [2,3], [3,4]]

seats = construct(SeatsArrangement)
# print seats
length = len(SeatsArrangement)


# Aisle
fill_aisle_seats()

# Window

fill_window_seats()

# Center
row = 0
tempBooked = 0
fill_middle_seats()


printSeats(seats)
