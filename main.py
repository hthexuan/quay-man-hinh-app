from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import QLabel
from kivy.uix.spinner import Spinner

class ScreenRecorderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = QLabel(
            text='Ứng Dụng Quay Màn Hình & Scale', 
            font_size=20,
            halign='center'
        )
        layout.add_widget(self.label)
        
        self.spinner = Spinner(
            text='Chọn tỷ lệ khung hình',
            values=('9:16 (TikTok/Reels)', '16:9 (YouTube)'),
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.spinner)
        
        btn_start = Button(
            text='Bắt đầu xử lý',
            background_color=(0.1, 0.6, 0.2, 1),
            size_hint=(1, 0.2)
        )
        btn_start.bind(on_press=self.start_process)
        layout.add_widget(btn_start)
        
        return layout

    def start_process(self, instance):
        selected_ratio = self.spinner.text
        if selected_ratio == 'Chọn tỷ lệ khung hình':
            self.label.text = 'Vui lòng chọn tỷ lệ trước!'
        else:
            self.label.text = f'Đang thiết lập chuẩn: {selected_ratio}'

if __name__ == '__main__':
    ScreenRecorderApp().run() 
