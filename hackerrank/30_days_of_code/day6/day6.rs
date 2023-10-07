use std::io;

fn main() {
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("failed to read");

    let n: i32 = n.trim().parse().expect("invalid input");

    for _i in 0..n {
        let mut s = String::new();
        io::stdin()
            .read_line(&mut s)
            .expect("failed to read");
        
        let mut e = String::new();
        let mut o = String::new();

        for (index, char) in s.trim().chars().enumerate() {
            
            if index % 2 == 0 {
                e.push(char);
            } else {
                o.push(char);
            }
        }
        println!("{} {}", e, o);
    }
}
