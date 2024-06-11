def main():

    about_me = { 

        "full_name": "Manuel Manrique",
        "Student_ID": "10326988",
        "Pizza_toppings": [
        
            "Pepperonni", 
             "Cheese", 
             "Mushrooms"
            ],

        "Movies": [
        {
            "title" : "tron Legacy", 
             "genre" : "sci-fi"
        },
        {
            "title" : "how to train your dragon",
             "genre" : "animation"

            }
        ]

    }  
    

    other_movie = {"title": "transformers", "genre": "action"}
    about_me["Movies"].append(other_movie)


    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)

    toppings = ["Pinapple", "Peppers"]
    add_pizza_toppings(about_me, toppings)

    print_movie_genres(about_me)

    movie_list = about_me["Movies"]
    print_movie_titles(movie_list)

	
def print_student_name_and_id(about_me):

    full_name = about_me["full_name"]
    student_id = about_me["Student_ID"]
    first_name = full_name.split()[0]
    NameP = f"My name is {full_name}, but you can call me Don {first_name}."
    Student = f"My student ID is {student_id}."

    print(NameP)
    print(Student, end = '\n\n')

    return
    
def add_pizza_toppings(about_me, toppings):

    print(f"My favourite pizza toppings are:")

    about_me["Pizza_toppings"].extend(toppings)
    toppings_lowercase = [toppings.lower() for toppings in about_me["Pizza_toppings"]]
    toppings_lowercase.sort()

    for item in toppings_lowercase: 
        print(f"- {item}")
    end = "\n"
    print(end)

    return add_pizza_toppings

def print_pizza_toppings(about_me):

    print(f"My favourite pizza toppings are:")

    toppings_uppercase = [topping.upper() for topping in about_me["Pizza_toppings"]]

    for item in toppings_uppercase: 
        print(f"- {item}")
    end = "\n"
    print(end)

    return

def print_movie_genres(about_me):

    Genre = [movie["genre"] for movie in about_me["Movies"]]
    Genre_Listed = ", ".join(Genre[:-1]) + ", and " + Genre[-1]

    print(f"I like to watch {Genre_Listed} movies.", end = "\n\n")

    return 

def print_movie_titles(movie_list):

    Movies = [movie["title"] for movie in movie_list]
    MoviesUp = [Movies.title() for Movies in Movies]
    Movies_Listed = ", ".join(MoviesUp[:-1]) + ", and " + MoviesUp[-1]

    print(f"Some of my favourite movies are {Movies_Listed}!")

    return
    
if __name__ == '__main__':
    main()