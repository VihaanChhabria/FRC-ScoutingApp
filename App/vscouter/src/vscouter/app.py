"""
A scouting app made for FRC.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import socket


class VScouter(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        button = toga.Button(
            "Initialize Match Scouter",
            on_press=self.sendBluetoothRequest,
            style=Pack(padding=5)
        )
        main_box.add(button)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def sendBluetoothRequest():
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        client.connect(("20:1e:88:18:14:ff", 4))

        client.send("message".encode("utf-8"))



def main():
    return VScouter()

