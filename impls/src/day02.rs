use pyo3::prelude::*;

pub fn part1_impl(data: &str) -> i64 {
    let mut total: i64 = 0;

    for range in data.split(',') {
        if let Some(ind) = range.find('-') {
            let start: i64 = range[..ind].trim().parse().unwrap();
            let end: i64 = range[ind + 1..].trim().parse().unwrap();

            for i in start..=end {
                let s = i.to_string();
                let digits = s.len();

                let mid = digits / 2;
                if &s[..mid] == &s[mid..] {
                    total += i;
                }
            }
        }
    }

    total
}

pub fn part2_impl(data: &str) -> i64 {
    let mut total: i64 = 0;

    for range in data.split(',') {
        if let Some(ind) = range.find('-') {
            let start: i64 = range[..ind].trim().parse().unwrap();
            let end: i64 = range[ind + 1..].trim().parse().unwrap();

            for i in start..=end {
                let s = i.to_string();
                let digits = s.len();
                let mut added = false;

                // Try every block size that divides the digit length
                for size in 1..=digits / 2 {
                    if digits % size != 0 {
                        continue;
                    }

                    let blocks = digits / size;
                    let mut all_equal_pairs = true;

                    for block in 0..(blocks - 1) {
                        let start1 = block * size;
                        let end1 = start1 + size;
                        let start2 = end1;
                        let end2 = start2 + size;

                        if &s[start1..end1] != &s[start2..end2] {
                            all_equal_pairs = false;
                            break;
                        }
                    }

                    if all_equal_pairs {
                        total += i;
                        added = true;
                        break; // don't add i multiple times
                    }
                }

                if added {
                    // already counted this i, move on
                    continue;
                }
            }
        }
    }

    total
}

#[pyfunction]
pub fn part1(data: &str) -> PyResult<i64> {
    Ok(part1_impl(&data))
}

#[pyfunction]
pub fn part2(data: &str) -> PyResult<i64> {
    Ok(part2_impl(&data))
}
