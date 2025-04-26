import pandas as pd
import re
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('Day38/Game_of_Thrones_jon_snow_data.csv', names=['text'])

def clean_text(text):
    text = re.sub(r'^[A-Z/() ]*:', '', text)
    text = text.replace('\r', ' ').replace('\n', ' ').replace(':', ' ')
    text = re.sub(r'[^a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵýỷỹ\s]', '', text)
    text = text.lower()
    stopwords_custom = {'jon', 'snow'}
    words = [word for word in text.split() if word not in stopwords_custom]
    return ' '.join(words)

df['cleaned'] = df['text'].astype(str).apply(clean_text)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['cleaned']))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

img_mask = np.array(Image.open('Day38/jon-snow.jpg'))

wc_mask = WordCloud(background_color='white', mask=img_mask, contour_width=1, width=800, height=400).generate(' '.join(df['cleaned']))
plt.figure(figsize=(10, 5))
plt.imshow(wc_mask, interpolation='bilinear')
plt.axis('off')
plt.show()

