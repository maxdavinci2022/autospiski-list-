# autospiski-list-
This repository contains two Python scripts that allow users to input data into a list with a time limit for each entry (3 seconds by default). The first script handles all inputs as strings, while the second script intelligently converts numeric inputs (integers and floats) into their respective types

Features  

  Timed Input :   
        Users have 3 seconds to input data. If the time runs out, the program stops and displays the collected data.
         
  Flexible Data Handling :   
        Script 1 : Accepts all inputs as strings (e.g., integers, floats, text, symbols).
        Script 2 : Automatically detects and converts numeric inputs (integers and floats) while keeping other inputs as strings.
         
  User-Friendly Output :   
        The final list is displayed in the format l = [...].
         
  Error Handling :   
        Handles invalid inputs gracefully without crashing the program.

Scripts  
1. timed_input_all.py  

This script collects all user inputs as strings and stores them in a list. 
How It Works  

    Prompts the user to input data every 3 seconds.
    Adds all inputs (numbers, text, symbols) directly to the list as strings.
    Stops when the user fails to input data within 3 seconds.
     

Usage  

    Clone the repository:
