import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import os

Builder.load_file('graphics.kv')

class ScreenOne(Screen):

	def callback(self):
		os.system('python src/recognition.py')
	def switch_screen(self):
		screen_manager.switch_to(ScreenTwo(name ="screen_two"))

class ScreenTwo(Screen):
	global screen_manager
	def callback(self):
		os.system('python src/recognition.py')
	# def switch_screen1(self):
	# 	screen_manager.switch_to(ScreenTwo(name ="screen_one"))

		#screen_manager.switch_to(ScreenThree(name ="screen_three"))
	def switch_screen(self):
		screen_manager.switch_to(ScreenThree(name ="screen_three"))
	def on_pre_enter(self, *args):
		lab=self.ids["img_label"]
		lab.source='src/plainpic.jpg'
		

	def showemotion(self):
		os.system('python src/recognition.py')	
	
class ScreenThree(Screen):
	def musicplayer(self):
		os.system('python music_app/main.py')		
	def callemotion(self):
		f = open("result.txt", "r")
		emotion_result=f.read()
		f.close()
		print(emotion_result)

		lab=self.ids["emotion_label"]
		lab.text=emotion_result
		# self.ids.emotion_label=emotion_result
		# emotion_detected= self.ids.emoinput.txt
		# print(emotion_detected)
		#os.system('python C:/Users/hp/OneDrive/Desktop/MiniProject/Emotion-Detection-Using-Facial-Recognition/src/display.py')
	def on_enter(self, *args):
		self.callemotion()
		
class ScreenFive(Screen):
	def switch_screen(self):
		screen_manager.switch_to(ScreenOne(name ="screen_one"))

	pass

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))

class ScreenApp(App):
	def build(self):
		return screen_manager

if __name__ == "__main__":
	sample_app = ScreenApp()
	sample_app.run()
