import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
const browser=await chromium.launch({executablePath:process.env.PLAYWRIGHT_CHROMIUM_PATH});
await fs.mkdir('../qa/arena',{recursive:true});
for(const [w,h] of [[1586,992],[1280,800],[768,1024],[390,844]]){const page=await browser.newPage({viewport:{width:w,height:h},deviceScaleFactor:1,reducedMotion:'reduce',locale:'vi-VN'});await page.goto('http://localhost:5173/rooms/room-01?demo=playing');await page.evaluate(async()=>{await document.fonts.ready;await Promise.all(["/assets/table-render.png","/assets/cards/back-render-small.png"].map(src=>{const i=new Image();i.src=src;return i.decode()}));await Promise.all(["play","navy","violet"].map(name=>{const image=new Image();image.src=`/assets/buttons/${name}.png`;return image.decode()}));await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))});await page.screenshot({path:`../qa/arena/room-${w}.png`});console.log(w,await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,font:document.fonts.check('400 16px "Be Vietnam Pro"')})));await page.close()}
const page=await browser.newPage({viewport:{width:1586,height:992}});await page.goto('http://localhost:5173/ui-kit');await page.screenshot({path:'../qa/arena/ui-kit.png',fullPage:true});await browser.close();

