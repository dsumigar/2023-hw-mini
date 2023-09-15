Exercise 1:

Q1) I believe that the program will take less than a second to run. Yes, our prediction was correct, it ran in 0.92 seconds. The program prints out “How many times shall I loop?”. 

Q2) The “int” and “float” notation indicates different variable data types. The program won’t run if those notations are removed 

Q3) “time.ticks_diff(toc,tic)” is used instead of toc - tic because it uses ring arithmetic to ensure that the result is accurate for wrap-around values.

Exercise 2:

Q1) Using a JSON file for parameter storage in embedded systems ensures consistency, reduces user errors, and provides non-volatile memory. It simplifies configuration, enhances security, and facilitates automation, eliminating repetitive manual input and offering flexibility for future changes. It also helps in faster data interchange and web service results. 

Q2) We prefer a JSON file because it improves code readability, and separates data from logic, therefore enhancing maintainability, dynamic configurations without changing the codebase, and supports sharing configurations across multiple scripts or platforms.

Q3) Why didn't the exercise02.py code use os.path.isfile, that is, why did I write the "is_regular_file()" function?: The custom is_regular_file() function was written because MicroPython may not have full os.path support. The custom function provides a consistent file-checking interface ensuring compatibility. 

Exercise 3:

Q1) Increasing the sample time in exercise03.py can reduce responsiveness to quick button presses, potentially missing or misinterpreting Morse code dots. With longer sample times relative to the dot_dash_threshold, distinguishing between dots, dashes, and spaces becomes challenging, leading to incorrect Morse code interpretations.

Exercise 4:
See exercise04.py and exercise04.json.
