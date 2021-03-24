import cv2

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def loades_image(image_path):
    return cv2.imread(image_path)

def show_image(image, image_path):
    gray = get_grayscale(image)
    cv2.imshow(image_path, gray)
    return gray

def saves_image(image, gray):
    cv2.imwrite(image, gray)

def wai_time(time):
    cv2.waitKey(time)
    cv2.destroyAllWindows()