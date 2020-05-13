
import cv2
from matplotlib import pyplot as plt

from opencv_part import get_sudo_grid, get_sudoku, solve_sudoku, create_sudoku_img, change_perspective_to_original

# cap = cv2.VideoCapture(0)
# images = []
# while 1:
#     ret, frame = cap.read()
#     try:
#         crp_img, orgnl, pts1, pts2 = get_sudo_grid(frame,900)
#         images.append(crp_img)
#         if crp_img.shape[0] == 900:
#             cv2.imshow('frame',crp_img)
#             break
#     except:
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
# 
# cap.release()
# cv2.destroyAllWindows()

folder = 'images/' 
img = cv2.imread("cropped.jpg",0)
orgnl = cv2.imread("original.jpg",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
sd_img, unsolved_sd_lst = get_sudoku(img, 900)
cv2.imwrite(folder + "sd_img.jpg",sd_img)
print("Numbers are extracted")

solved_sd_lst, unsolved_sd_img = solve_sudoku(unsolved_sd_lst, sd_img.shape)
cv2.imwrite(folder + "unsolved_sd_img.jpg",unsolved_sd_img)
print("Unsolved Sudoku image ready")

solved_sd_img = create_sudoku_img(img, solved_sd_lst, unsolved_sd_lst, False)
cv2.imwrite(folder + "solved_sd_img.jpg",solved_sd_img)
print("Solved sudoku image ready")


