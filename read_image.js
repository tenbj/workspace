const fs = require('fs');
const path = require('path');

// 读取图片文件并转为 base64
const imgPath = process.argv[2];
if (!imgPath) {
  console.error('Usage: node read_image.js <image_path>');
  process.exit(1);
}

const data = fs.readFileSync(imgPath);
const base64 = data.toString('base64');
const ext = path.extname(imgPath).slice(1).toLowerCase();
const mimeType = ext === 'jpg' || ext === 'jpeg' ? 'image/jpeg' : `image/${ext}`;

// 输出 data URL 供 AI 识别
console.log(`data:${mimeType};base64,${base64.substring(0, 100)}...`);
console.log('SIZE:', data.length, 'bytes');
console.log('BASE64_FULL:', base64);
