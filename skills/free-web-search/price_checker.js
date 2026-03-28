#!/usr/bin/env node
/**
 * 电商价格查询工具 - 支持淘宝/京东价格查询
 * 使用 web_fetch 获取公开价格信息
 */

const https = require('https');

// 搜索淘宝/京东商品
async function searchPrice(keyword) {
  // 使用 Bing 图片搜索来查找商品价格
  const searchUrl = `https://www.bing.com/images/search?q=${encodeURIComponent(keyword + ' 价格')}`;
  
  return new Promise((resolve, reject) => {
    const req = https.get(searchUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        // 提取价格信息
        const prices = [];
        const priceMatches = data.match(/(\d{2,3})[\s]*元/g) || [];
        priceMatches.forEach(match => {
          const price = parseInt(match.replace(/[^0-9]/g, ''));
          if (price >= 50 && price <= 800) {
            prices.push(price);
          }
        });
        resolve([...new Set(prices)].sort((a, b) => a - b));
      });
    });
    req.on('error', reject);
    req.setTimeout(10000, () => reject(new Error('Timeout')));
  });
}

// 主函数
async function main() {
  const products = [
    '苏泊尔 KJ50D827 空气炸锅',
    '九阳 KL50-VF516 空气炸锅', 
    '小熊 QZG-E14N7 空气炸锅',
    '美的 MF-KZE5004 空气炸锅',
    '飞利浦 HD9200 空气炸锅'
  ];
  
  console.log('=== 空气炸锅价格查询 ===\n');
  
  for (const product of products) {
    console.log(`查询: ${product}`);
    try {
      const prices = await searchPrice(product);
      if (prices.length > 0) {
        console.log(`  价格区间: ${prices[0]} - ${prices[prices.length - 1]} 元`);
        console.log(`  参考价格: ${prices.slice(0, 5).join(', ')} 元\n`);
      } else {
        console.log('  未获取到价格信息\n');
      }
    } catch (e) {
      console.log(`  查询失败: ${e.message}\n`);
    }
  }
}

main().catch(console.error);
