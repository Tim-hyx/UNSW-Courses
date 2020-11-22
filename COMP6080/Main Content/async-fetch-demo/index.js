const express = require('express');
const bodyParser = require('body-parser')

const app = express();
const port = 3000;

// In a real app we should have a database but
// for this quick example we are just gonna use a
// global object. This should NEVER be done in a 
// actual website.
const database = {
	food: [
		'Food: Secret killer, studies show food is bad for you',
		'Food: Secret medicine, studies show food is good for you',
	]
};

app.use(express.static('static'));

app.get('/api/posts', (req, res) => {
  const topic = req.query.topic;
  if (!topic) {
  	res.status(400);
  	res.send("No 'topic' provided in query params");
  	return;
  }
  res.json(database[topic] || []);
});

app.post('/api/posts', bodyParser.json(), (req, res) => {
	const topic = req.query.topic;
	if (!topic) {
		res.status(400);
		res.send("No 'topic' provided in query params");
		return;
	}

	const postText = req.body.postText;
	if (!postText) {
		res.status(400);
		res.send("No 'postText' provided in body");
		return;
	}

	database[topic] = [...(database[topic] || []), postText];
	res.status(200);
	res.send(':D');
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});