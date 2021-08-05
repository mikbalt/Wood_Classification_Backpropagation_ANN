import os
import numpy as np
import cv2

from keras.preprocessing.image import load_img, img_to_array
from keras.applications.xception import Xception
from keras.models import Sequential
from keras.layers import Dense, Flatten, GlobalAveragePooling2D

from sklearn.externals import joblib
from skimage.feature import hog

jumlah_kelas = 5

batch_size = 20

target_size = (299,299)

label_dictionary = {
        0 : 'I',
        1 : 'II',
        2 : 'III',
        3 : 'IV',
        4 : 'V'
}

def eks_hog(gambar):

    gambar = cv2.resize(gambar, (60,60))

    eks_ciri = hog(gambar, orientations=8, pixels_per_cell=(6, 6), cells_per_block=(6, 6), visualize=False, multichannel=True)
    
    eks_ciri = np.array(eks_ciri).astype('float')

    return eks_ciri

def meload_model():

    model = Xception(include_top=False, weights='imagenet')

    fc_model = Sequential()
    fc_model.add(GlobalAveragePooling2D(input_shape=(10,10,2048)))
    fc_model.add(Dense(5, activation='sigmoid'))

    clf = joblib.load("model/saved_model.pkl")

    return model, fc_model, clf

def prediksi(model, fc_model, path_gambar):

    os.system('cls')

    gambar = load_img(path_gambar, target_size=target_size)
    gambar = img_to_array(gambar)
    gambar = gambar / 255
    gambar = np.expand_dims(gambar, axis=0)

    bottleneck_prediction = model.predict(gambar)

    prediksi = fc_model.predict_classes(bottleneck_prediction)

    probabilitas = fc_model.predict(bottleneck_prediction)
        
    label = label_dictionary[prediksi[0]]

    nama_file = os.path.basename(path_gambar)

    return nama_file, label, probabilitas

def prediksi_ann(clf, path_gambar):

    os.system('cls')

    gambar_hog = cv2.imread(path_gambar)

    eks_ciri_prediksi = np.array(eks_hog(gambar_hog)).reshape(1,-1)

    prediksi = clf.predict(eks_ciri_prediksi)

    label = label_dictionary[prediksi[0]]

    probabilitas = clf.predict_proba(eks_ciri_prediksi)

    nama_file = os.path.basename(path_gambar)

    return nama_file, label, probabilitas