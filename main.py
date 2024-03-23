import sys
from PySide6.QtWidgets import QApplication
from cnocr import CnOcr
DEBUG = False
if DEBUG is False:
    import util.cap as cap
from ui.login_ui import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow(cap.Camera() if DEBUG is False else None, CnOcr(
        rec_model_name='number-densenet_lite_136-fc',
        det_model_name='en_PP-OCRv3_det',
        cand_alphabet='0123456789'))
    if login_window.detect_cfg_existence():
        login_window.token_check()
    else:
        login_window.show()

    sys.exit(app.exec())
    