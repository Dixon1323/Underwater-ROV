from ultralytics import YOLO
import cv2
import math 
import time
import numpy as np



cap = cv2.VideoCapture("1.mp4")
cap.set(3, 640)
cap.set(4, 480)


model = YOLO("best.pt")


classNames= ['coral', 'mine', 'mobile', 'n', 'watch']


def red_channel_correction(image):
    red, green, blue = cv2.split(image)
    # Adjust the red channel by combining it with green and blue channels
    red_corrected = cv2.addWeighted(red, 1.5, green, 0.5, 0)
    corrected_image = cv2.merge((red_corrected, green, blue))
    return image,corrected_image

# Function to apply brightness and contrast correction
def white_balance(image, alpha=0.7, beta=-50):
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

# # Function to apply CLAHE to improve local contrast
# def retinex(image):
#     lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
#     l, a, b = cv2.split(lab)
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     l_clahe = clahe.apply(l)
#     lab_clahe = cv2.merge((l_clahe, a, b))
#     return cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

def modified_retinex_with_dense_paths(image, sigma=25):
    # Convert image to LAB
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab)

    # Estimate illumination using Gaussian blur (proxy for path-based estimation)
    # You can later replace this with your own 8-path logic using pixel averaging.
    illumination = cv2.GaussianBlur(l_channel, (0, 0), sigma)

    # Prevent division by zero
    illumination = np.where(illumination == 0, 1, illumination)

    # Retinex: Reflectance = log(image) - log(illumination)
    reflectance = np.log1p(l_channel.astype(np.float32)) - np.log1p(illumination.astype(np.float32))
    reflectance = cv2.normalize(reflectance, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Merge back to LAB and then to BGR
    merged = cv2.merge((reflectance, a_channel, b_channel))
    enhanced_image = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    return enhanced_image



def adaptive_histogram_transform(image, epsilon=10):
    # Convert image to float32 for precision during calculations.
    image_float = image.astype(np.float32)
    output = np.zeros_like(image_float)
    
    # Process each channel independently.
    for c in range(3):
        channel = image_float[:, :, c]
        mean_val = channel.mean()
        
        # Define masks for the three regions.
        mask1 = channel < (mean_val - epsilon)
        mask2 = np.abs(channel - mean_val) <= epsilon
        mask3 = ~(mask1 | mask2)  # remaining pixels
        
        # Apply piecewise linear function.
        out_channel = np.zeros_like(channel)
        # Region 1: 0 ≤ I_c < Ī_c - ε
        out_channel[mask1] = (100 * channel[mask1]) / (mean_val - epsilon)
        # Region 2: |I_c - Ī_c| ≤ ε
        out_channel[mask2] = channel[mask2] - mean_val + 120
        # Region 3: Else
        out_channel[mask3] = (115 * (channel[mask3] - mean_val - epsilon)) / (235 - mean_val) + 130
        
        # Clip the values to [0, 255] and assign to output.
        output[:, :, c] = np.clip(out_channel, 0, 255)
    
    return output.astype(np.uint8)

def preprocess_underwater_image(image_path):
    image,red_image = red_channel_correction(image_path)  # Step 1
    adjusted_image = white_balance(image, alpha=0.65, beta=-40)
    retinex_img = modified_retinex_with_dense_paths(adjusted_image) 
    gamma_corrected_image = adaptive_histogram_transform(retinex_img, epsilon=10)
    return image, red_image, adjusted_image, retinex_img, gamma_corrected_image


while True:
    # time.sleep(4)
    success, img = cap.read()
    red_corrected,red__image, adjusted_image, retinex_image, preprocessed_image = preprocess_underwater_image(img)

    results = model(preprocessed_image, stream=True)


    for r in results:
        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

            

            
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])
            # print(a)

            
            org = [x1, y1+100]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 255, 0)
            thickness = 2
            if(classNames[cls]=="mine"or classNames[cls]=="coral"or classNames[cls]=="mobile"or classNames[cls]=="watch"or classNames[cls]=="n"):
                cv2.rectangle(preprocessed_image, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(preprocessed_image, classNames[cls], org, font, fontScale, color, thickness)



    cv2.imshow('Original', img)
    cv2.imshow('1 Preprocessing', red__image)
    cv2.imshow('2 Preprocessing', adjusted_image)
    cv2.imshow('3 Preprocessing', retinex_image)
    cv2.imshow('4 Preprocessing', preprocessed_image)
   

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()