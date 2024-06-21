const puppeteer = require('puppeteer');

(async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://127.0.0.1:5000/pdff', { waitUntil: 'networkidle2' });
    await page.pdf({ path: 'webpage.pdf', format: 'A4', printBackground: true });

    await browser.close();
})();