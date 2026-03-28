#!/usr/bin/env node
/**
 * Free Web Search - No API key needed
 * Uses SearXNG public instances
 */

const SEARCH_INSTANCES = [
  'https://search.sapti.me',
  'https://search.bus-hit.me',
  'https://search.projectsegfault.com',
  'https://search.rhscz.eu'
];

async function search(query, limit = 10) {
  const encodedQuery = encodeURIComponent(query);
  
  for (const instance of SEARCH_INSTANCES) {
    try {
      const url = `${instance}/search?q=${encodedQuery}&format=json&engines=google,bing,duckduckgo`;
      const response = await fetch(url, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        },
        timeout: 10000
      });
      
      if (!response.ok) continue;
      
      const data = await response.json();
      return data.results?.slice(0, limit).map(r => ({
        title: r.title,
        url: r.url,
        snippet: r.content || r.abstract
      })) || [];
    } catch (e) {
      continue;
    }
  }
  
  throw new Error('All search instances failed');
}

// CLI usage
if (require.main === module) {
  const query = process.argv[2];
  if (!query) {
    console.error('Usage: node search.js <query>');
    process.exit(1);
  }
  
  search(query).then(results => {
    console.log(JSON.stringify(results, null, 2));
  }).catch(err => {
    console.error('Search failed:', err.message);
    process.exit(1);
  });
}

module.exports = { search };
