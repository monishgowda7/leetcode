class Movie:
    
    def __init__(self,name,rating,release_year):
        self.name=name
        self.rating=rating
        self.release_year=release_year
        
    
    def movie_name(self):
        return f"Movie name is {self.name}"
    
    def movie_rating(self):
        return f"{self.name} movie Rating is {self.rating}"
    
    def release(self):
        return f"{self.name} movie will be released by {self.release_year}"
    
    
a=Movie("toxic",10,2026)    
b=Movie("durandar",9,2026)
c=Movie("maze runner",9.5,2015)

print("------Highest rated movie-------")
movies=[a,b,c]
highest=movies[0]
for i in movies:
    if i.rating>highest.rating:
        highest=i
        
print("Name        :",highest.name) 
print("rating      :",highest.rating)
print("Release year:",highest.release_year)       


    
    