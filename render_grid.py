from PIL import Image, ImageDraw, ImageFont
from digit_root_colors import digit_root, DIGIT_ROOT_COLORS

# RGB values for each color name
COLOR_RGB = {
    "Red":     (220,  50,  50),
    "Orange":  (255, 150,   0),
    "Yellow":  (240, 220,   0),
    "Green":   ( 50, 180,  50),
    "Blue":    ( 30, 100, 220),
    "Indigo":  ( 75,   0, 130),
    "Violet":  (180,  80, 220),
    "Pink":    (255, 150, 190),
    "Magenta": (210,   0, 180),
    "Black":   ( 30,  30,  30),
}

# Use light text on dark backgrounds, dark text on light backgrounds
LIGHT_TEXT = {"Blue", "Indigo", "Violet", "Magenta", "Black", "Red", "Green"}

CELL_SIZE = 80
ROWS      = 10  # 0-9 fill the first column, then 10-19, etc.


def get_text_color(color_name: str) -> tuple:
    return (240, 240, 240) if color_name in LIGHT_TEXT else (30, 30, 30)


def render_grid(start: int, end: int, output_path: str = "digit_root_grid.png"):
    """Render a column-major grid (ROWS rows) of numbers [start, end] colored by digit root.
    Numbers fill top-to-bottom then left-to-right, so 0-9 appear in column 0."""
    numbers = list(range(start, end + 1))
    cols = -(-len(numbers) // ROWS)  # ceiling division

    img_w = cols * CELL_SIZE
    img_h = ROWS * CELL_SIZE
    img = Image.new("RGB", (img_w, img_h), (245, 245, 245))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
    except OSError:
        font = ImageFont.load_default()

    for i, n in enumerate(numbers):
        col = i // ROWS
        row = i % ROWS
        x0 = col * CELL_SIZE
        y0 = row * CELL_SIZE
        x1 = x0 + CELL_SIZE - 1
        y1 = y0 + CELL_SIZE - 1

        root = digit_root(n)
        color_name = DIGIT_ROOT_COLORS.get(root, "Black")
        bg_color = COLOR_RGB[color_name]
        text_color = get_text_color(color_name)

        # Fill cell
        draw.rectangle([x0, y0, x1, y1], fill=bg_color)
        # Border
        draw.rectangle([x0, y0, x1, y1], outline=(200, 200, 200), width=1)

        # Center the number text
        label = str(n)
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = x0 + (CELL_SIZE - tw) // 2
        ty = y0 + (CELL_SIZE - th) // 2
        draw.text((tx, ty), label, fill=text_color, font=font)

    img.save(output_path)
    print(f"Saved to {output_path}  ({img_w}x{img_h} px, {ROWS} rows × {cols} cols)")


if __name__ == "__main__":
    render_grid(0, 1000, "digit_root_grid.png")
