import cv2
import cv2.aruco as aruco
import numpy as np
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from libs.subs.read_data import Read

class CameraScreen(MDScreen):
    title = "camera"
    marker_id = ""

    def clear_camera(self):
        # Bersihkan widget kamera, lepaskan tangkapan, dan batalkan jadwal pembaruan video
        self.ids.box_camera.clear_widgets()
        self.capture.release()
        Clock.unschedule(self.video)
        self.marker_id = ""

    def on_back(self):
        # Kembali ke halaman utama, bersihkan kamera terlebih dahulu
        self.clear_camera()
        self.manager.current = "home_page"
        self.manager.transition.direction = "right"

    def on_start(self):
        # Atur kamera saat memulai layar
        layout = self.ids.box_camera
        self.image = Image()
        layout.add_widget(self.image)

        # Mulai mengambil gambar dari kamera
        self.capture = cv2.VideoCapture(1)
        # Muat gambar tambahan
        self.aug_dict = self.load_aug_image("data/augmented_file")

        # Jadwalkan fungsi pembaruan video
        self.video = Clock.schedule_interval(self.load_video, 1.0 / 30.0)

    def load_video(self, *args):
        # Muat bingkai video dari kamera dan prosesnya
        ret, frame = self.capture.read()

        # Temukan penanda ArUco di bingkai
        aruco_found = self.find_aruco_markers(frame)

        # Jika penanda ArUco ditemukan, perbesar bingkai
        if len(aruco_found[0]) > 0:
            for corners, ids in zip(aruco_found[0], aruco_found[1]):
                ids = int(ids)
                if ids in self.aug_dict:
                    self.marker_id = str(ids)
                    frame = self.aug_image(corners, ids, frame, self.aug_dict[ids])

        # Tampilkan bingkai yang diperbesar
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
        self.image.texture = texture

    def load_aug_image(self, path):
        # Muat gambar tambahan dari suatu path
        aug_dict = {}
        ids, _, pic = Read.read_data()
        for id in ids:
            id = int(id)
            img_aug = cv2.imread(f"{path}/{pic[id]}")
            aug_dict[id] = img_aug
        return aug_dict

    def find_aruco_markers(self, frame):
        # Temukan penanda ArUco di bingkai yang diberikan
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
        detec_param = aruco.DetectorParameters()
        detec = aruco.ArucoDetector(aruco_dict, detec_param)
        corners, ids, _ = detec.detectMarkers(img_gray)

        return [corners, ids]

    def aug_image(self, corners, ids, frame, img_aug):
        # Perbesar bingkai dengan gambar yang diberikan berdasarkan sudut penanda ArUco
        marker_corners = corners[0][0]

        corners = corners.reshape((4, 2))
        (top_left, top_right, bottom_right, bottom_left) = corners

        tr = (int(top_right[0]), int(top_right[1]))
        br = (int(bottom_right[0]), int(bottom_right[1]))
        bl = (int(bottom_left[0]), int(bottom_left[1]))
        tl = (int(top_left[0]), int(top_left[1]))

        h, w, _ = img_aug.shape

        pts_marker = np.array([tl, tr, br, bl])
        pts_overlay = np.float32([[0, 0], [w, 0], [w, h], [0, h]])

        matrix, _ = cv2.findHomography(pts_overlay, pts_marker)
        wraped = cv2.warpPerspective(img_aug, matrix, (frame.shape[1], frame.shape[0]))

        cv2.fillConvexPoly(frame, pts_marker.astype(int), (0, 0, 0))

        img_output = frame + wraped

        return img_output

    def klik(self):
        # Jika ID penanda ada, navigasikan ke layar item yang sesuai
        if self.marker_id:
            _, title, _ = Read.read_data()
            title_temp = title[int(self.marker_id)].lower().replace(" ", "_")
            
            screen_name = f"item_{title_temp}"
            if screen_name in self.manager.screen_names:
                self.manager.get_screen(screen_name).from_camera = True
                self.manager.current = screen_name
