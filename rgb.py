import colorsys
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def get_triad_colors_and_hues(hue):
    hue = hue / 360.0
    hues = [(hue + i / 3) % 1.0 for i in range(3)]
    rgb_colors = [colorsys.hsv_to_rgb(h, 1.0, 1.0) for h in hues]
    hues_degrees = [h * 360 for h in hues]
    return rgb_colors, hues_degrees

def plot_colors(colors):
    fig, ax = plt.subplots(figsize=(8, 2))
    for i, color in enumerate(colors):
        ax.add_patch(patches.Rectangle((i, 0), 1, 1, facecolor=color))
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    hue = float(input("色相を入力してください (0-360): "))
    triad_colors, triad_hues = get_triad_colors_and_hues(hue)
    print(f"トライアド色相 (度数): {triad_hues}")
    plot_colors(triad_colors)
