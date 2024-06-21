import json
import templatee as templatee 
from datetime import datetime


out_html_path="/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/web_flip_Test/webpages/outs"

fat={
    "page_1": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_1.png",
    "page_2": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_2.png",
    "page_3": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_3.png",
    "page_4": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_4.png",
    "page_5": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_5.png",
    "page_6": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_6.png",
    "page_7": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_7.png",
    "page_8": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_8.png",
    "page_9": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_9.png",
    "page_10": "https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/20240621_204243_10.png"
}


fata = {
    'cover_page': "",
    'page1_right':fat['page_1'],
    'page2_left':fat['page_2'],
    'page2_right':fat['page_3'],
    'page3_left':fat['page_4'],
    'page3_right':fat['page_5'],
    'page4_left':fat['page_6'],
    'page4_right':fat['page_7'],
    'page5_left':fat['page_8'],
    'page5_right':fat['page_9'],
    'page6_left':fat['page_10'],
    'page6_right':""
}

html_str = templatee.flipbook_viewer.substitute(fata)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{out_html_path}/flip_page_{timestamp}.html"
with open(filename,'w') as f:
    f.writelines(html_str)

print(f"completed the load : {filename}")

