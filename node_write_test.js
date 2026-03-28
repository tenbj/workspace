const fs = require('fs');
try {
  fs.writeFileSync('C:/Users/Administrator/test_node.txt', 'hello from node');
  console.log('WRITE OK');
  fs.unlinkSync('C:/Users/Administrator/test_node.txt');
} catch(e) {
  console.log('FAIL:', e.code, e.message);
}
