import cv2

def localize_plate(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale for better processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply some preprocessing (like thresholding, edge detection, etc.)
    # This step might require some tuning depending on the images you're working with
    
    # Find contours in the image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through the contours and select ones that might be plates
    plates = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / h
        if 2.5 <= aspect_ratio <= 5.0 and w > 100 and h > 20:
            plates.append((x, y, w, h))
    
    return plates

# Example usage
plates = localize_plate('car.jpg')
print(plates)
