from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.utils import platform
import os

class MaelSpeedApp(App):
    def build(self):
        # Minta izin storage khusus Android
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

        root = FloatLayout()

        # Panggil foto dari folder assets
        bg_path = os.path.join('assets', 'background.jpg')
        if os.path.exists(bg_path):
            bg = Image(source=bg_path, allow_stretch=True, keep_ratio=False)
            root.add_widget(bg)

        # UI Overlay
        ui = BoxLayout(orientation='vertical', padding=40, spacing=20)
        ui.add_widget(Label(text="MAEL-SPEED V3", font_size='30sp', color=(0, 1, 0, 1), bold=True))
        
        self.url = TextInput(hint_text="Tempel Link Video...", size_hint_y=None, height='50dp', background_color=(0,0,0,0.5), foreground_color=(0,1,0,1))
        ui.add_widget(self.url)
        
        btn = Button(text="GAS DOWNLOAD", size_hint_y=None, height='60dp', background_color=(0, 0.7, 0, 1))
        ui.add_widget(btn)

        root.add_widget(ui)
        return root

if __name__ == '__main__':
    MaelSpeedApp().run()
