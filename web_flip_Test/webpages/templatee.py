from string import Template

# Define your HTML template using string.Template
viewer_pdf = Template("""<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia&effect=neon|outline|emboss|shadow-multiple">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tangerine">
    <link href='https://fonts.googleapis.com/css?family=Dancing Script' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=Marck Script' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=Great Vibes' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=Sacramento' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=Parisienne' rel='stylesheet'>
    <title>Webpage with Sections</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');
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
            width: 21cm;
            height: 29.7cm;
            background-size: contain;
            /* display: flex; */
            align-items: center;
            justify-content: center;
            background-position: top;
            display: block;
            margin: 0 auto;
            /* margin-bottom: 0.5cm; */
            box-shadow: 0 0 0.5cm rgba(0, 0, 0, 0.5);
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
        
         .song-name {
            font-size: 4.5em;
            font-weight: bold;
            letter-spacing: 2px;
            /* background: rgba(255, 255, 255, 0.21); */
            padding: 50px;
            border-radius: 8px;
            /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); */
            text-align: center;
            font-family: 'Dancing Script', 'Tangerine', 'Lobster';
        }
        
        .message {
            font-size: 30px;
            font-weight: bold;
            letter-spacing: 2px;
            /* background: rgba(255, 255, 255, 0.21); */
            /* padding-top: 30%; */
            padding-left: 30%;
            padding-right: 30%;
            border-radius: 8px;
            /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); */
            text-align: center;
            font-family: 'Marck Script';
        }
        
        .lyrics {
            width: 96%;
            font-size: 30px;
            /* font-weight: bold; */
            letter-spacing: 1px;
            /* background: rgba(255, 255, 255, 0.21); */
            padding-top: 10%;
            padding-left: 2%;
            /* padding-right: 30%; */
            border-radius: 8px;
            /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); */
            text-align: center;
            font-family: 'Bad Script', 'Parisienne', 'Sacramento';
            column-count: 2;
            /* text-shadow: 2px 2px rgb(255, 255, 255); */
        }
        /* Specific styles for each section */
        
        .section-1 .song-name {}
        
        .section-1 .message {
            /* styles for message in section  */
        }
        
        .section-2 .lyrics {
            font-size: 21px;
            color: rgb(255, 255, 255);
            /* text-shadow: black; */
            /* color: black; */
            text-shadow: 2px 2px rgb(0, 0, 0);
        }
        
        .section-3 .song-name {
            padding-top: 15%;
        }
        
        .section-3 .message {
            width: 60%;
            padding-left: 20%;
            padding-top: 20%;
        }
        
        .section-4 .lyrics {
            font-size: 22px;
            width: 96%;
            padding-left: 2%;
            text-shadow: 2px 2px rgb(209, 205, 205);
            /* background: rgba(255, 255, 255, 0.21); */
            font-weight: 400;
        }
        
        .section-5 .song-name {}
        
        .section-5 .message {
            /* styles for message in section  */
        }
        
        .section-6 .lyrics {
            /* styles for lyrics in section  */
            column-count: 1;
            width: 70%;
            padding-left: 15%;
        }
        
        .section-7 .song-name {}
        
        .section-7 .message {
            /* styles for message in section  */
        }
        
        .section-8 .lyrics {
            font-size: 20px;
            width: 96%;
            padding-left: 2%;
            color: rgb(255, 255, 255);
            /* text-shadow: 2px 2px rgb(255, 255, 255); */
            /* background: rgba(255, 255, 255, 0.21); */
            font-weight: 400;
        }
        
        .section-9 .song-name {}
        
        .section-9 .message {
            /* styles for message in section  */
        }
        
        .section-10 .lyrics {
            column-count: 1;
            width: 80%;
            padding-left: 10%;
            color: rgb(255, 255, 255);
        }
    </style>
</head>

<body>
    <div class="section section-1">
        <div class="song-name font-effect-shadow-multiple">${song_1}</div>
        <div class="message font-effect-outline">${message1}</div>
    </div>
    <div class="section section-2">
        <div class="lyrics">${lyrics1}</div>
    </div>
    <div class="section section-3">
        <div class="song-name font-effect-shadow-multiple">${song_2}</div>
        <div class="message font-effect-outline">${message2}</div>
    </div>
    <div class="section section-4">
        <div class="lyrics">${lyrics2}</div>
    </div>
    <div class="section section-5">
        <div class="song-name font-effect-shadow-multiple">${song_3}</div>
        <div class="message font-effect-outline">${message3}</div>
    </div>
    <div class="section section-6">
        <div class="lyrics">${lyrics3}</div>
    </div>
    <div class="section section-7">
        <div class="song-name font-effect-shadow-multiple">${song_4}</div>
        <div class="message font-effect-outline">${message4}</div>
    </div>
    <div class="section section-8">
        <div class="lyrics">${lyrics4}</div>
    </div>
    <div class="section section-9">
        <div class="song-name font-effect-shadow-multiple">${song_5}</div>
        <div class="message font-effect-outline">${message5}</div>
    </div>
    <div class="section section-10">
        <div class="lyrics">${lyrics5}</div>
    </div>
</body>

</html>
""")
