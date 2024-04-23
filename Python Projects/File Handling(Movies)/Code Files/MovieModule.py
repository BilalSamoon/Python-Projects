import os

class MovieM:

    #class variable
    S_FILENAME = "CollectibleDB.txt"

    def __init__(self) -> None:
        pass

    def addMovie(self):
        print("addMovie() called")
        try:
            #open a file to save the data
            MovieFile = open(MovieM.S_FILENAME, 'a')

            p_id = int(input("Enter Movie ID : "))
            p_name = input("Enter Movie name : ")
            p_genre = input("Enter Movie Genre : ")

            dataLine = f'{p_id},{p_name},{p_genre}\n'
            MovieFile.write(dataLine)

            print(f'\nSuccessfully saved {p_name} in the file\n')

        except FileNotFoundError as fnf:
            print(f'File not found at mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble writing/reading file : {ioe}')
        except ValueError as ve:
            print(f'please provide correct type of data : {ve}')
        except:
            print("unidentified error occurred")
        else:
        # finally:
            #close the file
            MovieFile.close()
            print("File closed successfully")

    def editMovie(self):

        self.displayMovie()

        try:
            MovieFile = open(MovieM.S_FILENAME, "r")

            tempFile = open("TempDB.txt", "a")


            allMovieLines = MovieFile.readlines()
            if (len(allMovieLines) > 0):
                idToEdit = int(input("Enter Movie ID to edit : "))

                found = False

                for eachMovie in allMovieLines:
                    attributes = eachMovie.split(',')

                    if idToEdit == int(attributes[0]):
                        found = True
                        print('matching Movie found')
                        print(f'{attributes[0]} -- {attributes[1]} -- {attributes[2]}')
                        print("Please enter updated details : ")
                        updatedName = input("Enter Movie name : ")
                        updatedgenre = input("Enter Movie genre : ")

                        updatedDataLine = f'{attributes[0]},{updatedName},{updatedgenre}\n' 

                        tempFile.write(updatedDataLine)
                    else:

                        tempFile.write(eachMovie)

                if not found:
                    print(f'no Movie found for the given id')

            else:
                print(f'There are not Movies in the file yet.')

        except FileNotFoundError as fnf:
            print(f'File not found at mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble writing/reading file : {ioe}')
        except:
            print("unidentified error occurred")
        finally:
            MovieFile.close()
            tempFile.close()


            if os.path.exists(f'{os.getcwd()}/TempDB.txt'):
                os.remove(f'{os.getcwd()}/{MovieM.S_FILENAME}')
                os.rename(f'{os.getcwd()}/TempDB.txt', f'{os.getcwd()}/{MovieM.S_FILENAME}')
            else:
                print("Error occurred while editing the file. No changes made.")



        

    def searchMovie(self):

        nameToSearch = input("\nEnter the Movie name to search : ")

        try:
            MovieFile = open(MovieM.S_FILENAME, "r")
            allMovieLines = MovieFile.readlines()

            if(len(allMovieLines) > 0):
                ifFound = False

                for eachLine in allMovieLines:
                    prodAttributes = eachLine.split(",")

                    if (prodAttributes[1].lower().strip() == nameToSearch.lower().strip()):
                        print("Matching Movie found.")
                        print(f'{prodAttributes[0]} --- ' + 
                              f'{prodAttributes[1]} --- ' + 
                              f'$ {prodAttributes[2]}')
                        ifFound = True

                if not ifFound:
                    print(f'Movie with {nameToSearch} is not found')
            else:
                print("There are no Movies in the file yet.")

        except FileNotFoundError as fnf:
            print(f'File not found at mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble writing/reading file : {ioe}')
        except:
            print("unidentified error occurred")
        else:
            MovieFile.close()

    def deleteMovie(self):

        self.displayMovie()

        try:
            MovieFile = open(MovieM.S_FILENAME, "r")
            #create a temporary file to save any records which are NOT to be deleted
            #use the temporary file to duplicate data to keep
            duplicateFile = open("TempDB.txt", "a")


            allMovieLines = MovieFile.readlines()

            if (len(allMovieLines) > 0):
                idToDelete = int(input("Enter the Movie ID to delete : "))

                ifFound = False

                for eachLine in allMovieLines:
                    prodAttributes = eachLine.split(",")
                    
                    if (int(prodAttributes[0].strip()) == idToDelete):
                        print("Movie to delete found.")
                        print(f'{prodAttributes[0]} --- ' + 
                              f'{prodAttributes[1]} --- ' + 
                              f'$ {prodAttributes[2]}')
                        ifFound = True
                    else:
                        #save the current record in the duplicate file
                        duplicateFile.write(eachLine)

                if not ifFound:
                    print(f'Movie with id {idToDelete} is not found')

            else:
                print("No Movie in the file to delete")

        except FileNotFoundError as fnf:
            print(f'File not found at mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble writing/reading file : {ioe}')
        except:
            print("unidentified error occurred")
        finally:
            MovieFile.close()
            duplicateFile.close()

            #delete the CollectibleDB file

            filePath = f'{os.getcwd()}/{MovieM.S_FILENAME}'
            print(f'filePath : {filePath}')
            os.remove(filePath)

            #rename the TempDB.txt to CollectibleDB.txt
            os.rename(f'{os.getcwd()}/TempDB.txt', filePath)

    def displayMovie(self):

        try:
            MovieFile = open(MovieM.S_FILENAME, "r")
            # r - read only 

            #read all the lines from file
            #readlines() will return the list of individual lines from file
            allMovieLines = MovieFile.readlines()


            if (len(allMovieLines) > 0):
                for eachLine in allMovieLines:

                    prodAttributes = eachLine.split(",") 

                    id = int(prodAttributes[0])
                    name = prodAttributes[1]
                    genre = prodAttributes[2]

                    print(f'---------------------------------')
                    print(f'{id} --- {name} --- {genre} ---')
                    print(f'---------------------------------')
            else:
                print(f'\nThere are no Movies in the file yet.\n')

        except FileNotFoundError as fnf:
            print(f'File not found at mentioned location : {fnf}')
        except IOError as ioe:
            print(f'Trouble writing/reading file : {ioe}')
        except:
            print("unidentified error occurred")
        else:
            MovieFile.close()
            print("File closed successfully")

