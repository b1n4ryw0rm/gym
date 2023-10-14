use std::io;

fn factorial(n: i32) -> i32 {
    if n == 1 {
        return 1
    } else {
        return n * factorial(n - 1);
    }
}

fn main() {
    let mut n = String::new();

    io::stdin()
        .read_line(&mut n)
        .expect("failed to read");

    let n: i32 = n.trim().parse().expect("invalid input");

    let result = factorial(n);

    println!("{}", result);
}
