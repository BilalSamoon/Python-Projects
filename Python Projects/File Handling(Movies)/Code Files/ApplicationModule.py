"""
ApplicationModule.py1
File Handling
"""
from MovieModule import MovieM

class Application:
    def __init__(self):
        self.jack = MovieM()

    def run(self):
        choice = 0
        while choice != 6:
            print("*-*"*10)
            print(" 1 : Add Movie")
            print(" 2 : Edit Movie")
            print(" 3 : Search Movie")
            print(" 4 : Delete Movie")
            print(" 5 : Display Movie List")
            print(" 6 : Exit")
            print("*-*"*10)
            choice = int(input("Enter your choice : "))
            self.doMenuOperations(choice)

    def doMenuOperations(self, operation):
        if operation == 1:
           self.addMovie()
        elif operation == 2:
            self.editMovie()
        elif operation == 3:
            self.searchMovie()
        elif operation == 4:
            self.deleteMovie()
        elif operation == 5:
            self.displayMovies()
        elif operation == 6:
            print("Terminating program")

    def addMovie(self):
        #TO-DO for adding a new Movie to file
        self.jack.addMovie()

    def editMovie(self):
        #TO-DO for updating Movie details in file
        self.jack.editMovie()

    def searchMovie(self):
        #TO-DO for searching Movie by name from file
        self.jack.searchMovie()

    def deleteMovie(self):
        #TO-DO for deleting a Movie from file
        self.jack.deleteMovie()

    def displayMovies(self):
        #TO-DO for displaying all Movie details from file
        self.jack.displayMovie()

#create an object of Application class
app = Application()
app.run()


    

