# Impossible passowrd
### First : check for any kind of web connection
#### I spend ten minute to take a look at how it validate flag , it actually doesn't check flag on the server instead it check the flag on client side.
### Second : Where is code that check the flag?
####
```javascript
var grid = [......]; // Contains some data
var index_to_row_column = [];
var index_to_direction = {}
for(var r = 0; r < grid.length; r++){
    for(var c = 0; c < grid[r].length; c++){
        var cell = grid[r][c];
        if(cell == null) continue;
        if(cell['across'] && cell['across']['is_start_of_word']){
            index_to_row_column[cell['across']['index']] = {"row" : r, "col" : c};
            index_to_direction[cell['across']['index']] = "across"
        }

        if(cell['down'] && cell['down']['is_start_of_word']){
            index_to_row_column[cell['down']['index']] = {"row" : r, "col" : c};            
            index_to_direction[cell['down']['index']] = "down"
        }
    }
}
```
#### So the grid variable is where the flag is stored.
### Last : Find the flag
#### I use console windows to run javascript directly.
![Here is my code]()