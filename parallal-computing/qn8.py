import cv2
import numpy as np
import time
from multiprocessing import Pool, cpu_count


# ==============================
# IMAGE LOADING
# ==============================
def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Image not found!")
    return img


# ==============================
# BLUR OPERATION (Sequential)
# ==============================
def blur_sequential(image):
    kernel = np.ones((3, 3)) / 9
    return cv2.filter2D(image, -1, kernel)


# ==============================
# SHARPEN OPERATION
# ==============================
def sharpen_sequential(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)


# ==============================
# EDGE DETECTION (Sobel)
# ==============================
def edge_detection_sequential(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    return np.uint8(np.clip(magnitude, 0, 255))


# ==============================
# PARALLEL HELPER FUNCTION
# ==============================
def parallel_apply(func, image):
    num_processes = cpu_count()
    chunks = np.array_split(image, num_processes)

    with Pool(num_processes) as pool:
        results = pool.map(func, chunks)

    return np.vstack(results)


# ==============================
# MAIN
# ==============================
def main():

    image = load_image("input.jpg")

    print("Image loaded successfully")
    print("Image shape:", image.shape)

    # ---------------- BLUR ----------------
    start = time.time()
    blur_seq = blur_sequential(image)
    end = time.time()
    blur_seq_time = end - start
    print("Blur Sequential Time:", blur_seq_time)

    start = time.time()
    blur_par = parallel_apply(blur_sequential, image)
    end = time.time()
    blur_par_time = end - start
    print("Blur Parallel Time:", blur_par_time)

    # ---------------- SHARPEN ----------------
    start = time.time()
    sharp_seq = sharpen_sequential(image)
    end = time.time()
    sharp_seq_time = end - start
    print("Sharpen Sequential Time:", sharp_seq_time)

    start = time.time()
    sharp_par = parallel_apply(sharpen_sequential, image)
    end = time.time()
    sharp_par_time = end - start
    print("Sharpen Parallel Time:", sharp_par_time)

    # ---------------- EDGE ----------------
    start = time.time()
    edge_seq = edge_detection_sequential(image)
    end = time.time()
    edge_seq_time = end - start
    print("Edge Sequential Time:", edge_seq_time)

    start = time.time()
    edge_par = parallel_apply(edge_detection_sequential, image)
    end = time.time()
    edge_par_time = end - start
    print("Edge Parallel Time:", edge_par_time)

    # ---------------- SPEEDUP ----------------
    print("\nSpeedup Analysis:")
    print("Blur Speedup:", blur_seq_time / blur_par_time)
    print("Sharpen Speedup:", sharp_seq_time / sharp_par_time)
    print("Edge Speedup:", edge_seq_time / edge_par_time)

    # ---------------- SAVE OUTPUTS ----------------
    cv2.imwrite("blur_output.jpg", blur_par)
    cv2.imwrite("sharpen_output.jpg", sharp_par)
    cv2.imwrite("edge_output.jpg", edge_par)

    print("\nProcessing complete. Images saved.")


if __name__ == "__main__":
    main()
