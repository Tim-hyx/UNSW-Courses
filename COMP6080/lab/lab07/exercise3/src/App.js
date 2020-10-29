import React from "react";
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    const defaultBoard = [['', '', '',], ['', '', '',], ['', '', '',],];
    this.state = {
      board: defaultBoard,
      firstUser: false
    };
  }

  setCell = (x, y) => {
    const letter = this.state.firstUser ? 'X' : 'O';
    const newBoard = { ...this.state.board };
    newBoard[x][y] = letter;
    this.setState({ board: newBoard, firstUser: !this.state.firstUser })
  };

  render() {
    return (
      <div className="App">
        <table border="1">
          <tr>
            <td onClick={() => this.setCell(0, 0)}>{this.state.board[0][0]}</td>
            <td onClick={() => this.setCell(0, 1)}>{this.state.board[0][1]}</td>
            <td onClick={() => this.setCell(0, 2)}>{this.state.board[0][2]}</td>
          </tr>
          <tr>
            <td onClick={() => this.setCell(1, 0)}>{this.state.board[1][0]}</td>
            <td onClick={() => this.setCell(1, 1)}>{this.state.board[1][1]}</td>
            <td onClick={() => this.setCell(1, 2)}>{this.state.board[1][2]}</td>
          </tr>
          <tr>
            <td onClick={() => this.setCell(2, 0)}>{this.state.board[2][0]}</td>
            <td onClick={() => this.setCell(2, 1)}>{this.state.board[2][1]}</td>
            <td onClick={() => this.setCell(2, 2)}>{this.state.board[2][2]}</td>
          </tr>
        </table>
      </div>
    );
  }
}

export default App;
