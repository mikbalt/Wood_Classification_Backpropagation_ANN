import os
import numpy as np

from keras_preprocessing.image import load_img, img_to_array

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

def prediksi(model, fc_model, path_gambar):

        os.system('cls')

        gambar = load_img(path_gambar, target_size=target_size)
        gambar = img_to_array(gambar)
        gambar = gambar / 255
        gambar = np.expand_dims(gambar, axis=0)

        bottleneck_prediction = model.predict(gambar)

        prediksi = fc_model.predict_classes(bottleneck_prediction)
        
        label = label_dictionary[prediksi[0]]

        nama_file = os.path.basename(path_gambar)

        return nama_file, label

if __name__ == '__main__':
        main()

