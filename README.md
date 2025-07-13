🔑 Simple Python Keylogger

This is a basic keylogger written in Python using the pynput library.
It listens for all keyboard presses on your system and saves them to a file named keys.txt in the current directory.

Once started, it runs in the background and logs every key you press, including letters, numbers, and special keys like Enter or Shift.
This is intended for educational and ethical purposes only — such as learning how keyloggers work or monitoring your own machine.
⚠️ Do not use this on anyone’s system without their explicit permission.

📦 Required Python Modules
This script requires the following Python module(s):

pynput — for listening to keyboard events

You can install it with pip:

bash
Copy
Edit
pip install pynput
🚀 How to Run
1️⃣ Clone or download this repository.
2️⃣ Install the required module if you haven’t already:

bash
Copy
Edit
pip install pynput
3️⃣ Run the script:

bash
Copy
Edit
python3 keylogger.py
On Linux/Mac, it will fork into the background and save keystrokes into keys.txt.
On Windows, you may need to remove the os.fork() and os.setsid() lines because fork() is not supported there.

📄 Output
All keystrokes are appended to a file named:

Copy
Edit
keys.txt
Sample log:

vbnet
Copy
Edit
key: a
key: b
key: Key.space
key: c
key: Key.enter

⚖️ Disclaimer
This code is for educational purposes only.
Do not use it to spy on others or perform malicious activities — doing so may violate privacy laws and ethical guidelines.
