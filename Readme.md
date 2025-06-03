# 🎯 Object Detection with YOLOv8 and Streamlit UI

This project implements an interactive web interface for object detection using YOLOv8 and Streamlit, providing real-time visualization and analysis of detected objects. 🚀

## ✨ Features

### 🔍 Core Detection Features
- 🤖 Object detection using YOLOv8 model
- 📊 Detection result visualization
- 📈 Detailed analysis including:
  - 🔢 Total number of detections
  - 📋 Class-wise object counts
  - 📊 Average confidence scores
  - 🎯 Jaccard indices (IoU) between detected objects

### 🖥️ Interactive UI Features
- 📤 Drag-and-drop image upload
- ⚡ Real-time processing with progress indicator
- 📂 Expandable sections for original and processed images
- 📊 Interactive data visualizations:
  - 📋 Detection metrics dashboard
  - 📊 Class distribution charts
  - 📄 Detailed detection tables
  - 🎯 IoU analysis with descriptive overlap levels

## 📋 Prerequisites

- 🐍 Python 3.12
- 🌐 Virtual environment (recommended)

## 🛠️ Installation

1. 📥 Clone the repository
2. 🚀 Run the appropriate startup script for your operating system (see Quick Start below)

## 🚀 Quick Start

#### 🪟 Windows Users
```sh
server-up-windows.bat
```

#### 🍎 macOS/Linux Users
```sh
chmod +x server-up-macos.sh
./server-up-macos.sh
```

The web interface will automatically open in your default browser at `http://localhost:8501` 🌐

### 🗂️ Project Structure

```
📁 Project Root
├── 🐍 app.py                    # Core ML processing logic
├── 🖥️ ui.py                     # Streamlit UI implementation
├── 📋 requirements.txt          # Python dependencies
├── 🤖 MAJOR_PROJECT_ML_MODELYOLOv8.pt  # YOLOv8 model file
├── 🪟 server-up-windows.bat     # Windows startup script
├── 🍎 server-up-macos.sh       # macOS startup script
└── 📝 .gitignore               # Git ignore file
```

## ⚙️ Technical Implementation

### 🔧 Core Components
- `ultralytics`: 🤖 YOLOv8 implementation
- `streamlit`: 🌐 Web interface framework
- `PIL`: 🖼️ Image processing
- `numpy`: 🔢 Numerical operations
- `cv2`: 👁️ Computer vision tasks

### 🎨 UI Components
- **Layout**: 📐 Uses Streamlit's column system for responsive design
- **Interactive Elements**:
  - 📤 File uploader with type validation
  - 📊 Progress bars for processing feedback
  - 📂 Expandable sections for better organization
  - 📈 Dynamic metrics display
  - 🖱️ Interactive data tables and charts

### 🔄 Processing Pipeline
1. 📤 Image upload via Streamlit's file_uploader
2. ⚙️ Pre-processing and YOLOv8 inference
3. 📊 Results analysis including:
   - 📈 Detection statistics
   - 📊 Class distribution
   - 🎯 IoU calculations
4. 🎨 Visual presentation of results with:
   - 🖼️ Annotated images
   - 📊 Statistical dashboards
   - 🖱️ Interactive data tables

### 📊 Data Visualization
- ⚡ Real-time metrics display
- 📊 Bar charts for class distribution
- 📄 Formatted tables for detailed detection information
- 🎨 Color-coded IoU analysis