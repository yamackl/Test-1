meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek"
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict)
else:
    print("Bu kelime sözlükte bulunmamaktadır")
