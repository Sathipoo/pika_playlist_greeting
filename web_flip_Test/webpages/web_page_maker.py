import json
import templatee as templatee 
from datetime import datetime

inp_fil="/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/web_flip_Test/webpages/input.json"

out_html_path="/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/web_flip_Test/webpages/outs"
with open(inp_fil,'r') as f:
    dat = json.load(f)



data = {
    'left1_url': dat[0]['left_img'],
    'right1_url': dat[0]['right_img'],
    'left2_url': dat[1]['left_img'],
    'right2_url': dat[1]['right_img'],
    'left3_url': dat[2]['left_img'],
    'right3_url': dat[2]['right_img'],
    'left4_url': dat[3]['left_img'],
    'right4_url': dat[3]['right_img'],
    'left5_url': dat[4]['left_img'],
    'right5_url': dat[4]['right_img'],
    'song_1': dat[0]['song'],
    'message1': dat[0]['message'],
    'lyrics1': dat[0].get('lyrics').replace("\n","<br>"),
    'song_2': dat[1]['song'],
    'message2': dat[1]['message'],
    'lyrics2': dat[1].get('lyrics').replace("\n","<br>"),
    'song_3': dat[2]['song'],
    'message3': dat[2]['message'],
    'lyrics3': dat[2].get('lyrics').replace("\n","<br>"),
    'song_4': dat[3]['song'],
    'message4': dat[3]['message'],
    'lyrics4': dat[3].get('lyrics').replace("\n","<br>"),
    'song_5': dat[4]['song'],
    'message5': dat[4]['message'],
    'lyrics5': dat[4].get('lyrics').replace("\n","<br>"),
}

html_str = templatee.viewer_pdf.substitute(data)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{out_html_path}/viewer_pdf_{timestamp}.html"
with open(filename,'w') as f:
    f.writelines(html_str)

print(f"completed the load : {filename}")

