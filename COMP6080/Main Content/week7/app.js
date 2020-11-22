const express = require('express');
const bodyParser = require('body-parser');
var cors = require('cors');

const app = express();
const port = 6080;

let count = 0;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.get('/count', (req, res) => {
  res.json({
  	count: count,
  });
});

app.post('/count/increment', (req, res) => {
	console.log(req.body);
  const increase = req.body.increase;
  console.log(increase, count);
  count += increase;
  res.json({});
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});