export class GameState {
	constructor() {
		this.state = {
			orange: 6,
			blue: 6
		};

		this.nextUpdatePromise = new Promise((resolve) => {
			this.resolveNextUpdate = resolve;
		});
	}

	nextUpdate() {
		return this.nextUpdatePromise;
	}

	changed() {
		this.resolveNextUpdate();
		this.nextUpdatePromise = new Promise((resolve) => {
			this.resolveNextUpdate = resolve;
		});
	}

	get orange() {
		return this.state.orange;
	}

	moveBarToBlue() {
		if (this.state.blue === 12)
			return;
		this.state.blue++;
		this.state.orange--;
		this.changed();
	}

	moveBarToOrange() {
		if (this.state.orange === 12)
			return;
		this.state.orange++;
		this.state.blue--;
		this.changed();
	}

	get blue() {
		return this.state.blue;
	}

	updateBlue(diff) {
		this.state.blue += diff;
		this.changed();
	}
}