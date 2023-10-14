use std::io;

fn main() {
    let mut n = String::new();

    io::stdin()
        .read_line(&mut n)
        .expect("failed to read");

    let n: i32 = n.trim().parse().expect("invalid input");

    let bin = format!("{:b}", n);
    
    let mut count = 0;
    let mut max_cout = 0;

    for c in bin.chars() {
        if c == '1' {
            count += 1;
            if count > max_cout {
                max_cout = count;
            }
        } else {
            count = 0
        }
    }

    println!("{}", max_cout);
}
