# An Augmented Sudoku Solution Image Generator
![python](https://img.shields.io/badge/Python-3.8-blue) 
![cargo](https://img.shields.io/badge/cargo-1.42.0-red)

So my aim was to create a project to solve the sudoku puzzle just using the image of it and Augmenting the solution back to the original Image.

It is a fairly under developed project and contains many glitches.

---

## Technology Used

- Python
- Rust
- Opencv
---
## Working Flow

We are using **Opencv** to Locate the Sudoku block in the image.



<img src = "output/orgnl.jpg" width = 300px style = "padding:20px;"></img>
<img src = "output/crpzimg.jpg" width = 300px style = "padding:20px;"></img>

After getting the cropped image , next job is to *remove the extra noise* and fill the openings if any and get the **number contours**.

<img src = "output/sd_img.jpg" width = 300px style = "padding:20px;"></img>

Next is to detect the numbers using our **ML model** and create a *digital copy of the whole sudoku puzzle*

<img src = "output/unsolved_sd_img.jpg" width = 300px style = "padding:20px;"></img>

After getting the digits recognized, we will be using our **Python library Written in Rust** to Solve the Sudoku and get the solution


<img src = "output/solved_sd_img.jpg" width = 300px style = "padding:20px;"></img>


Once we have the solution its time to **mask** it over our original image.

<img src = "output/final.jpg" width = 400px style = "padding:20px;"></img>



