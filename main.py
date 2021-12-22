from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

name = 'example'
original_image = Image.open('llama.jpg').convert("RGBA")
original_image_size = original_image.size

font = ImageFont.truetype('arial.ttf', 100)
text_size = font.getsize(name)
text_image = Image.new('RGBA', text_size, (255, 255, 255, 0))
text_draw = ImageDraw.Draw(text_image)
text_draw.text((0, 0), name, (255, 255, 255, 129), font=font)
rotated_text_image = text_image.rotate(45, expand=True, fillcolor=(0, 0, 0, 0))
rotated_text_image_size = rotated_text_image.size
watermarks_image = Image.new('RGBA', original_image_size, (255, 255, 255, 0))
x = original_image_size[0] // 2 - rotated_text_image_size[0] // 2
y = original_image_size[1] // 2 - rotated_text_image_size[1] // 2
watermarks_image.paste(rotated_text_image, (x, y))
combined_image = Image.alpha_composite(original_image, watermarks_image)
combined_image.show()
combined_image.save(f'lenna_3_{name}.png')
