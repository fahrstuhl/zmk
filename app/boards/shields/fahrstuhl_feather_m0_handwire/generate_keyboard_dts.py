#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader

# TODO: read quotes.py for template and create matrix dts

pin_dict = {
        "name": "",
        "num": 0,
        "long_name": "",
        "port": "",
        "pin": "",
        "flags": "",
        "arduino_pin": "",
        }

def generate_rows():
    # arduino_pin, port, pin
    row_tuples = [
            (15, "portb", 8),
            (13, "porta", 17),

            (6, "porta", 20),
            (12, "porta", 19),

            (5, "porta", 15),
            (11, "porta", 16),

            (21, "porta", 23),
            (10, "porta", 18),

            (20, "porta", 22),
            (9, "porta", 7),
            ]
    rows = []
    for i, row in enumerate(row_tuples):
        rows.append({
            "name": "row",
            "num": i,
            "long_name": "row",
            "port": row[1],
            "pin": row[2],
            "flags": "(GPIO_ACTIVE_LOW)",
            "arduino_pin": row[0],
            })
    return rows

def generate_cols():
    # board_pin, port, pin
    col_tuples = [
            (16, "portb", 9),
            (17, "porta", 4),
            (18, "porta", 5),
            (19, "portb", 2),
            (24, "portb", 11),
            (23, "portb", 10),
            ]
    cols = []
    for i, col in enumerate(col_tuples):
        cols.append({
            "name": "col",
            "num": i,
            "long_name": "column",
            "port": col[1],
            "pin": col[2],
            "flags": "(GPIO_PULL_UP | GPIO_ACTIVE_LOW)",
            "arduino_pin": col[0],
            })
    return cols

def generate_matrix_transform(rows, cols):
    return []

def main():
    env = Environment(
            loader = FileSystemLoader("./"),
            )
    template = env.get_template('./fahrstuhl_feather_m0_handwire.overlay.j2')
    rows = generate_rows()
    cols = generate_cols()
    matrix_transform = generate_matrix_transform(rows, cols)
    overlay = template.render(rows = rows, cols = cols, matrix_transform = matrix_transform)
    with open('./fahrstuhl_feather_m0_handwire.overlay', 'w') as f:
        f.write(overlay)

if __name__ == "__main__":
    main()
