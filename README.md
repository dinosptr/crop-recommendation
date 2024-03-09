# Pertanian
Pertanian presisi telah menghasilkan profil yang sangat tinggi dalam industri pertanian selama dekade terakhir. Meskipun demikian, lebih lanjut pengembangan teknologi diperlukan, khususnya di bidang sistem penginderaan dan pemetaan untuk menyediakan data spasial terkait pada tanaman, tanah dan faktor lingkungan. Pertanian presisi merupakan informasi yang sangat bermanfaat dan tidak dapat diwujudkan tanpa kemajuan besar dalam jaringan dan kekuatan pemrosesan komputer. Pertanian presisi, sebagai konsep pengelolaan tanaman, dapat memenuhi banyak peningkatan lingkungan, ekonomi, pasar dan tekanan publik pada pertanian yang subur[1].\
Pertanian presisi menggunakan pendekatan teknologi yang memungkinkan proses bisnis pertanian dapat berjalan sesuai kondisi, dimana hal itu memerlukan input dan teknik yang tepat sehingga tidak terjadi pemborosan sumberdaya. Pada akhirnya petani dapat melakukan tindakan budidaya yang tepat berdasarkan informasi yang mereka terima [2].
Untuk mengatasi masalah tersebut dibutuhkan sebuah prediksi yang dapat memprediksi jenis tanaman yang cocok untuk ditanam berdasarkan unsur unsur seperti nutrisi tanah, jumlah ph, kelembapan, temperatur dan juga jumlah curah hujan, sehingga para petani dapat melakukan budidaya yang tepat.
 1. [Implementing Precision Agriculture in the 21st Century](https://www.sciencedirect.com/science/article/abs/pii/S0021863400905778)
 2. [PERTANIAN PRESISI, CARA BERTANI CERDAS DI ERA INDUSTRI 4.0 Century](http://cybex.pertanian.go.id/artikel/74731/pertanian-presisi-cara-bertani-cerdas--di-era-industri-40/)
 

## Business Understanding

### Problem Statements
Diberikan sebuah input berupa fitur nutrisi tanah seperti NPK, kelembapan, temperature, jumlah ph, jumlah curah hujan. Kemudian output yang diharapkan adalah sebuah label tanaman. Rumusan masalahnya adalah bagaimana kita dapat mengklasifikasikan tanaman yang cocok untuk ditanam berdasarkan input fitur yang ada.

### Goals
* Dapat memprediksi jenis tanaman yang cocok untuk ditanam.
* Memudahkan Petani memilih tanaman yang akan ditanam.
* Membantu para petani dalam penggunaan sumber daya.

### Solution statements

Berdasarkan problem statements yang ada yaitu pengklasifikasian tanaman yang cocok untuk ditanam, saya menggunakan salah satu algoritma machine learning yaitu Support Vector Machine. .
- **Support Vector Machine**.  merupakan salah satu metode yang paling populer untuk machine learning saat ini. selain itu, SVM bertujuan menemukan hyperplane sebagai pemisah dari input-input. SVM bekerja dengan membuat sebuah bidang untuk memisahkan dua buah kelas atau lebih.

## Data Understanding
Pada projek ini, saya menggunakan dataset publik yang ada di Kaggle. Datasets ini dibuat dengan menambah kumpulan data curah hujan, iklim, dan data pupuk yang tersedia untuk India. Dataset ini berisikan 2200 baris dan juga memiliki 8 buah variable kolom.
 Variabel-variabel pada dataset sebagai berikut:
- N - rasio kandungan Nitrogen dalam tanah
- P - rasio kandungan Fosfor dalam tanah
- K - rasio kandungan Kalium dalam tanah
- suhu(temperature) - suhu dalam derajat Celcius
- kelembaban(humidity) - kelembaban relatif dalam %
- Kekuatan Hidrogen (ph) - nilai ph tanah
- curah hujan(rainfall) - curah hujan dalam mm

Berikut adalah link untuk mengunduh dataset: [crop-recommendation-dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset).
## Data Preparation
 

- Teknik Label Encoder
   Teknik ini diperlukan untuk membuat target label agar menjadi bilangan numerik dari  0 sampai n_classes-1, ini bertujuan agar mesin bisa menjalankan programnya, karena mesin tidak bisa mengolah data berupa kata. 
- Teknik train test split
  Teknik ini merupakan teknik membagi dataset antara data latih dan data uji, disini saya menerapkan 80% untuk data latih dan 20% untuk data uji.
- Teknik Standarisasi
  Standarisasi adalah sebuah proses konversi nilai-nilai dari suatu fitur sehingga nilai-nilai tersebut memiliki skala yang sama. Selain itu dengan menerapkan teknik ini akan lebih mengoptimalkan pengklasifikasian pada output.

## Modeling
Setelah melakukan tahap-tahap pra-proses data langkah selanjutnya adalah membuat model. Pada projek kali ini saya menggunakan algoritma Support Vector Machine (SVM) dengan parameternya seperti C, gamma, dan kernel sebagai algoritma modeling. Dalam proyek ini saya juga melakukan beberapa tunning seperti meningkatkan jumlah parameter C dan juga parameter gamma, disini juga saya menambahkan jenis kernel yaitu rbf, linear, sigmoid. Pada hasil akhirnya improvement baseline model memiliki hasil prediksi lebih baik dengan parameter C=100, gamma=0.05, kernel='rbf'. Berikut adalah performa berdasarkan akurasi antara baseline model dan improvement model:
1. Baseline model = 0.975 atau 97,5%
2. Improvement model = 0.986 atau 98,6%


## Evaluation
Evaluasi model yang digunakan untuk menilai performa prediksi pada projek kali ini adalah confusion metrik yang terdiri dari **accuracy, precision, recall, dan F1 score**.

- Confusion Matrix digunakan untuk melakukan perhitungan akurasi pada konsep data mining atau Sistem Pendukung Keputusan. Pada pengukuran kinerja menggunakan confusion matrix, terdapat 4 (empat) istilah sebagai representasi hasil proses klasifikasi. Keempat istilah tersebut adalah True Positive (TP), True Negative (TN), False Positive (FP) dan False Negative (FN).

- Accuracy adalah seberapa baik model kami dalam memprediksi kategori yang benar (kelas atau label). 
  - Accuracy = (TP+TN) / (TP+FP+FN+TN).
- Precision adalah rasio dari apa yang diprediksi model kita dengan benar dengan apa yang diprediksi oleh model kita. Untuk setiap kategori/kelas, ada satu nilai presisi. Rumus Precision adalah sebagai berikut.
    - Precision = (TP) / (TP + FP)
- Recall adalah rasio dari apa yang diprediksi model kami dengan benar dengan label sebenarnya. Mirip dengan presisi, untuk setiap kategori/kelas, ada satu nilai recall. Rumus recall adalah sebagai berikut.
    - Recall  = TP / (TP + FN)
- F1-score adalah cara menggabungkan presisi dan recall model, dan didefinisikan sebagai rata-rata harmonik presisi dan recall model. Rumus F1-score adalah sebagai berikut.
    - F-1 Score  = (2 * Recall * Precision) / (Recall + Precision)

- Berikut adalah hasil confusion matrix setiap class:
    a.  Model Baseline
        |   Class       |   TP |   FP |   FN |   TN |   Accuracy |   Precision |   Recall |   F1-Score |
|:--------------:|-----:|-----:|-----:|-----:|-----------:|------------:|---------:|-----------:|
|   apple        |   19 |    0 |    0 |  421 |      1.000 |       1.000 |    1.000 |      1.000 |
|   banana       |   21 |    0 |    0 |  419 |      1.000 |       1.000 |    1.000 |      1.000 |
|   blackgram    |   25 |    0 |    1 |  414 |      0.997 |       1.000 |    0.960 |      0.980 |
|   chickpea     |   20 |    0 |    0 |  420 |      1.000 |       1.000 |    1.000 |      1.000 |
|   coconut      |   23 |    0 |    0 |  417 |      1.000 |       1.000 |    1.000 |      1.000 |
|   coffee       |   24 |    0 |    0 |  416 |      1.000 |       1.000 |    1.000 |      1.000 |
|   cotton       |   19 |    1 |    0 |  420 |      0.997 |       0.950 |    1.000 |      0.970 |
|   grapes       |   20 |    0 |    0 |  420 |      1.000 |       1.000 |    1.000 |      1.000 |
|   jute         |   11 |    7 |    0 |  422 |      0.984 |       0.660 |    1.000 |      0.750 |
|   kidneybeans  |   23 |    0 |    0 |  417 |      1.000 |       1.000 |    1.000 |      1.000 |
|   lentil       |   21 |    1 |    1 |  417 |      0.995 |       0.910 |    1.000 |      0.950 |
|   maize        |   18 |    0 |    1 |  421 |      0.997 |       1.000 |    0.940 |      0.970 |
|   mango        |   14 |    0 |    0 |  426 |      1.000 |       1.000 |    1.000 |      1.000 |
|   mothbeans    |   18 |    0 |    1 |  421 |      0.997 |       1.000 |    0.940 |      0.970 |
|   mungbean     |   17 |    0 |    0 |  423 |      1.000 |       1.000 |    1.000 |      1.000 |
|   muskmelon    |   23 |    0 |    0 |  417 |      1.000 |       1.000 |    1.000 |      1.000 |
|   orange       |   14 |    0 |    0 |  426 |      1.000 |       1.000 |    1.000 |      1.000 |
|   papaya       |   20 |    0 |    3 |  417 |      0.993 |       1.000 |    0.860 |      0.930 |
|   pigeonpeas   |   27 |    0 |    0 |  413 |      1.000 |       1.000 |    1.000 |      1.000 |
|   pomegranate  |   17 |    0 |    0 |  423 |      1.000 |       1.000 |    1.000 |      1.000 |
|   rice         |   18 |    1 |    5 |  416 |      0.986 |       0.940 |    0.780 |      0.850 |
|   watermelon   |   17 |    0 |    0 |  423 |      1.000 |       1.000 |    1.000 |      1.000 |


    b.  Model Improvement
        1.apple = TP=19, FP=0, FN=0, TN=421. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        2.banana = TP=21, FP=0, FN=0, TN = 419. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        3. blackgram = TP=26, FP=0, FN=0, TN=414. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        4. chickpea = TP=20, FP=0, FN=0, TN=420. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        5. coconut = TP=23, FP=0, FN=0, TN = 417. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        6. coffee = TP=23, FP=0, FN=1, TN=416. Acc=0.997, Precision=1.0, Recall=0.95, F1-score = 0.97
        7. cotton = TP=19, FP=0, FN=0, TN=421. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        8. grapes = TP=20, FP=0, FN=0, TN=420. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        9. jute = TP=10, FP=5, FN=1, TN=424. Acc=0.986, Precision=0.667, Recall=0.90, F1-score = 0.76
        10. kidneybeans = TP=23, FP=0, FN=0, TN=417. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        11. lentil = TP=21, FP=0, FN=0, TN=419. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        12. maize = TP=19, FP=0, FN=0, TN=421. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        13. mango = TP=14, FP=0, FN=0, TN = 426. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        14. mothbeans = TP=19, FP=0, FN=0, TN=421. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        15. mungbean = TP=17, FP=0, FN=0, TN=423. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        16. muskmelon = TP=23, FP=0, FN=0, TN=417. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        17. orange = TP=14, FP=0, FN=0, TN=426. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        18. papaya = TP=23, FP=1, FN=0, TN=416. Acc=0.997, Precision=0.95, Recall=1.0, F1-score = 0.97
        19. pigeonpeas = TP=27, FP=0 FN=0, TN=413. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        20. pomegranate = TP=17, FP=0, FN=0, TN=423. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        21. rice = TP=19, FP=0, FN=4, TN=417. Acc=1.0, Precision=1.0, Recall=0.82, F1-score = 0.90
        22. watermelon = TP=17, FP=0, FN=0, TN=423. Acc=1.0, Precision=1.0, Recall=1.0, F1-score = 1.0
        
Berdasarkan hasil confusion matrix berdasarkan kelas diatas, model improvement memiliki hasil yang lebih baik, terlihat pada kelas blackgram, cotton, lentil, maize, mothbeans, jute, dan rice yang memiliki peningkatan pada accuracy, precision, recall dan juga f1-score. Akan tetapi terdapat satu kelas yang performanya menurun yaitu kelas coffe pada recall dan juga f1-score. Dengan hasil yang dijelaskan diatas terlihat bahwa perubahan pada tuning hyperparameter meningkatkan performa dalam suatu prediksi, maka dari itu penting untuk melakukan tuning hyperparameter pada sebuah model.

- Kelebihan Confusion Matrix:
    1. Penerapan dalam code mudah.
    2. Tabel yang dihasilkan mudah dipahami
    3. Tabel bervariasi
