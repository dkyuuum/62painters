import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2 as cv
import numpy as np
#디자이너에서 만든 UI파일을 사용할 수 있도록 준비
#form_class = uic.loadUiType("\\".join([os.path.dirname(os.path.abspath(__file__)), "main.ui"]))[0]
base_path = Path(__file__)
form_path = (base_path / "../main.ui").resolve()
form_class = uic.loadUiType(form_path)[0]
class MyApp(QMainWindow, form_class):
#62개의 알파벳과 숫자(A~Z,a~z,0~9) 문자를 gray 값으로 바꾸기 위한 배열 변수~
#문자의 생김새를 보고 글자 표현에 사용된 입자가 조밀한 정도에 따라 "어두운"<->"밝은"의 순서로 256개의 문자 배열를 결정
#--알고리즘 수정:진행하면서 모든 알파벳을 사용해서 명암을 표현하니 그림이 조잡해 보여서 수많은 조합과 테스트 끝에 특정한 문자로만 표현하기로 변경함
#--변환시 표현력: 너무 복잡한 풍경사진은 변환에 적합하지 않고 인물화나 단순한 물건 등의 변환 시 표현력이 좋음
#--향상시킬 점: 텍스트로 표현하다보니 문자간격보다 행간격이 더 넓어서 Y축으로 길게 표시 되면서 그림을 세밀하게 표현할 수 없는 문제 발생
image_chars = [
"8","8","8","8","8","8","8","8","8","8",
"8","8","8","8","8","8","8","8","8","8",
"8","8","8","8","8","8","8","8","8","8",
"8","8","M","M","M","M","M","M","M","M",
"M","M","M","M","M","M","M","M","M","M",
"M","M","M","M","M","M","M","M","M","M",
"M","M","M","M","N","N","N","N","N","N",
"N","N","N","N","N","N","N","N","N","N",
"N","N","N","N","N","N","N","N","N","N",
"N","N","N","N","N","N","B","B","B","B",
"B","B","B","B","B","B","B","B","B","B",
"B","B","B","B","B","B","B","B","B","B",
"B","B","B","B","B","B","B","B","C","C",
"C","C","C","C","C","C","C","C","C","C",
"C","C","C","C","C","C","C","C","C","C",
"C","C","C","C","C","C","C","C","C","C",
"3","3","3","3","3","3","3","3","3","3",
"3","3","3","3","3","3","3","3","3","3",
"3","3","3","3","3","3","3","3","3","3",
"3","3","7","7","7","7","7","7","7","7",
"7","7","7","7","7","7","7","7","7","7",
"7","7","7","7","7","7","7","7","7","7",

"7","7","7","7","L","L","L","L","L","L",
"L","L","L","L","L","L","L","L","L","L",
"L","L","L","L","L","L","L","L","L","L",
"L","L","L","L","L","L"
]
color_width = 200
color_height = 200
gray_width = 100
gray_height = 100
#프로그램 실행에 필요한 초기화
def __init__(self):
#파이썬 클래스 초기화
super().__init__()
#주 화면을 생성
self.setupUi(self)
#버튼 클릭 이벤트 함수 연결
self.cmdSelectFile.clicked.connect(self.cmdSelectFile_clicked)
self.cmdRefreshImage.clicked.connect(self.cmdRefreshImage_clicked)
self.cmdGenerateCharImage.clicked.connect(self.cmdGenerateCharImage_clicked)
#사진파일 선택 버튼이 눌렸을 때
def cmdSelectFile_clicked(self):
Tk().withdraw()
filename = askopenfilename()
self.textSelectedFile.setPlainText(filename)
self.show_frame_in_display(filename);
#사진 새로고침 버튼이 눌렸을 때
def cmdRefreshImage_clicked(self):
image_path = self.textSelectedFile.toPlainText()
self.show_frame_in_display(image_path);
#문자이미지 생성 버튼이 눌렸을 때
def cmdGenerateCharImage_clicked(self):
image_path = self.textSelectedFile.toPlainText()
self.show_charimage_in_display(image_path);
#원본이미지 표시
def show_frame_in_display(self,image_path):
#열려 있는 윈도우를 닫고
cv.destroyWindow("source")
#새로운 이미지 창을 열기
if os.path.isfile(image_path):
n = np.fromfile(image_path, np.uint8)
img = cv.imdecode(n, cv.IMREAD_COLOR)
dst = cv.resize(img, dsize=(self.color_width, self.color_height), fx=1.0, fy=1.0, interpolation=cv.INTER_AREA)
cv.namedWindow("source", cv.WINDOW_NORMAL)

cv.resizeWindow("source", self.color_width, self.color_height)
cv.imshow("source", dst);
#문자이미지 표시
def show_charimage_in_display(self,image_path):
#문자이미지 표시 부분을 정리하고
self.plainTextEdit.setPlainText("");
#열려 있는 gray 이미지 창이 있으면 닫고
cv.destroyWindow("gray")
#파일이 정말 있는지 검사하고
if os.path.isfile(image_path):
n = np.fromfile(image_path, np.uint8)
img = cv.imdecode(n, cv.IMREAD_COLOR)
dst = cv.resize(img, dsize=(self.gray_width, self.gray_height), fx=1.0, fy=1.0, interpolation=cv.INTER_AREA)
height = dst.shape[0]
width = dst.shape[1]
#gray 이미지 색상값을 저장할 공간을 깨끗하게 비우고
img_gray = np.zeros((height, width), np.uint8)
img_char = np.zeros((800, 800), np.uint8)
for y in range(0, height):
x_arr = []
for x in range(0, width):
#원본 이미지에서 픽셀의 색상값(R,G,B)을 얻고
b = dst.item(y, x, 0)
g = dst.item(y, x, 1)
r = dst.item(y, x, 2)
#평균값으로 gray 색상값을 얻고
gray = (int(b) + int(g) + int(r)) / 3.0
#gray 단계는 0~255이므로 만약 얻어진 gray 값이 255를 넘어가면 강제로 255로 맞추고
if gray > 255:
gray = 255
#gray 이미지 공간에 픽셀을 찍고
img_gray.itemset(y, x, gray)
#문자이미지를 위한 색상값을 배열에 추가하고
x_arr.append(gray)
#x좌표가 color 이미지의 가장 오른쪽에 도달했으면 현재 행을 처리하고 다음 행으로 이동하기 위해 x 루프 중단
if ((x + 1) >= width):
#gray 단계에 해당하는 문자 변환을 하고
tmp = self.print_rowstr_in_display(x_arr)
#화면에 표시
self.plainTextEdit.setPlainText(tmp)

break
#y좌표가 color 이미지의 제일 아래에 도달했으면 이미지의 모든 가로x세로 픽셀을 읽었으므로 y 루프 중단
if ((y+1) >= height):
break
#새로운 gray 이미지 창을 열기
cv.namedWindow("gray", cv.WINDOW_NORMAL)
cv.resizeWindow("gray", self.gray_width, self.gray_height)
cv.imshow("gray", img_gray)
#gray 이미지의 한 줄을 넘겨 받아서 gray 단계에 맞는 문자를 결정
def print_rowstr_in_display(self, row):
tmp = self.plainTextEdit.toPlainText()
tmp = tmp + "\r\n"
#배열을 전부 확인해서 gray 값에 해당하는 문자를 얻어 tmp에 더하고
for c in row:
tmp = tmp + str(self.image_chars[int(c)])
#최종적인 gray 단계에 따라 문자로 변환된 한 줄을 돌려주고
return tmp;
#프로그램이 시작되는 곳
if __name__ == "__main__":
app = QApplication(sys.argv)
w = MyApp()
w.show()
app.exec_()
