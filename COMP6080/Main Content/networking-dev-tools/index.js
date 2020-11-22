const express = require('express');
const bodyParser = require('body-parser')

const app = express();
const port = 3000;

function fail(res, message) {
	res.status(400);
	res.send(message);
}

function slowResponse(res, data, wait) {
	setTimeout(() => {
		res.json(data);
	}, wait);
}

app.use(express.static('static'));
app.use((req, res, next) => { 
  if (req.url === "/data/students.json") {
    res.set('Cache-control', 'public, max-age=300'); 
  }
  next();
});
app.use('/data', express.static('data', {
  etag: false,
  lastModified: false
}));

app.get('/api/marks/exam/:examNumber', (req, res) => {
  const examNumberString = req.params.examNumber;
  let examNumber = Number(examNumberString);
  if (isNaN(examNumber) || examNumber > 2 || examNumber <= 0) {
	fail(res, "Invalid exam number provided");
  	return;
  }
  
  if (examNumber === 1) {
	slowResponse(res, [3, 7, 4, 2, 1], 1000);
  } else {
	slowResponse(res, [1, 3, 6, 4, 1], 1000);
  }
});

app.get('/api/marks/ass/:assignmentNumber', (req, res) => {
	const assignmentNumberString = req.params.assignmentNumber;
	let assignmentNumber = Number(assignmentNumberString);
	if (isNaN(assignmentNumber) || assignmentNumber > 1 || assignmentNumber <= 0) {
	  fail(res, "Invalid assignment number provided");
		return;
	}
	slowResponse(res, [8, 4, 3, 4, 2], 3000);
  });

app.get('/api/attendence/:month', (req, res) => {
	const month = req.params.month;
	if (month !== 'oct') {
		fail(res, 'Invalid month');
		return;
	}
	const data = new Array(31).fill(0).map(() => Math.floor(Math.random() * 26));
	res.json(data);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});