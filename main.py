# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader

class MyButtonApp(App):

    def build(self):
        # Set window size and position
        Window.size = (400, 400)
        Window.top = 100
        Window.left = 100

        path = "Audio/"

        # Create root widget
        root_widget = FloatLayout()

        # Load and play the Faker.wav sound
        sound = SoundLoader.load("Audio/Applause.wav")
        if sound:
            sound.play()

        # Create button 1
        button1 = Button(text='Pass', size_hint=(None, None), size=(150, 50))
        button1.pos_hint = {'center_x': 0.3, 'center_y': 0.6}
        button1.bind(on_press=lambda args: self.playSound(path, "Pass.mp3"))
        root_widget.add_widget(button1)

        # Create button 2
        button2 = Button(text='Fail', size_hint=(None, None), size=(150, 50))
        button2.pos_hint = {'center_x': 0.7, 'center_y': 0.6}
        button2.bind(on_press=lambda args: self.playSound(path, "Fail.mp3"))
        root_widget.add_widget(button2)

        # Create button 3
        button3 = Button(text='Faker', size_hint=(None, None), size=(150, 50))
        button3.pos_hint = {'center_x': 0.3, 'center_y': 0.4}
        button3.bind(on_press=lambda args: self.playSound(path, "Applause.wav"))
        root_widget.add_widget(button3)

        return root_widget

    def playSound(self, path, file):
        sound = SoundLoader.load(path + file)
        sound.play()

if __name__ == '__main__':
    MyButtonApp().run()





# from kivy.app import App
# from kivy.uix.button import Button
# from playsound import playsound
#
# class AudioPlayerApp(App):
#     def build(self):
#         button = Button(text="Play")
#         button.bind(on_press=self.play_audio)
#         return button
#
#     def play_audio(self, instance):
#         audio_file = './Audio/Applause.wav'
#         playsound(audio_file)
#
# if __name__ == '__main__':
#     AudioPlayerApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
