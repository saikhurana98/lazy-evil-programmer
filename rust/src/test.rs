use super::*;

#[test]
fn can_initialize_game() {
    let options = GameOptions {
        answer: String::from("ADIEU")
    };
    let game = Game::new(options);
}