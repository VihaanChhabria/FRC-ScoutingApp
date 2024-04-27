"""
A scouting application for FRC made by Vihaan Chhabria.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class VScouter(toga.App):

    TEXT_QUESTION = "text"
    COUNTER_QUESTION = "counter"
    BOOLEAN_QUESTION = "boolean"

    matchQuestions = {
        "Match Number" : TEXT_QUESTION,
        "Team Number" : TEXT_QUESTION,
        "Initials" : TEXT_QUESTION,
        "Auto Shots in Amp" : COUNTER_QUESTION,
        "Auto Shots Missed in Amp" : COUNTER_QUESTION,
        "Auto Shots in Speaker" : COUNTER_QUESTION,
        "Auto Shots Missed in Amp" : COUNTER_QUESTION,
        "Taxi Off Starting Zone" : BOOLEAN_QUESTION,
        "Teleop Shots in Amp" : COUNTER_QUESTION,
        "Teleop Shots Missed in Amp" : COUNTER_QUESTION,
        "Teleop Shots in Speaker" : COUNTER_QUESTION ,
        "Teleop Shots Missed in Amp" : COUNTER_QUESTION,
        "Climbed" : BOOLEAN_QUESTION,
        "Buddy Climbed" : BOOLEAN_QUESTION,
        "Shots in Trap" : COUNTER_QUESTION,
        "Broke Down" : BOOLEAN_QUESTION,
        "Comments" : TEXT_QUESTION
    }

    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        #matchScoutingBox = toga.Box(style=Pack(direction=COLUMN))
        #pitScoutingBox = toga.Box()

        self.displayBox = toga.Box(style=Pack(direction=COLUMN))
        self.displayBox.add(self.WindowGenerators.generateMainWin(self))
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.displayBox
        self.main_window.show()
    
    class WindowGenerators():
        def generateMainWin(self):
            mainBox = toga.Box(style=Pack(direction=COLUMN))

            mainBox.add(
                toga.Button(
                    "Match Scout", 
                    on_press=self.change_window("MatchScout"), 
                    style=Pack(padding=5)))
            
            
            mainBox.add(
                toga.Button(
                    "Pit Scout", 
                    on_press=self.change_window("PitScout"), 
                    style=Pack(padding=5)))

            return mainBox
        
        def generateMatchScoutWin(self):

            def increment(widget, value_label):
                value = int(value_label.text) + 1
                value_label.text = str(value)
            
            # Function to handle decrementing the counter
            def decrement(widget, value_label):
                value = max(0, int(value_label.text) - 1)
                value_label.text = str(value)

            
            matchScoutBox = toga.Box(style=Pack(direction=COLUMN))

            matchScoutBox.add(
                toga.Button(
                    "Return", 
                    on_press=self.change_window("Main"), 
                    style=Pack(padding=5)))
            
            for inputName, inputType in self.matchQuestions.items():

                label = toga.Label(
                    inputName,
                    style=Pack(padding=(0, 5))
                )

                questionBox = toga.Box(style=Pack(direction=ROW, padding=5))
                questionBox.add(label)

                if inputType == self.TEXT_QUESTION:
                    textInput = toga.TextInput(style=Pack(flex=1))
                    questionBox.add(textInput)

                elif inputType == self.COUNTER_QUESTION:
                    
                    value_label = toga.Label("0", style=Pack(padding=(0, 5)))

                    minus_button = toga.Button('-', on_press=lambda widget: decrement(widget, value_label))
                    plus_button = toga.Button('+', on_press=lambda widget: increment(widget, value_label))

                    questionBox.add(minus_button)
                    questionBox.add(value_label)
                    questionBox.add(plus_button)


                matchScoutBox.add(questionBox)
            return matchScoutBox
            
        def generatePitScoutWin(self):
            pitScoutBox = toga.Box(style=Pack(direction=COLUMN))

            pitScoutBox.add(
                toga.Button(
                    "Return", 
                    on_press=self.change_window("Main"), 
                    style=Pack(padding=5)))
            
            return pitScoutBox

    def change_window(self, name):
        def on_press(widget):
            for child in self.displayBox.children:
                self.displayBox.remove(child)

            if name == "MatchScout":
                add = self.WindowGenerators.generateMatchScoutWin(self)
            elif name == "PitScout":
                add = self.WindowGenerators.generatePitScoutWin(self)
            else:
                add = self.WindowGenerators.generateMainWin(self)

            self.displayBox.add(add)
            self.main_window.show()
            
        return on_press


def main():
    return VScouter()