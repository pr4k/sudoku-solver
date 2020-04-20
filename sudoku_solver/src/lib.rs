use cpython::{py_fn, py_module_initializer, PyResult, Python};
use sudoku::Sudoku;

py_module_initializer!(sudoku_solver, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "solve", py_fn!(py, solve_py(sudoku_line: String)))?;
    Ok(())
});

fn solve_py(_: Python, sudoku_line: String) -> PyResult<String> {
    let out = solve(sudoku_line);
    Ok(out)
}
fn solve(sudoku_line: String) -> String {
    let sudoku = Sudoku::from_str_line(&sudoku_line).unwrap();

    let mut solution: String;
    solution = "".to_string();
    // Solve, print or convert the sudoku to another format
    if let Some(solve) = sudoku.solve_unique() {
        // print the solution in line format
        solution = solve.to_string();

        // or return it as a byte array
    }
    solution.to_string()
}
