const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://www.ebay.com/sch/i.html?_from=R40&_nkw=steph+curry+rookie+card&_sacat=0&LH_TitleDesc=0&_sop=13&LH_Complete=1&LH_Sold=1&_ipg=25');
    await page.screenshot({path: '00000013.png', fullPage: true});
    await browser.close();
})();