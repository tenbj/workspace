#!/usr/bin/env node
/**
 * 闲鱼价格监控脚本 - 通过网页抓取获取价格信息
 * 使用 Playwright 或 puppeteer 获取渲染后的页面
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// 搜索关键词
const KEYWORDS = ['空气炸锅', '全新'];

// 闲鱼搜索 URL
function getXianyuSearchUrl(keyword) {
  const encoded = encodeURIComponent(keyword);
  return `https://www.goofish.com/search?q=${encoded}`;
}

// 使用 curl 获取页面
async function fetchWithCurl(url) {
  try {
    const result = execSync(`curl.exe -sL "${url}" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"`, {
      encoding: 'utf-8',
      timeout: 15000
    });
    return result;
  } catch (e) {
    console.error('Curl failed:', e.message);
    return null;
  }
}

// 解析价格
function extractPrices(html) {
  const prices = [];
  // 匹配价格格式：¥123、123元、123.00等
  const priceRegex = /[¥￥]\s*(\d+(?:\.\d{1,2})?)\s*元?|<[^>]*>(\d{2,3}(?:\.\d{1,2})?)\s*<[^>]*>\s*元/g;
  let match;
  while ((match = priceRegex.exec(html)) !== null) {
    const price = parseFloat(match[1] || match[2]);
    if (price > 50 && price < 1000) {
      prices.push(price);
    }
  }
  return prices;
}

// 主函数
async function main() {
  console.log('开始搜索闲鱼空气炸锅价格...\n');
  
  const searchUrl = getXianyuSearchUrl(KEYWORDS.join(' '));
  console.log('搜索URL:', searchUrl);
  
  const html = await fetchWithCurl(searchUrl);
  
  if (!html) {
    console.error('无法获取页面内容');
    process.exit(1);
  }
  
  // 显示页面长度
  console.log('页面大小:', html.length, '字符\n');
  
  // 提取价格
  const prices = extractPrices(html);
  
  if (prices.length === 0) {
    console.log('未提取到价格信息，可能需要登录或页面结构变化');
  } else {
    console.log('找到', prices.length, '个价格:');
    const uniquePrices = [...new Set(prices)].sort((a, b) => a - b);
    console.log('价格区间:', uniquePrices[0], '-', uniquePrices[uniquePrices.length - 1], '元');
    console.log('前10个价格:', uniquePrices.slice(0, 10).join(', '));
  }
}

main().catch(console.error);
