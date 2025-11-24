from PIL import Image, ImageDraw

def create_mic_icon():
    # Create a 256x256 image with transparent background
    size = (256, 256)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Colors
    bg_color = "#2b2b2b"
    mic_color = "#3B8ED0"
    
    # Draw rounded background (circle)
    draw.ellipse([10, 10, 246, 246], fill=bg_color)
    
    # Draw Microphone body (simple capsule shape)
    mic_x = 128
    mic_y = 128
    mic_w = 60
    mic_h = 100
    
    # Mic head
    draw.rectangle(
        [mic_x - mic_w//2, mic_y - mic_h//2, mic_x + mic_w//2, mic_y + mic_h//2], 
        fill=mic_color
    )
    # Round the top and bottom of mic head
    draw.ellipse([mic_x - mic_w//2, mic_y - mic_h//2 - mic_w//2, mic_x + mic_w//2, mic_y - mic_h//2 + mic_w//2], fill=mic_color)
    draw.ellipse([mic_x - mic_w//2, mic_y + mic_h//2 - mic_w//2, mic_x + mic_w//2, mic_y + mic_h//2 + mic_w//2], fill=mic_color)

    # Save as ICO
    img.save('app_icon.ico', format='ICO', sizes=[(256, 256)])

if __name__ == "__main__":
    create_mic_icon()
