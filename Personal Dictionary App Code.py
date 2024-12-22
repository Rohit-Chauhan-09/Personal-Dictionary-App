from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from googletrans import Translator
from kivy.core.text import LabelBase

# font that supports Hindi
LabelBase.register(name='NotoSans', 
fn_regular=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.12\static\NotoSansDevanagari_Condensed-Black.ttf')

class MyApp(App):
    def build(self):
        self.translator = Translator()

        self.layout = FloatLayout()

        # Background Image
        self.img = Image(source=r"C:\Users\rohit\OneDrive\Desktop\Project Dictionary\Main Dictionary.png.png",
         allow_stretch=True, keep_ratio=True, size_hint=(1, 1.0),
          pos_hint={'center_x': 0.5, 'center_y': 0.50})
        self.layout.add_widget(self.img)

        # Input position on the image
        self.input = TextInput(hint_text='Enter an English word', multiline=False,
         size_hint=(0.2, 0.05),
         pos_hint={'center_x': 0.5, 'y': 0.46})
        self.layout.add_widget(self.input)

        # Button position on the image
        self.translate_button = Button(text='Translate', size_hint=(0.2, 0.06),
         pos_hint={'center_x': 0.5, 'y': 0.142})
        self.translate_button.bind(on_press=self.translate_word)
        self.layout.add_widget(self.translate_button)

        # Output position on the image and Font colour black
        self.output = Label(text='', font_name='NotoSans', font_size='20sp',
         color=(0, 0, 0, 1), size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'y': 0.21})
        self.layout.add_widget(self.output)

        return self.layout

    def translate_word(self, instance):
        english_word = self.input.text
        try:
            translation = self.translator.translate(english_word, src='en', dest='hi')
            print(f"Translated text: {translation.text}")  # Debugging print statement
            self.output.text = translation.text
        except Exception as e:
            print(f"Error: {e}")  # error messages
            self.output.text = "Translation error. Please try again."

if __name__ == '__main__':
    MyApp().run()
    