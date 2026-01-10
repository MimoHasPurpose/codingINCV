"""
@file laplace_demo.py
@brief Sample code showing how to detect edges using the Laplace operator
"""
import sys
import cv2 as cv
def main(argv):
    # [variables]
    # Declare the variables we are going to use
    ddepth = cv.CV_16S
    k_s1 = 1
    k_s2 = 3
    k_s3 = 5
    k_s4 = 7
    window_name1 ="kernel size-1"
    window_name2="kernel size-3"
    window_name3="kernel size-5"
    window_name4="kernel size-7"
    # [variables]
    # [load]
    imageName = argv[0] if len(argv) > 0 else 'lena.jpg'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR) # Load an image
    
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image')
        print ('Program Arguments: [image_name -- default lena.jpg]')
        return -1
    # [load]
    # [reduce_noise]
    # Remove noise by blurring with a Gaussian filter
    src = cv.GaussianBlur(src, (5, 5), 0)

   
    # [reduce_noise]
    # [convert_to_gray]
    # Convert the image to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # [convert_to_gray]
    # Create Window
    cv.namedWindow(window_name1, cv.WINDOW_AUTOSIZE)
    cv.namedWindow(window_name2, cv.WINDOW_AUTOSIZE)
    cv.namedWindow(window_name3, cv.WINDOW_AUTOSIZE)
    cv.namedWindow(window_name4, cv.WINDOW_AUTOSIZE)
    # [laplacian]
    # Apply Laplace function
    dst =cv.Laplacian(src_gray,ddepth,ksize=k_s1)
    dst2=cv.Laplacian(src_gray,ddepth,ksize=k_s2)
    dst3=cv.Laplacian(src_gray,ddepth,ksize=k_s3)
    dst4=cv.Laplacian(src_gray,ddepth,ksize=k_s4)
    # [laplacian]
    # [convert]
    # converting back to uint8

    abs_dst = cv.convertScaleAbs(dst)
    abs_dst2=cv.convertScaleAbs(dst2)
    abs_dst3=cv.convertScaleAbs(dst3)
    abs_dst4=cv.convertScaleAbs(dst4)
    # [convert]
    # [display]
    cv.imshow(window_name1, abs_dst)
    cv.imshow(window_name2,abs_dst2)
    cv.imshow(window_name3,abs_dst3)
    cv.imshow(window_name4,abs_dst4)
    cv.waitKey(0)
    # [display]
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
