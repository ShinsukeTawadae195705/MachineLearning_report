import cv2
import os

"""
scraping.pyにて取得した画像から、顔画像を切り出して保存
"""

cascade_path = "/Users/tdesu/myhobby/画像認識/lbpcascade_animeface/lbpcascade_animeface.xml" #フルパスでないとダメ
members = ["Ichika", "Nino", "Miku", "Yotsuba","Itsuki","All"] #各ヒロイン名
input_file = "/Users/tdesu/myhobby/画像認識/五等分の花嫁/figures" #フルパスでないとダメ
folders = os.listdir(input_file)
count = len(folders) #フォルダ内の画像枚数
digit = 6 #数字6桁で画像が保存されたので
picture_num = 1 #切り取った顔画像の枚数 & 画像保存する際の番号

#カスケード型分類器に使用する分類器のデータ（xmlファイル）を読み込み
cascade = cv2.CascadeClassifier(cascade_path)

def detect(i, filename, mem):
    num = "0"*(digit - len(str(i))) + str(i)
    image_picture = input_file + "/" + mem + "/" + num + ".jpg"
    img_g = cv2.imread(image_picture,0) #グレースケールに変換
    face_list = cascade.detectMultiScale(img_g, minSize=(10,10)) #minSizeが大きいと1枚の画像から複数人をカットできない

    if len(face_list) != 0:
        for x,y,w,h in face_list:
            face_cut = img_g[y:y+h, x:x+w]
            global picture_num
            cv2.imwrite("face_cut" + str(picture_num) + ".jpg", face_cut)
            picture_num += 1

for member in members:
    count = len(os.listdir(input_file + "/" + member)) #各フォルダの画像枚数を取得
    for i in range(1, count+1):
        detect(i, input_file, member)