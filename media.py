import webbrowser

class Video():
    #parent class to Movie and TvShow, added in Lesson 3b
    def __init__(self, duration, genre):
        self.duration = video_duration
        self.genre = video.genre

class Movie(): #uppercase per style guide\\
    #2 underscores indicate reserved word. init creates space in memory.
    #takes arguments
    #look up Self
    #init initializes pices of information like title storyline

    """ This class describes a movie """
    
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    #after defining __init__ we created some classes in entertainment_center.py
    #when we created these instances, what we did was set aside space
    #for all arguments. Each of the variables used is assigned unique values
    #by class, so these variables have a special name: instance variables.
    #The "self." in front of the instance varibles is important, as it
    #defines them as instance variables, assessible to other functions, rather than local variables
    #
    #when you define a class, you're giving it things to remember (arguments to pass to an __init__)
    #and things to do (functions)
    #
    #

#A function that is defined within s class and associated with an instance
#is called an instance method

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

