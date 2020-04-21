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
folder = 'output/'
name = 'sudoku_images/sudoku5.jpg'
img = cv2.imread(name,1)

crp_img, orgnl, pts1, pts2 = get_sudo_grid(img,900)

cv2.imwrite(folder + "crpzimg.jpg",crp_img)
cv2.imwrite(folder + "orgnl.jpg",orgnl)
print("Image is cropped")

sd_img, unsolved_sd_lst = get_sudoku(crp_img, 900)

cv2.imwrite(folder + "sd_img.jpg",sd_img)
print("Numbers are extracted")

solved_sd_lst, unsolved_sd_img = solve_sudoku(unsolved_sd_lst, sd_img.shape)
cv2.imwrite(folder + "unsolved_sd_img.jpg",unsolved_sd_img)
print("Unsolved Sudoku image ready")

solved_sd_img = create_sudoku_img(crp_img, solved_sd_lst, unsolved_sd_lst, False)
cv2.imwrite(folder + "solved_sd_img.jpg",solved_sd_img)
print("Solved sudoku image ready")

final = change_perspective_to_original(pts2, pts1, solved_sd_img, orgnl)
cv2.imwrite(folder + "final.jpg",final)
print("Perspective changed to original image")

plt.imshow(final)
plt.show()
