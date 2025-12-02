use pyo3::prelude::*;

fn part1_impl(rotations: &[String]) -> i32 {
    let mut dial = 50i32;
    let mut count = 0;

    for rot in rotations {
        let dir = &rot[0..1];
        let dist: i32 = rot[1..].trim().parse().unwrap();

        let mut dial_new = if dir == "R" { dial + dist } else { dial - dist };
        dial_new = ((dial_new % 100) + 100) % 100;

        if dial_new == 0 {
            count += 1;
        }
        dial = dial_new;
    }

    count
}

fn part2_impl(rotations: &[String]) -> i32 {
    let mut dial = 50i32;
    let mut count = 0;

    for rot in rotations {
        let dir = &rot[0..1];
        let dist_raw: i32 = rot[1..].trim().parse().unwrap();

        count += dist_raw / 100; // full rotations

        let mut remaining = dist_raw % 100;
        while remaining > 0 {
            dial = if dir == "R" { dial + 1 } else { dial - 1 };
            dial = ((dial % 100) + 100) % 100;

            if dial == 0 {
                count += 1;
            }

            remaining -= 1;
        }
    }

    count
}

#[pyfunction]
pub fn part1(data: Vec<String>) -> PyResult<i32> {
    Ok(part1_impl(&data))
}

#[pyfunction]
pub fn part2(data: Vec<String>) -> PyResult<i32> {
    Ok(part2_impl(&data))
}
