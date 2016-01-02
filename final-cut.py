#instance importing previously created media class
import media
from media import Movie
import fresh_tomatoes
#from fresh_tomatoes import create_movie_tiles_content
#from fresh_tomatoes import open_movies_page
import green_tomatoes
#from green_tomatoes import create_movie_tiles_content
#rom green_tomatoes import open_movies_page
import urllib

#some filename.classname fuction _init_ is called
#When I initialize a new class in this way, it refers back to media.py
#In media.py, __init__ is called, and all arguments listed are assigned their appropriate variables.
toy_story = media.Movie("Toy Story", "A story of a boy and his toys","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4") 
bugs_life = media.Movie("A Bug's Life", "An epic of minuscule proportions","http://e.movie.as/p/36151.jpg","https://www.youtube.com/watch?v=vhGlMv3UCXA")
toy_story2 = media.Movie("Toy Story 2", "Another story of a boy and his toys","https://fanart.tv/fanart/movies/863/movieposter/toy-story-2-5275e1f63a9f3.jpg","https://www.youtube.com/watch?v=Lu0sotERXhI")
monsters_inc = media.Movie("Monsters, Inc.", "A story of a boy and his toys","http://vignette2.wikia.nocookie.net/disney/images/f/fe/1000px-Monsters_inc_ver1_xlg.jpeg/revision/latest?cb=20120905225732","https://youtu.be/Ue_SfrHHBAc")
finding_nemo = media.Movie("Finding Nemo", "A story of a boy and his toys","http://assets.fontsinuse.com/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0","https://www.youtube.com/watch?v=2zLkasScy7A") 
incredibles = media.Movie("The Incredibles", "A story of a boy and his toys","http://www.movie-poster-artwork-finder.com/posters/the-incredibles-poster-artwork-craig-t-nelson-holly-hunter-samuel-l-jackson.jpg","https://www.youtube.com/watch?v=DYYt3nOrSkY")
cars = media.Movie("Cars", "A story of a boy and his toys","http://www.cyber-cinema.com/reprint/CarsAdvC867027.jpg","https://www.youtube.com/watch?v=SbXIj2T-_uk")
ratatouille = media.Movie("Ratatouille", "A health inspector's nightmare","http://www.movieartarena.com/imgs/ratatouillef.jpg","https://www.youtube.com/watch?v=niD-jahFURU")
walle = media.Movie("WALL-E", "A story of a boy and his toys","http://images1.fanpop.com/images/image_uploads/Official-Movie-Poster-wall-e-818680_565_837.jpg","https://www.youtube.com/watch?v=8-_9n5DtKOc")
up = media.Movie("Up", "A story of a boy and his toys","http://cdn1.ssninsider.com/wp-content/uploads/2013/11/up-movie-poster.jpg","https://www.youtube.com/watch?v=qas5lWp7_R0")
toy_story3 = media.Movie("Toy Story 3", "A third story of a boy and his toys","https://www.movieposter.com/posters/archive/main/98/MPW-49351","https://www.youtube.com/watch?v=JcpWXaA2qeg")
cars2 = media.Movie("Cars 2", "A story of a boy and his toys","http://cdn.collider.com/wp-content/uploads/cars-2-movie-poster-cast-hi-res-01.jpg","https://www.youtube.com/watch?v=R424MGHDFDc")
brave = media.Movie("Brave", "A story of a boy and his toys","http://cdn.collider.com/wp-content/uploads/brave-movie-poster1.jpg","https://www.youtube.com/watch?v=6CKcqIahedc")
monsters_u = media.Movie("Monsters University", "A story of a boy and his toys","http://cdn.collider.com/wp-content/uploads/monsters-university-movie-poster.jpg","https://www.youtube.com/watch?v=ODePHkWSg-U")
inside_out = media.Movie("Inside Out", "All the feels","https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg","https://www.youtube.com/watch?v=-kArxASiw3Y") 
good_dinosaur = media.Movie("The Good Dinosaur", "A story of a boy and his toys","http://www.rotoscopers.com/wp-content/uploads/2015/09/TheGoodDinoGif1.gif","https://www.youtube.com/watch?v=7BrH72aFXfI")

#1 For my Beta functionality, what I want to try to do is initialize something that takes arguments.
#1 Each argument will be driven by initial user input.
string = movie_request=media.Movie("A", "A custom story of usr-defined elements","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

#First user-facing info.
print("Which movie would you like to know about?")
print("\n")

def user_input():
#For initial user input and error-handling loops
    global movie_request
    global search
    global argument
    movie_request = raw_input("Please indicate \n\"All\" to view the full Pixar library, \nor \"Beta\" or your own entry to preview some lighthearted beta functionality:\n")
    argument = movie_request
    search = argument
    profanity_result = 1
    word_result = 1
    trailer_output = "www.google.com"
    google_output = "www.google.com"
    request()

def user_input2():
#For the beta error-handling loop
    global movie_request
    global search
    global argument
    movie_request = raw_input("Please enter a valid, single-word movie title:\n")
    argument = movie_request
    search = argument
    profanity_result = 1
    word_result = 1
    trailer_output = "www.google.com"
    google_output = "www.google.com"
    beta(movie_request)

def standard_input():
#To direct standard input ("All") to appropriate webspace
    global movie_request
    movies = movie_request
    print "\nDefault browser opening..."
    fresh_tomatoes.open_movies_page(movies)

def custom_input():
#To direct custom input ("Beta") to appropriate webspace
    global string
    global movie_request
    string = movie_request
    movie_request=string
    
    string = movie_request=media.Movie(movie_request, "A custom story of user-defined elements, presented in glorious BETA","http://sleepheroapp.com/wp-content/uploads/2015/02/Blog-Beta-testing_Renso-Kuster.gif","https://www.youtube.com/watch?v=bVQgrjttsD0")

    movies = [string]
    green_tomatoes.open_movies_page(movies)

def check_word(movie_request):
#For handling raw user input: English word validation
    global word_result
    #open connection to website
    connection = urllib.urlopen("http://dictionary.reference.com/browse/"+movie_request)
    #read a response from connection
    wdoutput = connection.geturl()
    print("\n")
    print("| Word Analysis Complete.")
    if wdoutput=="http://dictionary.reference.com/browse/"+movie_request:
        print(" ... You typed a word! Excellent.\n")
        word_result=0
    else:
        print(" ... Cat got your keyboard? I'm not sure that's a word. Try again.\n")
        word_result=1
    #close connection
    connection.close()
    return word_result

def check_profanity(movie_request):
#For handling raw user input: Profanity checker
    global profanity_result
    #open connection to website
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+movie_request)
    #read a response from connection
    output = connection.read()
    #print("\n")
    print("| Profanity Analysis Complete.")
    if output=="{\"response\": \"false\"}":
        print(" ... No profanity here! Good-*** work.\n")
        profanity_result=0
    else:
        print(" ... Profanity-ridden! \n\n ... Let's keep this PG. Try again.\n")
        profanity_result=1
    return profanity_result
    #close connection

    connection.close()

def beta(movie_request):
#takes custom input after we've opted into beta program and checks for
#word validity and profanity before passing to custom class
    global argument
    
    print "\n"
    print("... You have requested "+ "\""+movie_request+"\"")
    print "\n"
    print("... Hmm. I don't recognize that movie. Analyzing ... ")
    check_word(movie_request)
    if word_result==1:
        movie_request=[argument]
        argument=movie_request
        search = argument
        user_input2()
    else:
        check_profanity(movie_request)
        if profanity_result==1:
            movie_request=[argument]
            argument=movie_request
            search = argument
            user_input2()
        else:
            string=movie_request
            custom_input()

def request():
#The bread and butter. Receive user raw input and sort or reply as appropriate.
    global movie_request
    global argument

    if movie_request=="Beta" or movie_request=="beta" or movie_request=="BETA":
    #Explain the beta program
        print "\n"
        print("... You have indicated that you would like to preview our beta functionality area.")
        print("In this area, you will be asked to enter raw input for a movie request of your choice.")
        print("Your input will be checked to confirm:\n (1) That it is a valid English word\n (2) That it does not meet Google's definition of profanity")
        print("Your input will then be passed to a custom class for display on a web page.")
        print("Note - beta functionality focuses on error handling and validation related to raw user input.")
        print("Future permutations of this program will solve additional problems, such as how to supply content that matches the user's request.")
        print("\nLet's begin!")
        print "\n"
        movie_request = raw_input("Please enter a valid, single-word movie title:")
        beta(movie_request)
    else:
    #Return the standard output
        if movie_request=="All" or movie_request=="all" or movie_request=="ALL":
            print "\n"
            print("... You have indicated \"All\". \nLoading the Xttk Pixar Full Library Selections list!")
            movie_request=[toy_story,toy_story2,toy_story3,bugs_life,monsters_inc,finding_nemo,incredibles,cars,ratatouille,walle,up,cars2,brave,monsters_u,inside_out,good_dinosaur]
            standard_input()
        else:
        #Catch-all for user input, defaults to beta program
            print "\n"
            print("... You have requested "+ "\""+movie_request+"\"")
            print "\n"
            print("... Hmm. I don't recognize that movie. Analyzing ... ")
            check_word(movie_request)
            if word_result==1:
                movie_request=[argument]
                argument=movie_request
                search = argument
                user_input()
            else:
                check_profanity(movie_request)
                if profanity_result==1:
                    movie_request=[argument]
                    argument=movie_request
                    search = argument
                    user_input()
                else:
                    string=movie_request


user_input()

