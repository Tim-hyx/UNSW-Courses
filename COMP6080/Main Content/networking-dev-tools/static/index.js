const markGraphs = {
	'exam-1-marks': '/api/marks/exam/1',
	'exam-2-marks': '/api/marks/exam/2',
	'ass-1-marks': '/api/marks/ass/1',
};

function done() {
	document.getElementById('loading-screen').remove();
	document.body.style.overflow = '';
}

function populateMarksGraph(target, dataPoints) {
	const ctx = document.getElementById(target).getContext('2d');
	const options = {"scales":{"yAxes":[{"ticks":{"beginAtZero":true}}]}};
	const data = {
		labels: ['A', 'B', 'C', 'D', 'F'],
		datasets: [{
			label: 'Class Data',
			data: dataPoints,
			backgroundColor: [
				'#18bc9c',
				'#3498db',
				'#3498db',
				'#f39c12',
				'#e74c3c'
			]
		}]
	};
	new Chart(ctx, {
		type: 'bar',
		data,
		options
	});
}

function populateAttendenceGraph(target, dataPoints) {
	const ctx = document.getElementById(target).getContext('2d');
	const options = {};
	const data = {
		labels: new Array(31).fill().map((_, i) => String(i+1)),
		datasets: [{
			label: 'Attendence Data',
			data: dataPoints
		}]
	};

	new Chart(ctx, {
		type: 'line',
		data,
		options
	});
}

async function populateStudentsTable() {
	document.getElementById('table-error').style.display = 'none';
	const table = document.getElementById('students');
	table.innerHTML = '';
	let r;
	try {
		r = await fetch('/data/students.json');
	} catch (err) {
		document.getElementById('table-error').style.display = 'block';
		return;
	}
	const students = await r.json();
	for (student of students) {
		const cols = [student.id, student.name, student.average];
		const row = document.createElement('tr');
		for (const col of cols) {
			const td = document.createElement('td');
			td.innerText = col;
			row.appendChild(td);
		}
		table.appendChild(row);
	}
}

function tick() {
	if (!startTime) {
		startTime = Date.now();
	}
	document.getElementById('active-time').innerText = Math.floor((Date.now() - startTime)/1000);
}

async function init() {
	const allPromises = [];
	for (const [id, dataUrl] of Object.entries(markGraphs)) {
		allPromises.push(
			fetch(dataUrl)
				.then(r => r.json())
				.then(data => {
					populateMarksGraph(id, data);
				}))
	}
	
	await Promise.all(allPromises);

	await populateStudentsTable();
	document.getElementById('refresh-students')
		.addEventListener('click', () => {
			populateStudentsTable();
			document.getElementById('pencil').classList.toggle('write');
		});

	const attendenceData = await fetch('/api/attendence/oct').then(r => r.json());
	populateAttendenceGraph('attendence', attendenceData);
}

window.addEventListener('load', () => {
	document.body.style.overflow = 'hidden';
	init()
		.finally(done);
});