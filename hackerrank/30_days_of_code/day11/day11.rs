use std::io;

fn hourglass_sum(matrix: &Vec<Vec<i32>>) -> i32 {
    let mut max_sum = i32::MIN; // Initialize the maximum sum to the minimum possible integer value

    for i in 0..(matrix.len() - 2) {
        for j in 0..(matrix[i].len() - 2) {
            // Calculate the hourglass sum for the current position
            let current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
                + matrix[i + 1][j + 1]
                + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2];

            // Update the maximum sum if the current sum is greater
            max_sum = max_sum.max(current_sum);
        }
    }

    max_sum
}

fn main() {
    const ROWS: usize = 6;

    let mut array: Vec<Vec<i32>> = Vec::new();

    for _ in 0..ROWS {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let row: Vec<i32> = input
            .split_whitespace()
            .map(|s| s.parse().expect("Failed to parse integer"))
            .collect();
        array.push(row);
    }

    let max_hourglass_sum = hourglass_sum(&array);
    println!("{}", max_hourglass_sum);
}
