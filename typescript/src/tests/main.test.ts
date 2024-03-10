import { isBinaryOperatorToken } from 'typescript';
import { Game, PlacementError } from '../main';


describe("Othello Game", () => {
    test('make sure game initialized correctly', () => {
      const gi = new Game();
      
        expect(gi.board.getAxis("alpha").length).toBe(8);
        expect(gi.board.getAxis("num").length).toBe(8);
        
        expect(gi.getWhosTurn()).toBe("black");

    });
    
    
    
    test('make sure the starting pucks are there in their correct location  ', () => {
        const gi = new Game();
        
        expect(gi.board.get("d",5)).toBe("black");
        expect(gi.board.get("d",4)).toBe("white");
    
        expect(gi.board.get("e",5)).toBe("white");
        expect(gi.board.get("e",4)).toBe("black");
    
    
    
        expect(gi.board.get("d",3)).toBe(null);
    
    });

    test("checks first move", () => {
        const gi =  new Game();
        const b = gi.board;

        // place new puck
        b.place("e",6)
        expect(b.get("e",6)).toBe("black");
        expect(b.get("e",5)).toBe("black");


        const black = gi.getPlayer("black");
        expect(black.pucks).toBe(4);
        
        const white = gi.getPlayer("white");
        expect(white.pucks).toBe(1);
    
        expect(() => b.place("e", 5)).toThrow(PlacementError.OVERWRITE_NOT_ALLOWED); 
        
        expect(() => {
            b.place("e",8)
        }).toThrow(PlacementError.FLOATING_PUCK_NOT_ALLOWED);
        
    })

    test("get the whole board structure", () => {

        const gi = new Game();
        const b = gi.board;

        /*
        b.place("c",4);
        const white = gi.getPlayer("white");
        
        */
    


    });

});


