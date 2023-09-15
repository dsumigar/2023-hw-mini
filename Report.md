Exercise 1:

Question 1: I believe that the program will take a little more than 3 seconds to run for 3 loop iterations and a 1 second sleep time between iterations. Yes, our prediction was correct, it ran in 3.003 seconds and the predicted time was 3 seconds. The program prints out “How many times shall I loop?”; asking for an input. Then it prints “How long shall U sleep for each loop iteration”; asking for an input. Once these inputs are given, the program prints “Total time (predicted, seconds): 3.0. The rest of what is printed is shown below through the screenshot.  

![image](https://github.com/dsumigar/2023-hw-mini/assets/114698332/26b7282c-b9c2-496c-990c-780a43de8ff7)

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
