import time

name = input("'Kim Milyoner Olmak İster'e hoş geldiniz. Lütfen adınızı girin: ")
print(f"Hoşgeldin, {name.title()}. Ödül şeması aşağıdaki gibidir: ")

questions = {
    "1. İbn Haldun'un bir eserinin adı da olan \"mukaddime\" kelimesi ne anlama gelir?": ["a- Çeviri",
                                                                                       "b- Ön söz",
                                                                                       "c- Kaynakça",
                                                                                       "d- Dipnot" ],
    "2. 1959'dan beri düzenlenen, lise öğrencilerinin yarıştığı Uluslararası Matematik Olimpiyatı'nda "
    "1991 ve 2010'da kopya çektiği şüphesiyle diskalifiye edilen ülke hangisidir?": ["a- Kuzey Kore",
                                                                                     "b- Hindistan",
                                                                                     "c- Venezuela",
                                                                                     "d- Pakistan"],
    "3. Aslında Harry Potter'ın bütün hikayesi teyzesinin evinde mutsuz bir hayat yaşayan yetim bir "
    "çocuğun hayallerinden ibaret gibi hikayenin orijinalinde olmayan yorumlar hangisine "
    "örnektir?": ["a- Fermi Paradoksu",
                  "b- Oyun Teorisi",
                  "c- Bilgi Kuramı",
                  "d- Hayran Teorisi"],
    "4. Hangisi sırasında Atatürk 40'lı yaşlarının başındaydı?": ["a- Trablusgarp Savaşı",
                                                               "b- 1. Balkan Savaşı",
                                                               "c- Cumhuriyetin İlanı",
                                                               "d- Hatay'ın Türkiye'ye katılması"],
    "5. \"Tarım\"la eş anlamlı olan hangisidir?": ["a- Bilim",
                                                "b- Felsefe",
                                                "c- Kültür",
                                                "d- Sanat"],
    "6. Hangi masa oyununu kazanabilmeniz için oyun tahtasında rakibinize ait olan tüm taşları toplamanız gerekir?":
    ["a- Tavla",
     "b- Dama",
     "c- Satranç",
     "d- Okey"],
    "7. Gırnata, Belensiye ve İşbıliye günümüzde hangi ülkenin sınırları içinde yer alan şehirlerin eski adlarıdır?":
    ["a- Türkiye",
     "b- Bulgaristan",
     "c- İspanya",
     "d- Yunanistan"],
    "8. 1980'lere kadar hangi ülkedeki yetim, gayrimeşru doğmuş, ebeveyni alkolik, ayrılmış veya fakir olan çocuklar"
    "devlet tarafından bazen açık artırmada satılarak çiftliklerde zorla çalıştırılmıştır?": ["a- Danimarka",
                                                                                              "b- Norveç",
                                                                                              "c- İsviçre",
                                                                                              "d- Belçika"]
}
answers = ["b", "a", "d", "c",  "c",  "b",  "c",  "c"]
print("Ödül şeması aşağıda verilmiştir:")
awards_to_questions = list()
for element in range(1, 9):

    if element < 5:
        print("{}................................. {}$".format(element, element * 1150)), time.sleep(0.7)
        awards_to_questions.append(element * 1150)
    else:
        print("{}................................. {}$".format(element, element * 2250)), time.sleep(0.7)
        awards_to_questions.append(element * 2250)

print("Cevabı olduğunu düşündüğünüz şıkkı giriniz. (Örn.: a)"), time.sleep(0.7)
print(awards_to_questions)
answers_index = 0
for question, option in questions.items():
    answer = input(f"{question}\n{option}\n"
                    f"Cevabınız: ")
    if answer == answers[answers_index]:
        answers_index += 1
        if answers_index == 6:
            choice = input("Şimdiki ödülle çıkmak için 'q', kalmak için 'k': ")
            if choice == 'q':
                if answers_index == 0:
                    print("Ödülünüz: 0$")
                else:
                    print(f"Ödülünüz: {awards_to_questions[answers_index - 1]}$")
                break
        if answers_index == len(answers):
            print("KAZANDINIZ"), time.sleep(0.7)
            print(f"ÖDÜLÜNÜZ: {awards_to_questions[answers_index - 1]}$")
            break
    else:
        print("Yanlış Cevap.")
        print("KAYBETTİNİZ")
        break
