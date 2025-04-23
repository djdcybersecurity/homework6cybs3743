from fontTools.ttLib import TTFont

# Adjust this path to where your .ttf lives
font_path = "static/Roboto-Regular.ttf"
out_path  = "static/Roboto-Scrambled.ttf"

# Load the font
font = TTFont(font_path)

# Grab the first cmap subtable that looks like unicode
cmap_tables = [t for t in font['cmap'].tables if t.isUnicode()]
if not cmap_tables:
    raise RuntimeError("No Unicode cmap subtable found")
cmap = cmap_tables[0].cmap

# Example swap: 'A' <-> 'B'
a, b = ord('A'), ord('B')
glyph_for_a = cmap.get(a)
glyph_for_b = cmap.get(b)
if glyph_for_a and glyph_for_b:
    cmap[a], cmap[b] = glyph_for_b, glyph_for_a
else:
    print("One of A or B wasn't present in cmap")

# Save the new font
font.save(out_path)
print(f"Saved scrambled font to {out_path}")
