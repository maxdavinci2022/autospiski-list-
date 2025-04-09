# autospiski-list-
This repository contains two Python scripts that allow users to input data into a list with a time limit for each entry (3 seconds by default). The first script handles all inputs as strings, while the second script intelligently converts numeric inputs (integers and floats) into their respective types


Features  

Timed Input :   
  Users have 3 seconds to input data for each entry. If the time runs out, the program stops and displays the collected data.

Flexible Data Handling :   
  autolist_from_numbers.py : Automatically detects and converts numeric inputs (integers and floats) into their respective types.
  autolist_from_data.py : Accepts all inputs as strings, regardless of their type.

User-Friendly Output :   
  The final list is displayed in the format l = [...].

Error Handling :   
  Handles invalid inputs gracefully without crashing the program.

1. autolist_from_numbers.py  

This script intelligently detects numeric inputs (integers and floats) and converts them into their respective types while ignoring non-numeric inputs. 
How It Works  

    Prompts the user to input data every 3 seconds.
    Detects if the input is an integer or float and converts it accordingly.
    Ignores non-numeric inputs.
    Stops when the user fails to input data within 3 seconds.
     

Usage  

    Clone the repository:
    bash
     

 
1
git clone https://github.com/maxdavinci2022/autospiski-list-.git
 
 
Navigate to the directory:
bash
 
 
1
cd autospiski-list-
 
 
Install the required dependency:
bash
 
 
1
pip install inputimeout
 
 
Run the script:
bash
 

     
    1
    python autolist_from_numbers.py
     
     
     

Example  
 
 
1
2
3
4
5
6
7
8
9
10
Enter data (numbers only). You have 3 seconds for each input.
Enter data: 9
Number 9 added to the list.
Enter data: 3.14
Number 3.14 added to the list.
Enter data: hello
Invalid input. Only numbers are accepted.
Enter data: 
Time is up! Program terminated.
Your list: l = [9, 3.14]
 
 
2. autolist_from_data.py  

This script collects all user inputs as strings and stores them in a list. 
How It Works  

    Prompts the user to input data every 3 seconds.
    Adds all inputs (numbers, text, symbols) directly to the list as strings.
    Stops when the user fails to input data within 3 seconds.
     

Usage  

    Clone the repository:
    bash
     

 
1
git clone https://github.com/maxdavinci2022/autospiski-list-.git
 
 
Navigate to the directory:
bash
 
 
1
cd autospiski-list-
 
 
Install the required dependency:
bash
 
 
1
pip install inputimeout
 
 
Run the script:
bash
 

     
    1
    python autolist_from_data.py
     
     
     

Example  
 
 
1
2
3
4
5
6
7
8
9
10
11
12
Enter data (any type). You have 3 seconds for each input.
Enter data: 9
Data '9' added to the list.
Enter data: 3.14
Data '3.14' added to the list.
Enter data: hello
Data 'hello' added to the list.
Enter data: @
Data '@' added to the list.
Enter data: 
Time is up! Program terminated.
Your list: l = ['9', '3.14', 'hello', '@']
 
 
Installation  

    Ensure you have Python installed. You can check by running: 
    bash
     

 
1
python --version
 
 

If not installed, download Python from python.org . 

Install the required dependency: 
bash
 

     
    1
    pip install inputimeout
     
     
     

Contributing  

If you'd like to contribute to this project: 

    Fork the repository.
    Create a new branch (git checkout -b feature/YourFeatureName).
    Commit your changes (git commit -m "Add some feature").
    Push to the branch (git push origin feature/YourFeatureName).
    Open a pull request.
     

License  

This project is licensed under the MIT License. See the LICENSE  file for details. 
Contact  

For questions or suggestions, feel free to reach out: 

    Email: your.email@example.com 
    GitHub: @maxdavinci2022 
