import os
import numpy as np

from keras.preprocessing.image import load_img, img_to_array
from keras_applications.xception import Xception
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from keras import backend as K

path_prediksi = os.path.join(os.getcwd(), "delapan_watt/tiga_puluh_derajat/lima_belas_centi")
jumlah_kelas = 5

batch_size = 22

target_size = (299,299)

label_dictionary = {
        0 : 'I',
        1 : 'II',
        2 : 'III',
        3 : 'IV',
        4 : 'V'
}

def prediksi(model, fc_model, path):

        os.system('cls')

        jumlah_gambar = len(os.listdir(path))

        jumlah_salah = 0

        jumlah_keprediksi_A = np.array([0,0,0,0])
        jumlah_keprediksi_B = np.array([0,0,0,0])
        jumlah_keprediksi_C = np.array([0,0,0,0])
        jumlah_keprediksi_D = np.array([0,0,0,0])
        jumlah_keprediksi_E = np.array([0,0,0,0])

        for image in os.listdir(path):
                gambar = load_img(os.path.join(path, image), target_size=target_size)
                gambar = img_to_array(gambar)
                gambar = gambar / 255
                gambar = np.expand_dims(gambar, axis=0)
                
                bottleneck_prediction = model.predict(gambar)
                
                prediksi = fc_model.predict_classes(bottleneck_prediction)
                
                label = label_dictionary[prediksi[0]]

                jumlah_keprediksi_A, jumlah_keprediksi_B, jumlah_keprediksi_C, jumlah_keprediksi_D, jumlah_keprediksi_E, jumlah_salah = pencocokan(
                        image, label, jumlah_salah, 
                        jumlah_keprediksi_A, 
                        jumlah_keprediksi_B, 
                        jumlah_keprediksi_C, 
                        jumlah_keprediksi_D, 
                        jumlah_keprediksi_E
                )
        
        print("\n\nKelas A yang keprediksi II\t= ", jumlah_keprediksi_A[0])
        print("\nKelas A yang keprediksi III\t= ", jumlah_keprediksi_A[1])
        print("\nKelas A yang keprediksi IV\t= ", jumlah_keprediksi_A[2])
        print("\nKelas A yang keprediksi V\t= ", jumlah_keprediksi_A[3])

        print("\n\nKelas B yang keprediksi I\t= ", jumlah_keprediksi_B[0])
        print("\nKelas B yang keprediksi III\t= ", jumlah_keprediksi_B[1])
        print("\nKelas B yang keprediksi IV\t= ", jumlah_keprediksi_B[2])
        print("\nKelas B yang keprediksi V\t= ", jumlah_keprediksi_B[3])
        
        print("\n\nKelas C yang keprediksi I\t= ", jumlah_keprediksi_C[0])
        print("\nKelas C yang keprediksi II\t= ", jumlah_keprediksi_C[1])
        print("\nKelas C yang keprediksi IV\t= ", jumlah_keprediksi_C[2])
        print("\nKelas C yang keprediksi V\t= ", jumlah_keprediksi_C[3])

        print("\n\nKelas D yang keprediksi I\t= ", jumlah_keprediksi_D[0])
        print("\nKelas D yang keprediksi II\t= ", jumlah_keprediksi_D[1])
        print("\nKelas D yang keprediksi III\t= ", jumlah_keprediksi_D[2])
        print("\nKelas D yang keprediksi V\t= ", jumlah_keprediksi_D[3])
        
        print("\n\nKelas E yang keprediksi I\t= ", jumlah_keprediksi_E[0])
        print("\nKelas E yang keprediksi II\t= ", jumlah_keprediksi_E[1])
        print("\nKelas E yang keprediksi III\t= ", jumlah_keprediksi_E[2])
        print("\nKelas E yang keprediksi IV\t= ", jumlah_keprediksi_E[3])

        print("\nJumlah gambar\t= ",jumlah_gambar)
        print("\nJumlah salah\t= ",jumlah_salah)
        print("\n\nNilai akurasi nyata\t= ",round( ( (jumlah_gambar - jumlah_salah) / jumlah_gambar)*100,2))

                

def pencocokan(file_gambar, label_prediksi, jumlah_salah, jumlah_keprediksi_A, jumlah_keprediksi_B, jumlah_keprediksi_C, jumlah_keprediksi_D, jumlah_keprediksi_E):

        if "A" in file_gambar:
                label_sesungguhnya = 'I'
        elif "B" in file_gambar:
                label_sesungguhnya = 'II'
        elif "C" in file_gambar:
                label_sesungguhnya = 'III'
        elif "D" in file_gambar:
                label_sesungguhnya = 'IV'
        elif "E" in file_gambar:
                label_sesungguhnya = 'V'

        if(label_prediksi != label_sesungguhnya):
                jumlah_salah += 1
                print("Gambar ",file_gambar," terdeteksi ",label_prediksi)
                if "A" in file_gambar:
                        if 'II' == label_prediksi:
                                jumlah_keprediksi_A[0] += 1
                        elif 'III' == label_prediksi:
                                jumlah_keprediksi_A[1] += 1
                        elif 'IV' == label_prediksi:
                                jumlah_keprediksi_A[2] += 1
                        elif 'V' == label_prediksi:
                                jumlah_keprediksi_A[3] += 1
                elif "B" in file_gambar:
                        if 'I' == label_prediksi:
                                jumlah_keprediksi_B[0] += 1
                        elif 'III' == label_prediksi:
                                jumlah_keprediksi_B[1] += 1
                        elif 'IV' == label_prediksi:
                                jumlah_keprediksi_B[2] += 1
                        elif 'V' == label_prediksi:
                                jumlah_keprediksi_B[3] += 1
                elif "C" in file_gambar:
                        if 'I' == label_prediksi:
                                jumlah_keprediksi_C[0] += 1
                        elif 'II' == label_prediksi:
                                jumlah_keprediksi_C[1] += 1
                        elif 'IV' == label_prediksi:
                                jumlah_keprediksi_C[2] += 1
                        elif 'V' == label_prediksi:
                                jumlah_keprediksi_C[3] += 1
                
                elif "D" in file_gambar:
                        if 'I' == label_prediksi:
                                jumlah_keprediksi_D[0] += 1
                        elif 'II' == label_prediksi:
                                jumlah_keprediksi_D[1] += 1
                        elif 'III' == label_prediksi:
                                jumlah_keprediksi_D[2] += 1
                        elif 'V' == label_prediksi:
                                jumlah_keprediksi_D[3] += 1
                elif "E" in file_gambar:
                        if 'I' == label_prediksi:
                                jumlah_keprediksi_E[0] += 1
                        elif 'II' == label_prediksi:
                                jumlah_keprediksi_E[1] += 1
                        elif 'III' == label_prediksi:
                                jumlah_keprediksi_E[2] += 1
                        elif 'IV' == label_prediksi:
                                jumlah_keprediksi_E[3] += 1

        return jumlah_keprediksi_A, jumlah_keprediksi_B, jumlah_keprediksi_C, jumlah_keprediksi_D, jumlah_keprediksi_E, jumlah_salah



def main():

        model = Xception(include_top=False, weights='imagenet')

        fc_model = Sequential()
        fc_model.add(GlobalAveragePooling2D(input_shape=(10,10,2048)))
        fc_model.add(Dense(jumlah_kelas, activation='softmax'))
        fc_model.load_weights("weights/fc_weights.hdf5")

        prediksi(model=model, fc_model=fc_model, path=path_prediksi)

if __name__ == '__main__':
        main()

