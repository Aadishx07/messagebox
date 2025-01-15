# messagebox

This is a simple Tkinter-based GUI application that serves as a registration form. It allows users to input personal details such as their name, email, phone number, gender, and preferred course, and provides validation for required fields.

## Features

- **Input Fields:** 
  - First Name
  - Middle Name
  - Last Name
  - Email
  - Phone Number
  - Gender (Male/Female)
  - Selected Course
- **Validation:** Ensures that all required fields are filled before submission.
- **Submit and Clear Buttons:** 
  - `Submit` displays the entered data in a message box.
  - `Clear` resets all input fields to their default state.
- **Graphical Interface:** Built using Python's Tkinter library.

## Prerequisites

- Python 3.x
- Tkinter (included in the standard Python library)

## How to Run

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script with the following command:
   ```bash
   python registration_form.py
   ```

## Usage

1. Fill in the form fields.
2. Select your gender and course using the radio buttons.
3. Click the **Submit** button to validate and display your input data.
4. Use the **Clear** button to reset the form fields.

## Example Screenshot

(*Include a screenshot of the GUI here, if available.*)

## Code Overview

- **`submit()` Function:** Validates input fields and displays the entered data.
- **`clear()` Function:** Resets all form fields to empty or default values.
- **Tkinter Components:**
  - `Label`: Used for field descriptions.
  - `Entry`: Input fields for text data.
  - `Radiobutton`: Used for selecting gender and courses.
  - `Button`: Trigger actions like submitting or clearing the form.

## Potential Enhancements

- Add input validation for email format and phone number.
- Include additional fields or dynamic course selection.
- Store the registration data in a file or database.

