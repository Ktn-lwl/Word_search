"""
r and c refer to rows and columns respectively throughout code. Matrix coordinates
start from (1, 1) and go up to whatever you want (depending on computational
limitations of course).
"""

class Grid:
    def __init__(self, dimensions): 
        self.dimensions = dimensions
        self.body = [list("0"*dimensions) for i in range(dimensions)]
        """
        Makes a 2D (dimensions x dimensions) matrix full of 0s
        """

    def showgrid(self):
        for i in self.body:
            print("  ".join(i))
        """
        Displays the grid in its current state (prettified by using whitespace
        then removing square braces, quotes and commas from the matrix).
        """

    def update(self, coords, new):
        self.body[coords[0]-1][coords[1]-1] = new 
        """
        Update the item at the given coordinates in the matrix. Coordinates must 
        be a tuple/list of the form (r,c).
        """

    def mass_update(self, data):
        for i in data:
            self.update(i[0],i[1])   
        """
        Update several coordinates in the matrix at once. Takes a list of the 
        form: [((r1,c1), data1), ..., ((rN,cN), dataN)] as the 'data' 
        argument.
        """

    def wipe(self):
        self.body = [list("0"*self.dimensions) for i in range(self.dimensions)]
        """
        Initializes the matrix (keeps dimensions, but fills it with 0s).
        """

    def return_row(self, n, reversed=False):
        if not reversed:
            return self.body[n-1]
        else:
            return self.body[n-1][::-1]
        """
        returns the nth row of the matrix as a list where n is a positive integer.
        The 'reversed' argument indicates that the output should be returned in
        reverse order 
        """

    def return_column(self, n, reversed=False):
        if not reversed:
            return [i[n-1] for i in self.body]
        else:
            return [i[n-1] for i in self.body][::-1]
        """
        returns the nth column of the matrix as a list where n is a positive integer.
        The 'reversed' argument indicates that the output should be returned in
        reverse order 
        """ 
        
    def return_diagonal(self, n, reversed=False):
        if not reversed: 
            if n >= 0:
                return [self.body[i][i+n] for i in range(self.dimensions-n)]
            elif n < 0:
                return [self.body[abs(n)+i][i] for i in range(self.dimensions-abs(n))]
            
        else:
            if n >= 0:
                return [self.body[i][i+n] for i in range(self.dimensions-n)][::-1]
            elif n < 0:
                return [self.body[abs(n)+i][i] for i in range(self.dimensions-abs(n))][::-1]
        """
        returns the nth diagonal of the matrix as a list, where n is an integer
        indicative of whether the requested diagonal is the main diagonal, a
        superdiagonal, or a subdiagonal. The 'reversed' argument indicates that
        the output should be returned in reverse order. 
        """

    def return_skewdiagonal(self, n, reversed=False):
        dim = self.dimensions
        if not reversed:
            if n >= 0:
                return [self.body[dim-n-i-1][i] for i in range(dim-n)]
            elif n < 0:
                return [self.body[dim-i-1][i+abs(n)] for i in range(dim-abs(n))]
        
        else:
            if n >= 0:
                return [self.body[dim-n-i-1][i] for i in range(dim-n)][::-1]
            elif n < 0:
                return [self.body[dim-i-1][i+abs(n)] for i in range(dim-abs(n))][::-1]
        """
        returns the nth skew diagonal of the matrix as a list, where n is an integer
        indicative of whether the requested diagonal is the main skew diagonal, 
        a super-skew-diagonal, or a sub-skew-diagonal. The 'reversed' argument 
        indicates that the output should be returned in reverse order.
        (I kinda pulled the terms super-skew, and sub-skew-diagonal out of my ass,
        but cut me some slack okay? Idk what to call them and those seem fitting.) 
        """

    def vector(self, coords, di):
        dim = self.dimensions
        (r,c) = coords
        n = (int(di%4==1)*(dim+1-(c+r))+
             int(di%4==3)*(c-r))
        directions = {1:[Grid.return_skewdiagonal, (int(n>=0)*(c-1))+(int(n<0)*abs(r-dim))],
                      2:[Grid.return_row,(c-1)],
                      3:[Grid.return_diagonal, (int(n>=0)*(r-1))+(int(n<0)*(c-1))],
                      0:[Grid.return_column, (r-1)]}
        
        x = (n*int(di%2==1)+
             r*int(di%4==2)+
             c*int(di%4==0))

        y1 = int(di<5)*directions[di%4][1]
        y2 = int(di>4)*directions[di%4][1]+int(di>4)+int(di<5)*len(directions[di%4][0](self,x))

        z = int(di<5)-int(di>=5)

        return directions[di%4][0](self, x)[y1:y2][::z]
    
        """
        Return the item at the given coordinates plus all the consecutive items in a 
        specified direction, 'di', in the matrix. The direction is to be specified using an
        integer between 1 and 8 inclusive, with 8 indicating North, 1 indicating 
        Northeast, and so on (kinda like you would arrange the numbers on a clock 
        face, except with 8 numbers, not 12).
        """

"""
Disregard these last few lines, I just use them to dynamically testing my methods as I
write em (I'm kinda lazy and don't wanna write actual test cases).
"""

a = Grid(6)
updata = [((1,2), "A"), ((2,6), "B"), ((3,4), "E"), ((3,1), "M"),
          ((5,5), "S"), ((6,3), "W"),((1,1), "X")]
Grid.mass_update(a, updata)#recently discovered implicit calls, and I think they're pretty neat :)
a.showgrid()
for i in range(1,9):
    print(a.vector((3,5), i))
