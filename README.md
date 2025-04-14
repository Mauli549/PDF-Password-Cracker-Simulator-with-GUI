# PDF-Password-Cracker-Simulator-with-GUI


PDF Password Cracker Simulator - Documentation
Author: Mauli Gaming
Project Title:
PDF Password Cracker Simulator (Brute Force Based GUI Tool)



Description:

 This project is a GUI-based PDF Password Cracker Simulator built using Python and Tkinter. It
demonstrates how brute-force attacks work by trying all possible password combinations based on
the given character set and password length. It provides a visually interactive interface with features
like theme toggling, progress tracking, sound notifications, and a log panel.


Features:
1. GUI using Tkinter.
2. File selection using file dialog.
3. Brute force password cracking logic using itertools.product.
4. Live progress bar updates.
5. Output logging panel with scroll functionality.
6. Dark and light theme toggle.
7. Max password length input field.
8. Background image support.
9. Sound effect on password crack success.
10. Error handling and validations with message boxes.

Technologies Used:
- Python 3
- Tkinter for GUI
- PyPDF2 for PDF password checking
- Pygame for playing sound effects
- Pillow (PIL) for image handling
- itertools for generating password combinations
  
How It Works:
1. User selects a password-protected PDF file.
2. User enters the maximum password length for brute-force.
3. On clicking 'Start Cracking', the tool:
 - Tries all combinations of characters up to that length.
 - Uses PdfReader to attempt opening the file with each password.
 - If a password is correct, it shows the password and plays a success sound.
4. The GUI updates the log panel and progress bar in real-time.

How to Run:
Requirements:
Install required libraries using:
pip install pygame PyPDF2 pillow
Run the script:
python your_script_name.py

GUI Components:
- Browse PDF: Select a password-protected PDF.
- Max Length Input: Enter max password length (e.g., 3, 4).
- Start Cracking: Begins brute-force attack simulation.
- Toggle Theme: Switch between light/dark mode.
- Output Log: Shows real-time attempt logs and results.
- Progress Bar: Shows cracking progress.

Notes:
- This is a simulator for educational purposes and ethical hacking learning only.
- It may take time for longer passwords due to the exponential number of combinations.
- The tool supports alphabetic and numeric character combinations

![image alt](https://github.com/Mauli549/PDF-Password-Cracker-Simulator-with-GUI/blob/c4631f2c50b305df001b2d0e8478e26acadf042e/Screenshot%202025-04-13%20172750.png)\
![image alt](https://github.com/Mauli549/PDF-Password-Cracker-Simulator-with-GUI/blob/4bff6445a64b2d88240d90937cd89af11c165771/Screenshot%202025-04-13%20172806.png)
![image alt](https://github.com/Mauli549/PDF-Password-Cracker-Simulator-with-GUI/blob/bf3b6916d428181673beb8b2fd62b280149e4000/Screenshot%202025-04-13%20172837.png)
 
