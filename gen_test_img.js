const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  // 设置一个小viewport
  await page.setViewportSize({ width: 800, height: 400 });
  
  // 打开一个本地HTML测试页
  const html = `
  <!DOCTYPE html>
  <html>
  <head><style>
    body { background: #2c3e50; color: white; font-family: Arial; padding: 40px; margin: 0; }
    h1 { color: #e74c3c; margin: 0 0 20px 0; }
    p { font-size: 24px; margin: 0; }
    .box { background: #34495e; border-radius: 8px; padding: 20px; display: inline-block; }
  </style></head>
  <body>
    <div class="box">
      <h1>Hello World!</h1>
      <p>OpenClaw 图像理解测试</p>
      <p>March 23, 2026</p>
      <p>这是一段中文测试文字</p>
    </div>
  </body>
  </html>
  `;
  
  await page.setContent(html);
  
  const outPath = 'C:/Users/Administrator/.qclaw/workspace/test_img.png';
  await page.screenshot({ path: outPath, type: 'png' });
  console.log('Screenshot saved:', outPath);
  
  const stats = fs.statSync(outPath);
  console.log('File size:', stats.size, 'bytes');
  
  await browser.close();
})();
