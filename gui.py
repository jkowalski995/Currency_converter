"""
This program was made by Jakub KOWALSKI.
GitHub repository: https://github.com/jkowalski995

This is the main program witch starts the GUI and print the result of currency change.
"""

import PySimpleGUI as Sg
from convert import calculate, calculate_one_way


layout = [
    [Sg.Text("Please enter this data below to proceed!")],
    [Sg.Text()],
    [Sg.Text("Select if You have Polish Zloty (PLN)"), Sg.Checkbox('', default=False, key="-PLN-", enable_events=True)],
    [Sg.Text("Provide the code of currency You have", size=(40, 1)),
     Sg.InputText(key="-currency_have-", disabled=False)],
    [Sg.Text("Provide the amount of currency You have", size=(40, 1)), Sg.InputText(key="-amount_have-")],
    [Sg.Text("Provide the code of currency You want to have", size=(40, 1)), Sg.InputText(key="-currency_want-")],
    [Sg.Button("Convert")],
    [Sg.Exit()]
]

if __name__ == '__main__':

    window = Sg.Window(title="Currency changer", layout=layout, margins=(100, 50))

    while True:
        event, values = window.read()
        print(event, values)

        # Toggle the first input field
        if event == "-PLN-":
            if not window["-currency_have-"].Disabled:
                window["-currency_have-"].Update(disabled=True)
            else:
                window["-currency_have-"].Update(disabled=False)

        # Exit the program
        if event == Sg.WINDOW_CLOSED or event == 'Exit':
            break

        # Convert the values
        elif event == "Convert":

            currency_have = values["-currency_have-"]
            amount_have = values["-amount_have-"]
            currency_want = values["-currency_want-"]
            check_box = values["-PLN-"]

            # Check if box is marked
            if not window["-currency_have-"].Disabled:

                # Check the values if any is empty
                if currency_want == '' or amount_have == '' or currency_have == '':
                    print("Every field must be filled with proper value")
                else:
                    try:  # Check if amount is a number
                        amount_have = float(amount_have)
                        # calculate with box not checked
                        Sg.popup(calculate(currency_have, currency_want, amount_have), title="Result!", line_width=300)
                    except ValueError:
                        print("Second value must be an integer!")

            else:

                # Check the values if any is empty
                if currency_want == '' or amount_have == '':
                    print("Every field must be filled with proper value")
                else:
                    try:  # Check if amount is a number
                        amount_have = float(amount_have)
                        # calculate with box checked
                        Sg.popup(calculate_one_way(currency_want, amount_have), title="Result!", line_width=300)
                    except ValueError:
                        print("Second value must be an integer!")

    window.close()
