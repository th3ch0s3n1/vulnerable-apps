const http = require('http');
const crypto = require('crypto');
const db = require('better-sqlite3')(':memory:');

const hash = p => crypto.createHash('sha256').update(p).digest('hex');

db.exec(`
  CREATE TABLE users (name TEXT, password TEXT, is_admin INTEGER);
  INSERT INTO users VALUES ('alice', '${hash("tajne123")}', 0);
  INSERT INTO users VALUES ('admin', '${hash("admin1234")}', 1);
`);

const FORM = `<!DOCTYPE html><html><body>
  <form method="POST" action="/login">
    <input name="username" placeholder="Uživatel"><br>
    <input name="password" type="password" placeholder="Heslo"><br>
    <button>Přihlásit</button>
  </form></body></html>`;

const login = db.prepare('SELECT * FROM users WHERE name = ? AND password = ?');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  if (req.method === 'GET') return res.end(FORM);

  let body = '';
  req.on('data', d => body += d);
  req.on('end', () => {
    const p = new URLSearchParams(body);
    const pass = hash(p.get('password') ?? '');

    const row = login.get(p.get('username'), pass);

    res.end(row ? `Vítejte, ${row.name}!` : 'Špatné jméno nebo heslo.');
  });
});

server.listen(5000);
