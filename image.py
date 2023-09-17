import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

# Set the page title
st.set_page_config(page_title="Streamlit Image Processing App")

# Title and description
st.title("Image Processing App")
st.write("Upload an image and apply various image processing operations.")

# Upload an image
image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if image is not None:
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Sidebar for image processing options
    st.sidebar.title("Image Processing Options")

    # Image enhancement options
    brightness = st.sidebar.slider("Brightness", 0.1, 3.0, 1.0)
    contrast = st.sidebar.slider("Contrast", 0.1, 3.0, 1.0)
    sharpness = st.sidebar.slider("Sharpness", 0.1, 3.0, 1.0)

    # Additional image processing options
    grayscale = st.sidebar.checkbox("Grayscale")
    blur = st.sidebar.checkbox("Apply Blur")

    rotate_angle = st.sidebar.slider("Rotate Angle", -180, 180, 0)
    flip_horizontal = st.sidebar.checkbox("Flip Horizontal")
    flip_vertical = st.sidebar.checkbox("Flip Vertical")

    # Option to select the area to crop
    crop = st.sidebar.checkbox("Crop")

    if crop:
        # Define cropping coordinates
        st.sidebar.write("Specify cropping coordinates:")
        left = st.sidebar.number_input("Left", value=0)
        top = st.sidebar.number_input("Top", value=0)
        right = st.sidebar.number_input("Right", value=0)
        bottom = st.sidebar.number_input("Bottom", value=0)

    apply_filter = st.sidebar.selectbox("Apply Filter", ["None", "Vintage", "Black and White"])

    # Apply image processing operations
    img = Image.open(image)
    
    if rotate_angle != 0:
        img = img.rotate(rotate_angle, expand=True)

    if flip_horizontal:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    if flip_vertical:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

    if crop:
        # Crop the image based on the user-defined coordinates
        img = img.crop((left, top, right, bottom))

    if apply_filter == "Vintage":
        # Apply vintage filter
        img = img.convert("L")
        img = ImageEnhance.Contrast(img).enhance(1.5)
    elif apply_filter == "Black and White":
        # Apply black and white filter
        img = img.convert("L")

    if grayscale:
        img = img.convert("L")

    if blur:
        img = img.filter(ImageFilter.BLUR)

    img = ImageEnhance.Brightness(img).enhance(brightness)

    # Check if contrast is not zero before applying
    if contrast != 0:
        img = ImageEnhance.Contrast(img).enhance(contrast)

    img = ImageEnhance.Sharpness(img).enhance(sharpness)

    # Display the processed image
    st.image(img, caption="Processed Image", use_column_width=True)

    # Download button for the processed image
    st.download_button(
        "Download Processed Image",
        img.tobytes(),
        file_name="processed_image.jpg",
        key="processed_image",
    )

    # Add option to reset the image
    if st.button("Reset Image"):
        img = Image.open(image)

# Add some additional text
st.write("Made By Rohit.")
