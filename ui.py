import streamlit as st
from app import process_image  # Assuming you have this function in app.py
import time


def display_detection_results(results):
    """Display detection results in a formatted manner"""
    
    # Overall Statistics
    st.subheader("📊 Detection Summary")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Detections", results['total_detections'])
    with col2:
        st.metric("Avg Confidence", f"{results['average_confidence']:.2%}")
    with col3:
        st.metric("Unique Classes", len(results['class_counts']))
    
    # Class Distribution
    if results['class_counts']:
        st.subheader("🏷️ Classification Results")
        
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Detected Classes:**")
            for class_name, count in results['class_counts'].items():
                st.write(f"• **{class_name}**: {count} detection(s)")
        
        with col2:
            # Display class distribution as a bar chart
            if len(results['class_counts']) > 1:
                st.bar_chart(results['class_counts'])
    
    # Individual Detections
    if results['detections']:
        st.subheader("🔍 Individual Detections")
        
        # Create a table of detections
        detection_data = []
        for i, detection in enumerate(results['detections']):
            detection_data.append({
                'ID': i + 1,
                'Class': detection['class_name'],
                'Confidence': f"{detection['confidence']:.2%}",
                'Bounding Box': f"({detection['bbox'][0]:.0f}, {detection['bbox'][1]:.0f}, {detection['bbox'][2]:.0f}, {detection['bbox'][3]:.0f})"
            })
        
        st.dataframe(detection_data, use_container_width=True)
    
    # Jaccard Index Results
    if results['jaccard_indices']:
        st.subheader("📐 Jaccard Index (IoU) Analysis")
        st.write("*Measures overlap between detected objects (0 = no overlap, 1 = perfect overlap)*")
        
        # Display Jaccard indices
        jaccard_data = []
        for jaccard_info in results['jaccard_indices']:
            jaccard_data.append({
                'Detection Pair': jaccard_info['detection_pair'],
                'Jaccard Index': f"{jaccard_info['jaccard_index']:.4f}",
                'Overlap Level': get_overlap_description(jaccard_info['jaccard_index'])
            })
        
        st.dataframe(jaccard_data, use_container_width=True)
        
        # Show average Jaccard index if there are multiple pairs
        if len(results['jaccard_indices']) > 1:
            avg_jaccard = sum([j['jaccard_index'] for j in results['jaccard_indices']]) / len(results['jaccard_indices'])
            st.info(f"**Average Jaccard Index**: {avg_jaccard:.4f}")
    else:
        st.info("📐 **Jaccard Index**: No overlapping detections found (only calculated when 2+ objects are detected)")


def get_overlap_description(jaccard_index):
    """Get a descriptive text for Jaccard index values"""
    if jaccard_index == 0:
        return "No Overlap"
    elif jaccard_index < 0.1:
        return "Minimal Overlap"
    elif jaccard_index < 0.3:
        return "Low Overlap"
    elif jaccard_index < 0.5:
        return "Moderate Overlap"
    elif jaccard_index < 0.7:
        return "High Overlap"
    else:
        return "Very High Overlap"


def main():
    st.set_page_config(page_title="Image Processor", page_icon="🖼️", layout="wide")
    st.title("Defect Detection Model 🎨")
    
    # File upload section
    uploaded_file = st.file_uploader(
        "Upload an image", 
        type=["png", "jpg", "jpeg", "bmp"],
        accept_multiple_files=False
    )
    
    if uploaded_file is not None:
        # Display original image in an expandable section
        with st.expander("▲ Original Image ▲", expanded=True):
           col1, col2, col3 = st.columns([1, 2, 1])
           with col2:
            st.image(uploaded_file, width=500)
        st.success("Image uploaded successfully!")
        
        # Add visual separator
        st.divider()
        
        # Process image section
        if st.button("✨ Process Image ✨", type="primary"):
            # Initialize progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Simulate processing stages
                for percent in range(0, 101, 20):
                    progress_bar.progress(percent)
                    status_text.text(f"Processing: {percent}% complete")
                    time.sleep(0.1)  # Simulate processing time
                
                # Actual processing (now returns both image and results)
                result_image, detection_results = process_image(uploaded_file)
                
                # Create two columns for results
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    # Display processed image
                    with st.expander("▼ Processed Result ▼", expanded=True):
                        st.image(result_image, use_container_width=True)
                        st.success("Processing complete!")
                
                with col2:
                    # Display detection results
                    with st.expander("▼ Analysis Results ▼", expanded=True):
                        display_detection_results(detection_results)
                
                st.balloons()
                
            except Exception as e:
                st.error(f"🚨 Error: {str(e)}")
                st.error("Please make sure your model file exists and the image is valid.")
            finally:
                # Clean up progress indicators
                progress_bar.empty()
                status_text.empty()


if __name__ == "__main__":
    main()