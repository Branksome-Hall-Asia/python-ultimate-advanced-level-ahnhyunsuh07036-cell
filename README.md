<h1>🎓 Level 3: Advanced Python & Systems</h1>

<p>Welcome to the final tier. In this level, we move beyond simple scripts and start building "Software." You will learn to handle data like a pro, use external libraries, and create systems that "remember" information even after the program is closed.</p>

<p><strong>HOW TO USE THIS REPO:</strong> Each task file contains an <strong>EXAMPLE</strong> (code you can run) followed by a <strong>CHALLENGE</strong>. You must write your own code in the Challenge section to complete the level.</p>
<hr>

<h2>🛠 THE 12 ADVANCED SKILLS</h2>

<h3>1. Dictionaries (Key-Value Pairs)</h3>
<p><strong>The Concept:</strong> A List uses numbers (0, 1, 2). A Dictionary uses "Keys" (words).</p>
<p><strong>Example:</strong></p>
<pre>car = {"brand": "Tesla", "model": "Model 3", "year": 2024}
print(car["brand"]) # Output: Tesla</pre>
<p><strong>Task:</strong> Open task_01_dict_intro.py and create a student profile dictionary.</p>

<hr>

<h3>2. Dictionary Methods (.keys, .values, .items)</h3>
<p><strong>The Concept:</strong> Extract just labels, just data, or both.</p>
<p><strong>Example:</strong></p>
<pre>book = {"title": "The Hobbit", "author": "Tolkien"}
print(book.keys())   # Shows: ['title', 'author']
print(book.values()) # Shows: ['The Hobbit', 'Tolkien']</pre>
<p><strong>Task:</strong> Loop through a dictionary and print only the "Values" in task_02_dict_methods.py.</p>

<hr>

<h3>3. File Reading (.txt)</h3>
<p><strong>The Concept:</strong> Using "with open" to pull data from a text file.</p>
<p><strong>Example:</strong></p>
<pre>with open("my_notes.txt", "r") as f:
    content = f.read()
    print(content)</pre>
<p><strong>Task:</strong> Read the secrets from secrets.txt in task_03_file_read.py.</p>

<hr>

<h3>4. File Writing & Appending</h3>
<p><strong>The Concept:</strong> 'w' overwrites; 'a' (Append) adds to the bottom.</p>
<p><strong>Example:</strong></p>
<pre>with open("high_scores.txt", "a") as f:
    f.write("Player1: 5000\n")</pre>
<p><strong>Task:</strong> Build a persistent "Guest Book" in task_04_file_write.py.</p>

<hr>

<h3>5. CSV Data Tables</h3>
<p><strong>The Concept:</strong> Handling "Excel-style" data where values are separated by commas.</p>
<p><strong>Task:</strong> Import the csv library and read the database.txt file in task_05_csv_intro.py.</p>

<hr>

<h3>6. The Datetime Library</h3>
<p><strong>The Concept:</strong> Adding timestamps to your programs.</p>
<pre>import datetime
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))</pre>
<p><strong>Task:</strong> Print the current date and time in task_06_datetime.py.</p>

<hr>

<h3>7. The OS Library</h3>
<p><strong>The Concept:</strong> Letting Python interact with your folders and files.</p>
<p><strong>Task:</strong> List every file in your folder in task_07_os_library.py.</p>

<hr>

<h3>8. Turtle Graphics (Coordinates)</h3>
<p><strong>The Concept:</strong> Moving a "Turtle" using X and Y math coordinates.</p>
<p><strong>Task:</strong> Use t.goto(x, y) to draw shapes in task_08_turtle_basics.py.</p>

<hr>

<h3>9. Turtle Loops (Algorithmic Art)</h3>
<p><strong>The Concept:</strong> Combining loops with turns to create patterns.</p>
<p><strong>Task:</strong> Draw a colorful geometric pattern in task_09_turtle_loops.py.</p>

<hr>

<h3>10. List Comprehension (Pro Mode)</h3>
<p><strong>The Concept:</strong> Creating a new list in just one single line of code.</p>
<pre>squares = [x*x for x in range(6)] 
# Result: [0, 1, 4, 9, 16, 25]</pre>
<p><strong>Task:</strong> Filter a list of prices in task_10_list_comp.py.</p>

<hr>

<h3>11. PIP & External Packages</h3>
<p><strong>The Concept:</strong> How to install code "packages" via the terminal.</p>
<p><strong>Task:</strong> Install and use the cowsay library in task_11_pip_install.py.</p>

<hr>

<h3>12. Custom Error Handling (Try/Except)</h3>
<p><strong>The Concept:</strong> Creating "Safety Nets" so your program doesn't crash.</p>
<pre>try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That is not a valid number!")</pre>
<p><strong>Task:</strong> Use raise ValueError for an invalid PIN in task_12_error_handling.py.</p>

<hr>

<h2>🏛 THE MEGA-PROJECT: SECURE ATM SYSTEM</h2>
<p><strong>File: MEGA_PROJECT_ATM.py</strong></p>
<ul>
    <li><strong>Load:</strong> Reads names and balances from database.txt.</li>
    <li><strong>Verify:</strong> Checks a PIN against a Dictionary.</li>
    <li><strong>Transaction:</strong> Allows the user to "Withdraw" money.</li>
    <li><strong>Save:</strong> Writes the new balance back to the file.</li>
    <li><strong>Receipt:</strong> Prints a timestamped receipt using Datetime.</li>
</ul>
