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
        
        .section-1 .song-name {
            /* styles for song in section ${song_1}  */
        }
        
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
            /* styles for song in section  */
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
        
        .section-5 .song-name {
            /* styles for song in section  */
        }
        
        .section-5 .message {
            /* styles for message in section  */
        }
        
        .section-6 .lyrics {
            /* styles for lyrics in section  */
            column-count: 1;
            width: 70%;
            padding-left: 15%;
        }
        
        .section-7 .song-name {
            /* styles for song in section  */
        }
        
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
        
        .section-9 .song-name {
            /* styles for song in section  */
        }
        
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


flipbook_viewer=Template("""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
                body {
                font-family: "Poppin", sans-serif;
                background-color: #2e3537;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .book {
                width: 350px;
                height: 450px;
                position: relative;
                transition-duration: 1s;
                perspective: 1500px;
            }

            input {
                display: none;
            }

            .cover,
            .back-cover {
                background-color: #4173a5;
                width: 100%;
                height: 100%;
                border-radius: 0 15px 15px 0;
                box-shadow: 0 0 5px rgb(41, 41, 41);
                display: flex;
                align-items: center;
                justify-content: center;
                transform-origin: center left;
            }

            .cover {
                position: absolute;
                z-index: 8;
                transition: transform 1s;
            }

            .cover label {
                width: 100%;
                height: 100%;
                cursor: pointer;
            }

            .back-cover {
                position: relative;
                z-index: -1;
            }

            .page {
                position: absolute;
                background-color: white;
                width: 330px;
                height: 430px;
                border-radius: 0 15px 15px 0;
                margin-top: 10px;
                transform-origin: left;
                transform-style: preserve-3d;
                transform: rotateY(0deg);
                transition-duration: 1.5s;
            }

            .page img {
                width: 100%;
                height: 100%;
                border-radius: 15px 0 0 15px;
            }

            .front-page {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                box-sizing: border-box;
                /* padding: 1rem; */
            }

            .back-page {
                transform: rotateY(180deg);
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                z-index: 99;
            }

            .next,
            .prev {
                position: absolute;
                bottom: 1em;
                cursor: pointer;
            }

            .next {
                right: 1em;
            }

            .prev {
                left: 1em;
            }

            #page1 {
                z-index: 7;
            }

            #page2 {
                z-index: 6;
            }

            #page3 {
                z-index: 5;
            }

            #page4 {
                z-index: 4;
            }

            #page5 {
                z-index: 3;
            }

            #page6 {
                z-index: 2;
            }

            #page7 {
                z-index: 1;
            }

            #checkbox-cover:checked~.book {
                transform: translateX(200px);
            }

            #checkbox-cover:checked~.book .cover {
                transition: transform 1.5s, z-index 0.5s 0.5s;
                transform: rotateY(-180deg);
                z-index: 1;
            }

            #checkbox-cover:checked~.book .page {
                box-shadow: 0 0 3px rgb(99, 98, 98);
            }

            #checkbox-page1:checked~.book #page1 {
                transform: rotateY(-180deg);
                z-index: 8;
            }

            #checkbox-page2:checked~.book #page2 {
                transform: rotateY(-180deg);
                z-index: 9;
            }

            #checkbox-page3:checked~.book #page3 {
                transform: rotateY(-180deg);
                z-index: 10;
            }

            #checkbox-page4:checked~.book #page4 {
                transform: rotateY(-180deg);
                z-index: 11;
            }

            #checkbox-page5:checked~.book #page5 {
                transform: rotateY(-180deg);
                z-index: 12;
            }

            #checkbox-page6:checked~.book #page6 {
                transform: rotateY(-180deg);
                z-index: 13;
            }

            #checkbox-page7:checked~.book #page7 {
                transform: rotateY(-180deg);
                z-index: 14;
            }
    </style>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <title>Song Book</title>
</head>

<body>
    <input type="checkbox" id="checkbox-cover">
    <input type="checkbox" id="checkbox-page1">
    <input type="checkbox" id="checkbox-page2">
    <input type="checkbox" id="checkbox-page3">
    <input type="checkbox" id="checkbox-page4">
    <input type="checkbox" id="checkbox-page5">
    <input type="checkbox" id="checkbox-page6">
    <input type="checkbox" id="checkbox-page7">
    <div class="book">
        <div class="cover" style="background-image: url('${cover_page}')">
            <label for="checkbox-cover"></label>
        </div>
        <div class="page" id="page1">
            <div class="front-page">
                <img src="https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/first_page.jpeg">
                <label class="next" for="checkbox-page1"><i class="fas fa-chevron-right"></i></label>
            </div>
            <div class="back-page">
                <img src="${page1_right}">
                <label class="prev" for="checkbox-page1"><i class="fas fa-chevron-left"></i></label>
            </div>
        </div>
        <div class="page" id="page2">
            <div class="front-page">
                <img src="${page2_left}">
                <label class="next" for="checkbox-page2"><i class="fas fa-chevron-right"></i></label>
            </div>
            <div class="back-page">
                <img src="${page2_right}">
                <label class="prev" for="checkbox-page2"><i class="fas fa-chevron-left"></i></label>
            </div>
        </div>
        <div class="page" id="page3">
            <div class="front-page">
                <img src="${page3_left}">
                <label class="next" for="checkbox-page3"><i class="fas fa-chevron-right"></i></label>
            </div>
            <div class="back-page">
                <img src="${page3_right}">
                <label class="prev" for="checkbox-page3"><i class="fas fa-chevron-left"></i></label>
            </div>
        </div>
        <div class="page" id="page4">
            <div class="front-page">
                <img src="${page4_left}">
                <label class="next" for="checkbox-page4"><i class="fas fa-chevron-right"></i></label>
            </div>
            <div class="back-page">
                <img src="${page4_right}">
                <label class="prev" for="checkbox-page4"><i class="fas fa-chevron-left"></i></label>
            </div>
        </div>
        <div class="page" id="page5">
            <div class="front-page">
                <img src="${page5_left}">
                <label class="next" for="checkbox-page5"><i class="fas fa-chevron-right"></i></label>
            </div>
            <div class="back-page">
                <img src="${page5_right}">
                <label class="prev" for="checkbox-page5"><i class="fas fa-chevron-left"></i></label>
            </div>
        </div>
        <div class="page" id="page6">
            <div class="front-page">
                <img src="${page6_left}">
                <label class="next" for="checkbox-page6"><i class="fas fa-chevron-right"></i></label>
            </div>
            <div class="back-page">
                <img src="${page6_right}">
                <label class="prev" for="checkbox-page6"><i class="fas fa-chevron-left"></i></label>
            </div>
        </div>
        <div class="page" id="page7">
            <div class="front-page">
                <img src="https://storage.googleapis.com/pika_image_uploads/pika_flip_book_imgs/last_page.jpeg">
            </div>
        </div>
        <div class="back-cover"></div>
    </div>
</body>
""")