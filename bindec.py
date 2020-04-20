import PySimpleGUI as sg


class PythonScreen:
    def __init__(self):
        sg.change_look_and_feel('DarkGrey')
        # layout
        layout = [
            [sg.Text('Enter a whole number', size=(20,0)), sg.Input(size=(15, 0), key='num')],
            [sg.Text('Convert to:')],
            [sg.Radio('Binary','convtype',key='binary'),sg.Radio('Hexadecimal','convtype',key='hexa'),sg.Radio('Octal','convtype',key='octal')],
            [sg.Button('Convert')],
            [sg.Output(size=(38, 8))]
        ]
        # window
        self.window = sg.Window("Numeric bases converter").layout(layout)

    def start(self):
        while True:
            # Extract data from screen
            self.button, self.values = self.window.Read()
            num = self.values['num']
            binary = self.values['binary']
            hexa = self.values['hexa']
            octal = self.values['octal']
            if binary == True:
                print('{} converted to binary is {}'.format(num, bin(int(num))[2:]))
            elif hexa == True:
                print('{} converted to hexadecimal is {}'.format(num, oct(int(num))[2:]))
            elif octal == True:
                print('{} coverted para octal é igual a {}'.format(num, hex(int(num))[2:]))
            else:
                print('\033[31mInvalid option\033[m')


screen = PythonScreen()
screen.start()
