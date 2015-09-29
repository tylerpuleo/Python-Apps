import iSenseAPI
import iSense
import random
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()

user_credentials = iSense.Credentials(username="t@t.t", password="t")
number_of_dice_rolls = int(raw_input("Enter number of dice rolls: "))

project = iSense.Project(1379)
field = project.getFieldIds()
print field
dice_rolls = []

for i in xrange(0,number_of_dice_rolls):
	dice_rolls.append(random.randint(1,6))

data_to_be_uploaded = {str(field[0]): dice_rolls }

project.createDataSet("title", data_to_be_uploaded, user_credentials)