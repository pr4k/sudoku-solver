import cv2
from matplotlib import pyplot as plt

from opencv_part import get_sudo_grid, get_sudoku, solve_sudoku, create_sudoku_img, change_perspective_to_original

'''
get_sudoku_grid:- 
Input: Img array, Size
Output: cropped_img, original, pts1, pts2

get_sudoku    
Input: Cropped_img, size 
Output: sudoku_image_with_eroded_digits, unsolved_sudoku_list

solve_sudoku   
Input: sudoku_unsolved, shape
Output: sudoku_solved_list, sudoku_unsolved_image

create_sudoku_img
Input: sudoku_image_original, sudoku_solved, sudoku_unsolved, with_lines:bool
Output: solved_sudoku_image

change_perspective_to_original
Input: pts2, pts1, sudoku_image, original
output: Final_Image
'''
name = 'sudoku_images/sudoku5.jpg'
img = cv2.imread(name,1)

crp_img, orgnl, pts1, pts2 = get_sudo_grid(img,900)

sd_img, unsolved_sd_lst = get_sudoku(crp_img, 900)

solved_sd_lst, unsolved_sd_img = solve_sudoku(unsolved_sd_lst, sd_img.shape)

solved_sd_img = create_sudoku_img(crp_img, solved_sd_lst, unsolved_sd_lst, False)

final = change_perspective_to_original(pts2, pts1, solved_sd_img, orgnl)

plt.imshow(final)
plt.show()
