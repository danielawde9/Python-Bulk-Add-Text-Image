# to add row number in 2 location and row id 
# to add different prices from rows above f till x 
# to add balcony for o to x
from PIL import Image, ImageDraw, ImageFont

# Load your image not the reference
image_path = 'input-img.png'

# Define the output path
output_path_template = 'output_image_{}_{}.jpg'

# Define the font and size
font_size = 50
font = ImageFont.truetype("arial.ttf", font_size)

font_size2 = 40
font2 = ImageFont.truetype("arial.ttf", font_size2)

# Define row and column range
rows = "ABCDEFGHIJKLMNOPQRSTUVWX"
columns = list(range(1, 16))

# Define position templates for the text
rowPositionLeft = (1300, 431)
rowPositionRight = (1700, 431)
pricePositionLeft = (1280, 510)
pricePositionRight = (1680, 510)
ifBalconyPosition = (1280, 570)

# Loop through each seat and create an image
for row in rows:
    for col in columns:
        # Open the image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Determine text based on row and column
        if row in "ABCD":
            text = f'{row}       {col}'
            draw.text(rowPositionLeft, text, fill="white", font=font)
            draw.text(rowPositionRight, text, fill="black", font=font)
        elif row in "EFGHIJKLMNOPQRSTUVWX":
            if row in "EFGHIJKLMN":
                price = "$25"
            else:
                price = "$15"
                balcony = "Balcony"
                draw.text(ifBalconyPosition, balcony, fill="white", font=font2)

            text = f'{row}       {col}'
            draw.text(rowPositionLeft, text, fill="white", font=font)
            draw.text(rowPositionRight, text, fill="black", font=font)
            price_text = f'PRICE: {price}'
            draw.text(pricePositionLeft, price_text, fill="white", font=font2)
            draw.text(pricePositionRight, price_text, fill="black", font=font2)

        # Save the output image
        output_path = output_path_template.format(row, col)
        image.save(output_path)

        print(f"Image saved to {output_path}")