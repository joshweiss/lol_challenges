import openpyxl
import string
import PySimpleGUI as sg

categories = ['hello']
charges = []

# Setting up the Gui
sg.ChangeLookAndFeel('BlueMono')

layout = [
    [sg.Text('Month'), sg.Combo(
        ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
         'September'], key='month')],
    [sg.Text('What is the charge?'), sg.InputText(key='detail', size=(30, 1), do_not_clear=False)],
    [sg.Text('Cost?', size=(19, 1)), sg.InputText(key='cost', size=(10, 1), do_not_clear=False)],
    [sg.Text('Type of Expense'), sg.Combo(categories, key='category')],
    [sg.Submit(), sg.Exit(), sg.Button('Show Monthly Totals')]
]

window = sg.Window("LOL Challenges").Layout(layout)

while True:
    button, values = window.Read()
    if button is None or button == 'Exit':
        break
    # Adding the values from the gui into a list of dictionaries for each time the form was submitted
    if button == 'Submit':
        charges.append({'detail': values['detail'], 'cost': float(values['cost']), 'category': values['category'],
                        'month': values['month']})
    if button == 'Show Monthly Totals':
        month_for_show = values['month']
        show_monthly_totals = True
        break

window.Close()

print(charges)