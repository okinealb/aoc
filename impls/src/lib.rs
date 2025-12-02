use pyo3::prelude::*;

mod day01;
mod day02;

#[pymodule]
fn impls(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Day 1
    let day01_mod = PyModule::new(py, "day01")?;
    day01_mod.add_function(wrap_pyfunction!(day01::part1, &day01_mod)?)?;
    day01_mod.add_function(wrap_pyfunction!(day01::part2, &day01_mod)?)?;
    m.add_submodule(&day01_mod)?;
    
    // Day 2
    let day02_mod = PyModule::new(py, "day02")?;
    day02_mod.add_function(wrap_pyfunction!(day02::part1, &day02_mod)?)?;
    day02_mod.add_function(wrap_pyfunction!(day02::part2, &day02_mod)?)?;
    m.add_submodule(&day02_mod)?;

    Ok(())
}