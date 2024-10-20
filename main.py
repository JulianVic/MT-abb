import tkinter as tk
from tkinter import ttk

class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transitions):
        self.tape = list(tape) + ['']
        self.head_position = 0
        self.state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def step(self):
        symbol = self.tape[self.head_position]

        if (self.state, symbol) in self.transitions:
            new_state, write_symbol, direction = self.transitions[(self.state, symbol)]
            self.tape[self.head_position] = write_symbol

            if direction == 'R':
                self.head_position += 1
                if self.head_position >= len(self.tape):
                    self.tape.append('')
            elif direction == 'L':
                if self.head_position == 0:
                    self.tape.insert(0, '')
                else:
                    self.head_position -= 1

            self.state = new_state
        else:
            return False
        return True

    def run(self):
        while self.state not in self.final_states:
            if not self.step():
                return False
        return True

def validate_string():
    input_string = entry.get()
    result = "valid" if run_turing_machine(input_string) else "invalid"
    table.insert("", tk.END, values=(input_string, result))

def run_turing_machine(input_string):
    initial_state = 'q0'
    final_states = {'q4'}
    transitions = {
        ('q0', 'a'): ('q1', 'a', 'R'),
        ('q1', 'b'): ('q2', 'b', 'R'),
        ('q2', 'b'): ('q3', 'b', 'R'),
        ('q3', 'a'): ('q1', 'a', 'R'),
        ('q3', ''): ('q4', '', 'L'),
    }
    tm = TuringMachine(input_string, initial_state, final_states, transitions)
    return tm.run()

root = tk.Tk()
root.title("MT abb")

label = tk.Label(root, text="Ingrese una cadena:")
label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

validate_button = tk.Button(root, text="Validar", command=validate_string)
validate_button.grid(row=0, column=2, padx=10, pady=10)

columns = ("input", "result")
table = ttk.Treeview(root, columns=columns, show="headings")
table.heading("input", text="Input")
table.heading("result", text="Result")
table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=table.yview)
scrollbar.grid(row=1, column=3, sticky="ns")
table.configure(yscrollcommand=scrollbar.set)

root.mainloop()
