## Install all requirements
```pip install -r requirements.txt``` 

## Run server

```python server.py``` 
    or 
```export FLASK_APP=server.py & flask run```

## How to use:

#### Get all games

``` http://127.0.0.1:5000/test ```

#### Get number of games 

``` http://127.0.0.1:5000/get_number ```

#### Find something
by name of the game:
``` http://127.0.0.1:5000/search?game_name=<game_name> ``` 

or by keyword: 
``` http://127.0.0.1:5000/search?keyword=<keyword> ```


