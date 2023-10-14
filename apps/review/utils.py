import cv2


def cartoonify_image(image, output_path):
    # Load the image using cv2
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.medianBlur(grayimg, 5)

    # Get the edges
    edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

    # Convert to a cartoon version
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save the cartoonized image to a file
    file = f"review/covers/cartoonize/{output_path.split('/')[-1]}"
    cv2.imwrite(f"media/{file}", cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))
    return file
