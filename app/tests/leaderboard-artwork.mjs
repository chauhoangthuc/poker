import {chromium} from '@playwright/test';
const b=await chromium.launch({executablePath:process.env.PLAYWRIGHT_CHROMIUM_PATH});const p=await b.newPage({viewport:{width:1586,height:992},deviceScaleFactor:1});await p.goto('http://localhost:5173/leaderboard');await p.evaluate(async()=>{await document.fonts.ready;await Promise.all(['/assets/leaderboard-stage.png','/assets/buttons/navy.png','/assets/buttons/violet.png'].map(src=>{let i=new Image();i.src=src;return i.decode()}))});await p.screenshot({path:'../qa/leaderboard-artwork.png'});await b.close();


