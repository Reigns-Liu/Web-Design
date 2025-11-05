class Board:

    def __init__(self):
        """__init_ method"""
        self.x = "-"
        self.y = "|"
        self.z = "  "
        self.zz = ""
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]    

    def Draw(self):
        """Draws the board without square numbers then draws the board with square numbers"""
        print ('The Board looks like this: \n')     
        print ((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print ((self.z * 16), self.x * 17)
        print ((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print ((self.z * 16), self.x * 17)
        print ((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print ((self.z * 16), self.x * 17)
        print ((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print ('\n')
        print ('The Board with the square numbers looks like this: \n')    
        print ((self.z * 16), 1, self.zz, self.y, 2, self.zz, self.y, 3, self.zz, self.y, 4)
        print ((self.z * 16), self.x * 17)
        print ((self.z * 16), 5, self.zz, self.y, 6, self.zz, self.y, 7, self.zz, self.y, 8)
        print ((self.z * 16), self.x * 17)
        print ((self.z * 16), 9, self.zz, self.y, 10, self.y, 11, self.y, 12)
        print ((self.z * 16), self.x * 17)
        print ((self.z * 16), 13, self.y, 14, self.y, 15, self.y, 16)
        print ('\n')

class Mark(Board):
    
    def draw(self, square_number, mark):
        """Draws the borad with current values"""
        self.square_number = square_number - 1     
        self.mark = mark                           
        self.board[self.square_number] = self.mark  
        for i in range(16):     
            try:
                self.board[i] += 1  
                self.board[i] = " " 
            except TypeError:       
                pass
        print ('\n')
        print ((self.z * 16), self.board[0], self.y, self.board[1], self.y, self.board[2], self.y, self.board[3]) 
        print ((self.z * 16), self.x * 14)
        print ((self.z * 16), self.board[4], self.y, self.board[5], self.y, self.board[6], self.y, self.board[7])
        print ((self.z * 16), self.x * 14)
        print ((self.z * 16), self.board[8], self.y, self.board[9], self.y, self.board[10], self.y, self.board[11])
        print ((self.z * 16), self.x * 14)
        print ((self.z * 16), self.board[12], self.y, self.board[13], self.y, self.board[14], self.y, self.board[15]) 
        print ('\n')

class Play(Mark):

    def select_square(self):
        """Starts the game with square selection"""
        self.switch = True     
        self.turn = ["X", "O"] 
        self.counter = 0        
        while self.switch == True:  
            for move in range(2):   
                self.move = move
                self.get_input(self.turn, self.move)    
                if self.switch == False:       
                    break                       
                else:
                    self.counter += 1      
                if self.counter == 16:       
                    print ("The game is a Tie - no winner.\n")  
                    self.switch = False     
                    break                   
                else:
                    continue                

    def get_input(self, turn, move):
        """Gets input from user"""
        self.turn = turn
        self.move = move
        try:
            sn = int(input(self.turn[self.move] + " Enter a square number (1-16) for your move: ")) 
            if self.check_input(sn) == True:                   
                self.draw(sn, self.turn[move])                  
                if self.check_win(self.turn, move) == True:     
                    self.print_win(self.turn, move)            
                else:
                    pass
            else:
                pass
        except ValueError:
            print ("\nError: Please enter a number between 1-16\n")     
            self.Draw()                                                 
            self.get_input(self.turn, self.move)                        

    def check_input(self, square_number):
        """Checks the input for errors"""
        self.square_number = square_number
        if((self.square_number >= 1) and (self.square_number <= 16)):   
            if ((self.board[self.square_number - 1]) == "X") \
                or ((self.board[self.square_number - 1]) == "O"):       
                print ("\nError: That space is already taken, please choose an open space.\n") 
                self.get_input(self.turn, self.move)               
            else:       
                return True     
        else:
            print ("\nError: That is not a valid square number, please enter a value between 1-16\n")    
            self.Draw()                                             
            self.get_input(self.turn, self.move)                    

    def check_win(self, turn, move):
        """Checks the ten possibilites for a win"""
        if (self.board[0] == self.turn[move] and self.board[1] == self.turn[move] \
              and self.board[2] == self.turn[move] and self.board[3] == self.turn[move]):
            return True
        elif (self.board[4] == self.turn[move] and self.board[5] == self.turn[move] \
              and self.board[6] == self.turn[move] and self.board[7] == self.turn[move]):
            return True
        elif (self.board[8] == self.turn[move] and self.board[9] == self.turn[move] \
              and self.board[10] == self.turn[move] and self.board[11] == self.turn[move]):
            return True
        elif (self.board[12] == self.turn[move] and self.board[13] == self.turn[move] \
              and self.board[14] == self.turn[move] and self.board[15] == self.turn[move]):
            return True
        elif (self.board[0] == self.turn[move] and self.board[4] == self.turn[move] \
              and self.board[8] == self.turn[move] and self.board[12] == self.turn[move]):
            return True
        elif (self.board[1] == self.turn[move] and self.board[5] == self.turn[move] \
              and self.board[9] == self.turn[move] and self.board[13] == self.turn[move]):
            return True
        elif (self.board[2] == self.turn[move] and self.board[6] == self.turn[move] \
              and self.board[10] == self.turn[move] and self.board[14] == self.turn[move]):
            return True
        elif (self.board[3] == self.turn[move] and self.board[7] == self.turn[move] \
              and self.board[11] == self.turn[move] and self.board[15] == self.turn[move]):
            return True
        elif (self.board[0] == self.turn[move] and self.board[5] == self.turn[move] \
              and self.board[10] == self.turn[move] and self.board[15] == self.turn[move]):
            return True
        elif (self.board[3] == self.turn[move] and self.board[6] == self.turn[move] \
              and self.board[9] == self.turn[move] and self.board[12] == self.turn[move]):
            return True
        else:
            return False

    def print_win(self, turn, move):
        """Prints the winning message"""
        print (str(turn[move]) + " Wins ! \n")  
        self.switch = False                     
        return self.switch                     

b1 = Play() 
b1.select_square() 