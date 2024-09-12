const puppeteer = require('puppeteer');
const path = require('path');
const { createInterface } = require('readline');
const fs =require('fs')

const pathToFile = path.join("urls.txt");

(async () => {
  const browser = await puppeteer.launch();

  const fileStream = fs.createReadStream(pathToFile);
  const rl = createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  for await (const url of rl) {
    
    await page.goto(url);
    await page.screenshot({path: 'path.png', fullPage: true});
    await browser.close();
  }
  const page = await browser.newPage();
})().catch(console.error);