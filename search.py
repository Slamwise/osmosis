import asyncio
from pyppeteer import launch

url1 = 'https://app.osmosis.zone/pools'

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url1)
    await page.screenshot({'path': 'osmosis.png'}, fullPage=True)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
quit()
import json
import cv2
import numpy as np
import csv
from PIL import Image

for i in range(pagequantity):                           #Generate the final cropped .jpg images to be sent to detection
  img = cv2.imread('searchimg/' + str(i) + 'r.png')
  height, width, channels = img.shape
  sections = int(height/7180+1)
  inpu = i
  current = 0
  interval = 7180
  for j in range(sections):
    crop_img = img[current:interval, 0:800]
    cv2.imwrite("cropped/{}{}r.png".format(inpu, j), crop_img)
    interval = interval + 7180
    current = current + 7180
    im1 = Image.open(r'C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering/cropped/' + str(inpu) + str(j) + 'r.png')
    im = im1.convert('RGB')
    im.save(r'C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering\cropped\crop_' + str(inpu) + str(j)  + '.jpg')
