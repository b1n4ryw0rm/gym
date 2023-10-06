use std::io;

fn main() {
    let mut n = String::new();

    io::stdin()
        .read_line(&mut n)
        .expect("failed to read");

    let n: i32 = n.trim().parse().expect("invalid input");

    for i in 1..=10 {
        let res = n * i;
        println!("{} x {} = {}", n, i, res);
    } 
}
