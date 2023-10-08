use std::io;
use std::collections::HashMap;

fn main() {
    let mut phone_book = HashMap::new();
    
    let mut n = String::new();

    io::stdin()
        .read_line(&mut n)
        .expect("failed to read");

    let n: i32 = n.trim().parse().expect("invalid input");

    for _ in 0..n {
        
        let mut entry = String::new();

        io::stdin()
            .read_line(&mut entry)
            .expect("failed to read");

        let parts: Vec<&str> = entry.trim().split_whitespace().collect();

        let name = parts[0].to_string();
        let number = parts[1].to_string();
        phone_book.insert(name.clone(), number);
        
    }
    
    loop {
        let mut query = String::new();
        io::stdin()
            .read_line(&mut query)
            .expect("Failed to read line");

        let name_to_lookup = query.trim();

        if name_to_lookup == "" {
            break; // Exit the loop if there's no more input
        }

        if phone_book.contains_key(name_to_lookup) {
            let number = phone_book.get(name_to_lookup).unwrap(); // Get the number associated with the name
            println!("{}={}", name_to_lookup, number);
        } else {
            println!("Not found");
        }
    }
}
