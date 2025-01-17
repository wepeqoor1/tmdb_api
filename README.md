# Themoviedb
Downloading films description and generate rating.

## **Environment requirements**
Python3.10+

## **How to install**
```bash
$ pip install -r requirements.txt
```

## **API-key**
You want generate API-key in https://api.themoviedb.org

## **hello_api_TMDB.py**
Takes the API key. If it is missing, the program terminates with the error `Invalid api key'.  
Shows the budget of the movie if the key is valid.

## **tmdb_helpers.py**
Prompts the user to enter the API key. 
Generates a service request https://api.themoviedb.org and returns data depending on the method.  
Otherwise, it causes an authorization error.  

## **search_in_db.py**
Offers to enter the path to the database. If there is no database, it outputs the error `File not found, sorry...`.  
It offers to enter the original name of the movie.  
Searches for a movie in the local database by the original title and outputs the names of the movies that match to the console.

## **make_own_db.py**
Creates local database.  
Checks the API key for validity, otherwise the program terminates with the error `Invalid api key`.    
Uploads (by default) 1000 movies to the specified file (by default `MyFilmDB.json').  

## **find_similar.py**
Offers to enter the path to the database. If there is no database, it outputs the error `File not found, sorry...`  
It prompts you to enter the name of the movie. Searches for a movie in the database.  
If the movie is not found, the program terminates with the error `No such film in FilmsDB'.  
Then selects recommendations based on the rating of the movie and output the names of similar movies in the console.  
**Example:**

```bash
python3 find_similar.py
```                                                                            
```bash 
Enter path to DataBase:MyFilmDB.json  
```
```bash     
Enter film to search for:Ariel
```
Then output the names of similar movies.
``` bash 
Elsker dig for evigt
Hable con ella
Kunstgriff
Las Hurdes
Megacities
Sonntag im August
The Dark
To Die For
Varjoja paratiisissa
```

## **own_db_helpers.py**
Checks for the presence of the file and reads the data.
