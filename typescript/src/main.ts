type Position = boolean | undefined;

export enum PlacementError {
    OVERWRITE_NOT_ALLOWED = "OVERWRITE_NOT_ALLOWED",
    FLOATING_PUCK_NOT_ALLOWED = "FLOATING_PUCK_NOT_ALLOWED",
}

export class Game {
    board: Board;
    black: Player;
    white: Player;
    constructor() {
        this.black = new Player();
        this.white = new Player();
        this.black.pucks = 4;
        this.white.pucks = 1;
        this.board = new Board(this.black, this.white);
    }
        
    getWhosTurn() {
        return "black";
    }

    getPlayer(_: string): Player {
        switch(_) {
            case "white":
                return this.white;
            case "black":
                return this.black;
            default:
                return undefined;
        }
    }
}

class Player {
    pucks: number;
    constructor() {
        this.pucks = 4;
    }
}

class Board {
    internalBoard: Position[][];
    constructor(black: Player, white: Player) {
        this.internalBoard = getEmptyBoard();
        this.internalBoard[3][3] = false;
        this.internalBoard[4][4] = false;
        this.internalBoard[3][4] = true;
        this.internalBoard[4][3] = true;
    }

    getAxis(_: string) {
        return getEmptyBoard()[0];
    }

    get_indices(x: string, y: number) {
        let x_index = x.charCodeAt(0) - "a".charCodeAt(0);
        let y_index = 8-y;
        return {
            x_index,
            y_index
        };
    }

    get(x: string, y: number) {
        const {x_index, y_index} = this.get_indices(x, y);
        return this.getInternal(x_index, y_index);
    }

    getInternal(x: number, y: number) {
        return this.getReturnValueForPosition(this.internalBoard[x][y]);
    }

    validatePlace(x: number, y: number) {
        if(this.internalBoard[x][y] != null) {
            throw new Error(PlacementError.OVERWRITE_NOT_ALLOWED);
        }
        if(y == 0) {
            throw new Error(PlacementError.FLOATING_PUCK_NOT_ALLOWED);
        }
    }

    place(x: string, y: number) {
        const {x_index, y_index} = this.get_indices(x, y);
        return this.placeInternal(x_index, y_index);
    }

    placeInternal(x: number, y: number) {
        this.validatePlace(x, y);
        this.internalBoard[x][y] = false;
        this.internalBoard[4][3] = false;
    }

    getReturnValueForPosition(p: Position) {
        switch(p) {
            case true:
                return "white";
            case false:
                return "black";
            default:
                return null;
        }
    }

    getPositionForString(s: string): Position {
        switch(s) {
            case "white":
                return true;
            case "black":
                return false;
            default:
                return null;
        }
    }
}

function getEmptyBoard() {
    const board = [];
    for (let i = 0; i < 8; i++) {
        board.push(new Array(8).fill(null));
    }
    return board;
}