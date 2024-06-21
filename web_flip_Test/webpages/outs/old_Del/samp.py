import json
from datetime import datetime
from string import Template

# Define your HTML template using string.Template
viewer_pdf = Template("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webpage with Sections</title>
    <style>
        body {
            display: flex;
            flex-wrap: wrap;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            align-items: center;
            justify-content: center;
        }
        
        .section {
            width: 8.27in;
            height: 8.27in;
            background-color: rgb(218, 218, 218);
            background-size: cover;
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
            padding: 20px;
        }
        
        .section-1 {
            background-image: url('${left1_url}');
        }
        
        .section-2 {
            background-image: url('${right1_url}');
        }
        
        .section-3 {
            background-image: url('${left2_url}');
        }
        
        .section-4 {
            background-image: url('${right2_url}');
        }
        
        .section-5 {
            background-image: url('${left3_url}');
        }
        
        .section-6 {
            background-image: url('${right3_url}');
        }
        
        .section-7 {
            background-image: url('${left4_url}');
        }
        
        .section-8 {
            background-image: url('${right4_url}');
        }
        
        .section-9 {
            background-image: url('${left5_url}');
        }
        
        .section-10 {
            background-image: url('${right5_url}');
        }
        
        .song-name,
        .message,
        .lyrics {
            background: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        /* Specific styles for each section */
        
        .section-1 .song-name, .section-3 .song-name, .section-5 .song-name, .section-7 .song-name, .section-9 .song-name {
            font-size: 1.5em;
            font-weight: bold;
            letter-spacing: 1px;
            position: absolute;
            top: 10%;
            left: 5%;
        }
    </style>
</head>

<body>
    <div class="section section-1">
        <div class="song-name">${song_1}</div>
        <div class="message">${message1}</div>
    </div>
    <div class="section section-2">
        <div class="lyrics">${lyrics1}</div>
    </div>
    <div class="section section-3">
        <div class="song-name">${song_2}</div>
        <div class="message">${message2}</div>
    </div>
    <div class="section section-4">
        <div class="lyrics">${lyrics2}</div>
    </div>
    <div class="section section-5">
        <div class="song-name">${song_3}</div>
        <div class="message">${message3}</div>
    </div>
    <div class="section section-6">
        <div class="lyrics">${lyrics3}</div>
    </div>
    <div class="section section-7">
        <div class="song-name">${song_4}</div>
        <div class="message">${message4}</div>
    </div>
    <div class="section section-8">
        <div class="lyrics">${lyrics4}</div>
    </div>
    <div class="section section-9">
        <div class="song-name">${song_5}</div>
        <div class="message">${message5}</div>
    </div>
    <div class="section section-10">
        <div class="lyrics">${lyrics5}</div>
    </div>
</body>

</html>
""")

# Define the input file path
inp_fil = "/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/web_flip_Test/webpages/input.json"

# Load the JSON data
with open(inp_fil, 'r') as f:
    dat = json.load(f)

# Define the output directory
out_html_path = "/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/web_flip_Test/webpages/outs"

# Get the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create the data dictionary for the template
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
    'lyrics1': dat[0].get('lyrics'),
    'song_2': dat[1]['song'],
    'message2': dat[1]['message'],
    'lyrics2': dat[1].get('lyrics'),
    'song_3': dat[2]['song'],
    'message3': dat[2]['message'],
    'lyrics3': dat[2].get('lyrics'),
    'song_4': dat[3]['song'],
    'message4': dat[3]['message'],
    'lyrics4': dat[3].get('lyrics'),
    'song_5': dat[4]['song'],
    'message5': dat[4]['message'],
    'lyrics5': dat[4].get('lyrics')
}

# Create the HTML content with formatted variables
html_str = viewer_pdf.substitute(data)

# Define the output filename with the timestamp
filename = f"{out_html_path}_{timestamp}.html"

# Write the HTML content to the file
with open(filename, 'w') as f:
    f.write(html_str)