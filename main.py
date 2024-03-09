from pathlib import Path

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

from libs.subs.camera_screen import CameraScreen


class HomePage(MDScreen):
    pass


class CameraPage(CameraScreen):
    pass


class LibraryScreen(MDScreen):
    title = "Library"


class HelpPage(MDScreen):
    pass


class DownloadMarkers(MDScreen):
    pass


class AboutPage(MDScreen):
    tentang = (
        "Aplikasi ini merupakan aplikasi pembelajaran komponen distribusi "
        "berbasis augmented reality dibuat menggunakan bahasa pemograman python. "
        "Aplikasi ini dibuat untuk memenuhi laporan Praktik Kerja Lapangan di UP3 Mataram"
    )
    developer = (
        "Mauliddin Nur Muhammad\n"
        "Jurusan Teknik Elektro\n"
        "Universitas Mataram"
    )


class PageManager(MDScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        Window.size = (600, 600)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        kv_paths = ["libs/kv/item/", "libs/kv/menu/"]
        for kv_path in kv_paths:
            kv_files = Path(kv_path).glob("*.kv")
            for kv_file in kv_files:
                Builder.load_file(str(kv_file))

        return Builder.load_file("main.kv")

    # fungsi untuk pindah screen
    def call(self, screen_name, direc="left"):
        self.root.current = screen_name
        self.root.transition.direction = direc


if __name__ == "__main__":
    MainApp().run()
