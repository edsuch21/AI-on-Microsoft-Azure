import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from os import listdir

headers = {
    'Content-Type': 'application/octet-stream',
    'Prediction-Key': '7f48f95e05f84050a8a2ef4e815dd7ad',
}

test_dir = "/home/edsuch21/Documents/studia/Azure/vision/projekt/data_proj/ja/test"

score_ja = 0
score_tata = 0
score_mama = 0
try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    for filename in listdir(test_dir):
        with open(test_dir + '/' + filename, "rb") as image:
            f = image.read()
            body = bytearray(f)
            conn.request("POST", "/customvision/v3.0/Prediction/d283b29a-f351-424e-b1c6-3fa626554b3e/classify/iterations/Final_Model/image", body, headers)
            response = conn.getresponse()
            data = response.read()
            text = data.decode('utf8').replace("'", '"')
            jsonFile = json.loads(text)
            for data in jsonFile["predictions"]:
                if data["tagName"] == "mama":
                    score_mama += data["probability"]
                if data["tagName"] == "tata":
                    score_tata += data["probability"]
                if data["tagName"] == "ja":
                    score_ja += data["probability"]
    conn.close()
    score_ja /= len(listdir(test_dir))
    score_mama /= len(listdir(test_dir))
    score_tata /= len(listdir(test_dir))

    if score_ja == max(score_mama, score_tata, score_ja) and score_ja > 0.8:
        print("To jest pismo klasy 'ja'")
    elif score_mama == max(score_mama, score_tata, score_ja) and score_mama > 0.8:
        print("To jest pismo klasy 'mama'")
    elif score_tata == max(score_mama, score_tata, score_ja) and score_tata > 0.8:
        print("To jest pismo klasy 'tata'")
    else:
        print("Nie rozpoznano czyj to charakter pisma")
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))