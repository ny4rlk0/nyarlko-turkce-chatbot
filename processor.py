import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import wikipedia as wiki
import datetime
wiki.set_lang("tr")

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('job_intents.json', encoding='utf-8').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.99
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    try:tag = ints[0]['intent']
    except:return "Bunu bilmiyorum."
    #Bir üst satırda wikipedia üzerinde sorduğu soruyu ara.
    else:
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            result="null"
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                return result
                break
komutlar_aciklamasi="""
wiki Aranacak Şey | wikipedia üzerinde arama başlatır ve sonucu size gösterir.
<br>
tarih | Size saat tarih bilgisini yollar.
"""
def chatbot_response(msg):#Kullanıcı girişi buradan geçiyor. msg= kullanıcı girişi.
    text=msg;text=text.lower()
    if text.startswith("komutlar"):
        return komutlar_aciklamasi
    elif text.startswith("wiki"):
        try:
            veri=text.split("wiki ")
            ozet=wiki.summary(veri[1])
            ozet=str(ozet)
        except:return f"Üzgünüm, [{msg}] Wikipedia içerisinde bulamadım!"
        else:return ozet
    elif text.startswith("saat") or text.startswith("tarih") or text.startswith("zaman") or text.startswith("gün") or text.startswith("ay") or text.startswith("yıl"):
        try:
            suanki_zaman = datetime.datetime.now()
            return suanki_zaman
        except:return "Zamanı alırken bir hata ile karşılaştım."
    #chikapediayı yazılımın içine entegre et.
    #Önce araştırsın sonra job_intents.json içine kaydetsin.
    #Daha sonrada kendisini tekrar inşa etsin. (python build.py)
    #Hazır olduğunda kendisini yeniden başlatsın.
    else:
        ints = predict_class(msg, model)
        res = getResponse(ints, intents)
        return res