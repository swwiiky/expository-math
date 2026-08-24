import tkinter as tk
from itertools import permutations

COLORS = ["green", "orange", "red", "blue", "purple"]


def draw_permutation(canvas, permutation, width, height):
    canvas.delete("all")
    n = len(permutation)
    spacing = width // (n + 1)
    radius = min(40, spacing // 3)

    for i, value in enumerate(permutation):
        x = (i + 1) * spacing
        y = height // 2
        color = COLORS[value - 1]
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="black")


def visualize_permutations(elements):
    all_permutations = list(permutations(elements))

    width = 800
    height = 400
    root = tk.Tk()
    root.title("Permutations of colored balls")

    label = tk.Label(root, text="Permutation: 0", font=("Arial", 16))
    label.pack(pady=10)

    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    idx = {'value': 0}

    def show_next_permutation():
        if idx['value'] < len(all_permutations):
            perm = all_permutations[idx['value']]
            label.config(text=f"Permutation: {idx['value'] + 1}")
            draw_permutation(canvas, perm, width, height)
            idx['value'] += 1
            root.after(200, lambda x: show_next_permutation(), None)

    show_next_permutation()

    root.mainloop()


if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5]
    visualize_permutations(elements)
