import io
from PIL import Image
from ultralytics import YOLO
import numpy as np
import cv2

def calculate_jaccard_index(box1, box2):
    """
    Calculate Jaccard Index (IoU) between two bounding boxes.
    
    Args:
        box1, box2: Bounding boxes in format [x1, y1, x2, y2]
    
    Returns:
        Jaccard index (float between 0 and 1)
    """
    # Calculate intersection area
    x1_inter = max(box1[0], box2[0])
    y1_inter = max(box1[1], box2[1])
    x2_inter = min(box1[2], box2[2])
    y2_inter = min(box1[3], box2[3])
    
    if x2_inter <= x1_inter or y2_inter <= y1_inter:
        return 0.0
    
    intersection_area = (x2_inter - x1_inter) * (y2_inter - y1_inter)
    
    # Calculate union area
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = box1_area + box2_area - intersection_area
    
    return intersection_area / union_area if union_area > 0 else 0.0

def process_image(uploaded_file, model_path="./MAJOR_PROJECT_ML_MODELYOLOv8.pt"):
    """
    Loads a YOLOv8 model and performs object detection on an uploaded image.

    Args:
        uploaded_file: File-like object of the uploaded image.
        model_path: Path to the pretrained YOLOv8 .pt model.

    Returns:
        Tuple: (processed_image_bytes, detection_results_dict)
    """
    # Load image using PIL
    image = Image.open(uploaded_file).convert("RGB")
    
    # Convert PIL image to numpy array
    image_np = np.array(image)

    # Load the YOLOv8 model
    model = YOLO(model_path)

    # Run prediction
    results = model(image_np)

    # Extract detection information
    detection_results = {
        'detections': [],
        'total_detections': 0,
        'class_counts': {},
        'average_confidence': 0.0,
        'jaccard_indices': []
    }

    if len(results) > 0 and results[0].boxes is not None:
        boxes = results[0].boxes
        detection_results['total_detections'] = len(boxes)
        
        confidences = []
        detected_boxes = []
        
        for i, box in enumerate(boxes):
            # Get box coordinates and class info
            coords = box.xyxy[0].cpu().numpy()  # [x1, y1, x2, y2]
            confidence = float(box.conf[0].cpu().numpy())
            class_id = int(box.cls[0].cpu().numpy())
            class_name = model.names[class_id]
            
            detected_boxes.append(coords)
            confidences.append(confidence)
            
            # Store individual detection info
            detection_info = {
                'class_name': class_name,
                'confidence': confidence,
                'bbox': coords.tolist()
            }
            detection_results['detections'].append(detection_info)
            
            # Count classes
            if class_name in detection_results['class_counts']:
                detection_results['class_counts'][class_name] += 1
            else:
                detection_results['class_counts'][class_name] = 1
        
        # Calculate average confidence
        if confidences:
            detection_results['average_confidence'] = sum(confidences) / len(confidences)
        
        # Calculate Jaccard indices between all pairs of detections
        jaccard_indices = []
        for i in range(len(detected_boxes)):
            for j in range(i + 1, len(detected_boxes)):
                jaccard = calculate_jaccard_index(detected_boxes[i], detected_boxes[j])
                jaccard_indices.append({
                    'detection_pair': f"{detection_results['detections'][i]['class_name']} & {detection_results['detections'][j]['class_name']}",
                    'jaccard_index': jaccard
                })
        
        detection_results['jaccard_indices'] = jaccard_indices

    # Draw results on the image
    result_image = results[0].plot()  # This returns a numpy array with annotations

    # Convert result image (np array) to PIL Image
    result_pil = Image.fromarray(result_image)

    # Convert to byte array
    img_byte_arr = io.BytesIO()
    result_pil.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return img_byte_arr, detection_results