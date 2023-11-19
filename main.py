class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initial_state = None
        self.final_states = set()

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            self.states = set(lines[0].split(','))
            self.alphabet = set(lines[1].split(','))
            self.initial_state = lines[2]
            self.final_states = set(lines[3].split(','))

        for transition in lines[4:]:
            parts = transition.split(',')
            if len(parts) != 3:
                continue 
            src, symbol, dst = parts
            if (src, symbol) not in self.transitions:
                self.transitions[(src, symbol)] = dst


    def display(self):
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Transitions:", self.transitions)
        print("Initial State:", self.initial_state)
        print("Final States:", self.final_states)

    def accepts_sequence(self, sequence):
        current_state = self.initial_state
        for symbol in sequence:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.final_states

def main():
    fa = FiniteAutomaton()
    fa.read_from_file("FLCD-LAB4/FA.in")

    while True:
        print("\nFinite Automaton Menu:")
        print("1. Display FA elements")
        print("2. Check sequence acceptance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            fa.display()
        elif choice == '2':
            sequence = input("Enter the sequence: ")
            print("Sequence accepted:" if fa.accepts_sequence(sequence) else "Sequence not accepted")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
