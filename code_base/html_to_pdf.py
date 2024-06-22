import time
import subprocess
from gcp_activities import upload_file_to_gcs

js_content = """
const puppeteer = require('puppeteer');

// Get the URL and filename from command-line arguments
const url = process.argv[2];
const filename = process.argv[3];

if (!url || !filename) {
  console.error('Please provide a URL as the first argument and a filename as the second argument');
  process.exit(1);
}

(async() => {
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });
    await page.pdf({ path: filename, format: 'A4', printBackground: true });

    await browser.close();
})();
"""

temp_path = "/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/code_base/logs/generate-pdf.js'"
print("Creating JavaScript file...")
with open(temp_path, 'w') as file:
    file.write(js_content)

# Step 4: Define the URL and Generate a Timestamped Filename
url = 'https://storage.googleapis.com/pika_image_uploads/play_list_htmls/viewer_pdf_20240622_061707.html'
timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = f'/Users/sathishkumar/Documents/Pickachooz/gitworkspace/pika-playlist-greeting/code_base/logs/webpage_{timestamp}.pdf'

# Step 5: Run the JavaScript File with the URL and Filename Parameters
print(f"Running JavaScript file with URL: {url} and filename: {filename}...")
subprocess.run(['node', temp_path, url, filename], check=True)

print(f"PDF generated: {filename}")

bucket_name="pika_image_uploads"
destination_subfolder = "play_list_htmls/"
upload_file_to_gcs(bucket_name, filename, destination_subfolder=destination_subfolder)