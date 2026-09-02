"""Generate all cover images for Book 3: Healthy AI Implementation Roadmap for Hospitals"""
from PIL import Image, ImageDraw, ImageFont
import math, os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors
NAVY = (11, 36, 71)       # #0B2447
TEAL = (79, 209, 197)     # #4FD1C5
WHITE = (255, 255, 255)
LIGHT_TEAL = (150, 230, 220)
DARK_BLUE = (8, 25, 50)
ACCENT_ORANGE = (255, 183, 77)

# Fonts
def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)
        return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)
    except:
        return ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", size)

def get_segoe_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", size)
        return ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", size)
    except:
        return get_font(size, bold)

def draw_gradient_bg(draw, w, h, color1, color2):
    """Draw vertical gradient background"""
    for y in range(h):
        ratio = y / h
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def draw_grid_dots(draw, w, h, spacing=40, color=(79, 209, 197, 15)):
    """Draw subtle grid dot pattern"""
    for x in range(0, w, spacing):
        for y in range(0, h, spacing):
            draw.ellipse([x-1, y-1, x+1, y+1], fill=color)

def draw_ecg_line(draw, w, h, y_center, color=TEAL, thickness=3):
    """Draw a decorative ECG/heartbeat line"""
    points = []
    x = 0
    while x < w:
        # Normal flat line
        points.append((x, y_center))
        x += 20
        # Small bump
        points.append((x, y_center - 8))
        x += 10
        points.append((x, y_center))
        x += 30
        # Big spike (QRS complex)
        points.append((x, y_center))
        x += 10
        points.append((x, y_center + 15))
        x += 5
        points.append((x, y_center - 25))
        x += 5
        points.append((x, y_center + 10))
        x += 5
        points.append((x, y_center))
        x += 40
        # T-wave
        points.append((x, y_center - 8))
        x += 15
        points.append((x, y_center))
        x += 50

    if len(points) > 1:
        draw.line(points, fill=color, width=thickness)

def draw_bokeh_particles(draw, w, h, count=15, color=TEAL):
    """Draw soft bokeh light particles"""
    import random
    random.seed(42)
    for _ in range(count):
        x = random.randint(0, w)
        y = random.randint(0, h)
        r = random.randint(3, 12)
        opacity = random.randint(20, 60)
        c = (*color[:3], opacity) if len(color) == 4 else (*color, opacity)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=c)

def draw_medical_cross(draw, x, y, size, color=TEAL):
    """Draw a small medical cross"""
    t = size // 4
    draw.rectangle([x-t, y-size//2, x+t, y+size//2], fill=color)
    draw.rectangle([x-size//2, y-t, x+size//2, y+t], fill=color)

def center_text(draw, text, y, w, font, fill=WHITE):
    """Draw centered text"""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (w - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def create_kdp_cover():
    """Create KDP full cover (1600x2560)"""
    w, h = 1600, 2560
    img = Image.new('RGB', (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Gradient background
    draw_gradient_bg(draw, w, h, DARK_BLUE, NAVY)

    # Grid dots
    draw_grid_dots(draw, w, h, spacing=50, color=(79, 209, 197, 20))

    # Bokeh particles
    draw_bokeh_particles(draw, w, h, count=25, color=TEAL)

    # ECG line across lower third
    draw_ecg_line(draw, w, h, y_center=int(h * 0.65), color=TEAL, thickness=4)

    # Medical cross top-right
    draw_medical_cross(draw, w - 150, 120, 40, TEAL)

    # Series label
    font_series = get_font(36)
    center_text(draw, "PRACTICAL AI IN HEALTHCARE", 180, w, font_series, TEAL)

    # Divider line
    draw.line([(w//2 - 200, 240), (w//2 + 200, 240)], fill=TEAL, width=2)

    # Book number
    font_booknum = get_font(48, bold=True)
    center_text(draw, "BOOK 3", 270, w, font_booknum, ACCENT_ORANGE)

    # Main title - wrap if needed
    font_title = get_font(72, bold=True)
    title_lines = wrap_text("Healthy AI Implementation Roadmap for Hospitals", font_title, w - 200, draw)
    y = 400
    for line in title_lines:
        center_text(draw, line, y, w, font_title, WHITE)
        y += 90

    # Subtitle
    font_subtitle = get_font(38)
    subtitle_lines = wrap_text("From Pilot to Production", font_subtitle, w - 200, draw)
    y += 30
    for line in subtitle_lines:
        center_text(draw, line, y, w, font_subtitle, LIGHT_TEAL)
        y += 50

    font_subtitle2 = get_font(32)
    center_text(draw, "A Step-by-Step Playbook for Hospital Leaders", y + 10, w, font_subtitle2, LIGHT_TEAL)
    center_text(draw, "and Analysts", y + 55, w, font_subtitle2, LIGHT_TEAL)

    # Bottom decorative line
    draw.line([(w//2 - 250, h - 350), (w//2 + 250, h - 350)], fill=TEAL, width=2)

    # Author name
    font_author = get_font(44, bold=True)
    center_text(draw, "MOHAMMED IMTHIYAZ A", h - 300, w, font_author, WHITE)

    # Author title
    font_authtitle = get_font(26)
    center_text(draw, "Senior Quality Analyst | Healthcare AI Specialist", h - 240, w, font_authtitle, TEAL)

    # Bottom accent bar
    draw.rectangle([(0, h - 8), (w, h)], fill=TEAL)

    path = os.path.join(OUT_DIR, "cover_kdp_full.jpg")
    img.save(path, "JPEG", quality=95, dpi=(72, 72))
    print(f"Created: {path} ({w}x{h})")

def create_gumroad_cover():
    """Create Gumroad horizontal cover (1280x720)"""
    w, h = 1280, 720
    img = Image.new('RGB', (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Gradient
    draw_gradient_bg(draw, w, h, DARK_BLUE, NAVY)

    # Grid dots
    draw_grid_dots(draw, w, h, spacing=35, color=(79, 209, 197, 15))

    # Bokeh
    draw_bokeh_particles(draw, w, h, count=12, color=TEAL)

    # ECG line
    draw_ecg_line(draw, w, h, y_center=int(h * 0.7), color=TEAL, thickness=3)

    # Medical cross
    draw_medical_cross(draw, w - 100, 60, 25, TEAL)

    # Series label
    font_series = get_font(22)
    center_text(draw, "PRACTICAL AI IN HEALTHCARE  |  BOOK 3", 40, w, font_series, TEAL)

    # Divider
    draw.line([(w//2 - 180, 80), (w//2 + 180, 80)], fill=TEAL, width=1)

    # Main title
    font_title = get_font(52, bold=True)
    title_lines = wrap_text("Healthy AI Implementation Roadmap for Hospitals", font_title, w - 150, draw)
    y = 120
    for line in title_lines:
        center_text(draw, line, y, w, font_title, WHITE)
        y += 65

    # Subtitle
    font_subtitle = get_font(28)
    center_text(draw, "From Pilot to Production", y + 15, w, font_subtitle, LIGHT_TEAL)
    center_text(draw, "A Step-by-Step Playbook for Hospital Leaders and Analysts", y + 55, w, get_font(22), LIGHT_TEAL)

    # Bottom
    draw.line([(w//2 - 200, h - 100), (w//2 + 200, h - 100)], fill=TEAL, width=1)
    font_author = get_font(28, bold=True)
    center_text(draw, "MOHAMMED IMTHIYAZ A", h - 80, w, font_author, WHITE)

    # Bottom accent bar
    draw.rectangle([(0, h - 4), (w, h)], fill=TEAL)

    path = os.path.join(OUT_DIR, "cover_gumroad.jpg")
    img.save(path, "JPEG", quality=95, dpi=(72, 72))
    print(f"Created: {path} ({w}x{h})")

def create_thumbnail():
    """Create square thumbnail (600x600)"""
    w, h = 600, 600
    img = Image.new('RGB', (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Gradient
    draw_gradient_bg(draw, w, h, DARK_BLUE, NAVY)

    # Grid dots
    draw_grid_dots(draw, w, h, spacing=30, color=(79, 209, 197, 15))

    # ECG line
    draw_ecg_line(draw, w, h, y_center=int(h * 0.72), color=TEAL, thickness=2)

    # Series label
    font_series = get_font(16)
    center_text(draw, "PRACTICAL AI IN HEALTHCARE", 30, w, font_series, TEAL)

    # Book 3
    font_booknum = get_font(24, bold=True)
    center_text(draw, "BOOK 3", 60, w, font_booknum, ACCENT_ORANGE)

    # Title - wrap
    font_title = get_font(32, bold=True)
    title_lines = wrap_text("Healthy AI Implementation Roadmap for Hospitals", font_title, w - 80, draw)
    y = 110
    for line in title_lines:
        center_text(draw, line, y, w, font_title, WHITE)
        y += 40

    # Subtitle
    font_sub = get_font(16)
    center_text(draw, "From Pilot to Production", y + 15, w, font_sub, LIGHT_TEAL)
    center_text(draw, "A Step-by-Step Playbook", y + 40, w, font_sub, LIGHT_TEAL)

    # Author
    draw.line([(w//2 - 100, h - 80), (w//2 + 100, h - 80)], fill=TEAL, width=1)
    font_author = get_font(18, bold=True)
    center_text(draw, "MOHAMMED IMTHIYAZ A", h - 60, w, font_author, WHITE)

    # Bottom bar
    draw.rectangle([(0, h - 4), (w, h)], fill=TEAL)

    path = os.path.join(OUT_DIR, "cover_kdp_thumbnail.jpg")
    img.save(path, "JPEG", quality=95, dpi=(72, 72))
    print(f"Created: {path} ({w}x{h})")

def create_google_play_cover():
    """Create Google Play cover (1024x1600)"""
    w, h = 1024, 1600
    img = Image.new('RGB', (w, h), NAVY)
    draw = ImageDraw.Draw(img)

    # Gradient
    draw_gradient_bg(draw, w, h, DARK_BLUE, NAVY)

    # Grid dots
    draw_grid_dots(draw, w, h, spacing=40, color=(79, 209, 197, 18))

    # Bokeh
    draw_bokeh_particles(draw, w, h, count=18, color=TEAL)

    # ECG line
    draw_ecg_line(draw, w, h, y_center=int(h * 0.65), color=TEAL, thickness=3)

    # Medical cross
    draw_medical_cross(draw, w - 100, 80, 30, TEAL)

    # Series
    font_series = get_font(28)
    center_text(draw, "PRACTICAL AI IN HEALTHCARE", 120, w, font_series, TEAL)

    # Divider
    draw.line([(w//2 - 150, 170), (w//2 + 150, 170)], fill=TEAL, width=1)

    # Book 3
    font_booknum = get_font(36, bold=True)
    center_text(draw, "BOOK 3", 190, w, font_booknum, ACCENT_ORANGE)

    # Title
    font_title = get_font(56, bold=True)
    title_lines = wrap_text("Healthy AI Implementation Roadmap for Hospitals", font_title, w - 150, draw)
    y = 280
    for line in title_lines:
        center_text(draw, line, y, w, font_title, WHITE)
        y += 70

    # Subtitle
    font_subtitle = get_font(30)
    center_text(draw, "From Pilot to Production", y + 20, w, font_subtitle, LIGHT_TEAL)
    font_subtitle2 = get_font(24)
    center_text(draw, "A Step-by-Step Playbook for Hospital Leaders", y + 65, w, font_subtitle2, LIGHT_TEAL)
    center_text(draw, "and Analysts", y + 100, w, font_subtitle2, LIGHT_TEAL)

    # Bottom
    draw.line([(w//2 - 180, h - 200), (w//2 + 180, h - 200)], fill=TEAL, width=1)
    font_author = get_font(36, bold=True)
    center_text(draw, "MOHAMMED IMTHIYAZ A", h - 160, w, font_author, WHITE)

    font_authtitle = get_font(20)
    center_text(draw, "Senior Quality Analyst | Healthcare AI Specialist", h - 110, w, font_authtitle, TEAL)

    # Bottom bar
    draw.rectangle([(0, h - 6), (w, h)], fill=TEAL)

    path = os.path.join(OUT_DIR, "cover_google_play.jpg")
    img.save(path, "JPEG", quality=95, dpi=(72, 72))
    print(f"Created: {path} ({w}x{h})")

if __name__ == "__main__":
    create_kdp_cover()
    create_gumroad_cover()
    create_thumbnail()
    create_google_play_cover()
    print("\nAll covers generated!")
