fn main() {
    println!("Hello, world!");
}

struct Game;

struct GameOptions {
    answer: String,
}


impl Game {
    pub fn new(game_ops: GameOptions) -> Self {
        Self {}
    }
}

#[cfg(test)]
mod test;
