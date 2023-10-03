use std::io;

fn main(){
    let mut num = String::new();

    io::stdin()
        .read_line(&mut num)
        .expect("failed to read");

    let num: i32 = num.trim().parse().expect("invalid input");

    if num % 2 == 0 {
        if num >= 2 && num <= 5 {
            println!("Not Weird");
        } else if num >= 6 && num <= 20 {
            println!("Weird");
        } else if num > 20 {
            println!("Not Weird");
        }
    } else {
        println!("Weird");
    }
}
