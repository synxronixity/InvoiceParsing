import sys
import pymupdf
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPainter, QImage, QPixmap

class PDFViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.page_item = None
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def setPage(self, pixmap):
        self.scene().clear()
        self.page_item = self.scene().addPixmap(pixmap)
        self.scene().setSceneRect(self.page_item.boundingRect())

    def currentZoom(self):
        return self.transform().m11()  # Return the current zoom level (scale factor)

    def ZoomBy(self, factor):
        new = max(MinZoom, min(MaxZoom, self.currentZoom() * factor))
        factor = new / self.currentZoom()
        self.scale(factor, factor)

RenderScale = 2.0  # Adjust the scale factor as needed

app = QApplication(sys.argv)
win = QMainWindow()
view = PDFViewer()
win.setCentralWidget(view)
win.resize(1100, 900)

path = r"C:\Users\lucasc\Documents\Invoices\ElGenio\FBTY_20261019_143542.pdf"
doc = pymupdf.open(path)
page = doc[0]
pix = page.get_pixmap(matrix=pymupdf.Matrix(RenderScale, RenderScale), alpha=False)
img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
view.setPage(QPixmap.fromImage(img))

win.show()
sys.exit(app.exec())



