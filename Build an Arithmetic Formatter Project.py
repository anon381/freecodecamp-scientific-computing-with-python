
def arithmetic_arranger(problems, show_answers=False):

    # --- Error checks ---
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for prob in problems:
        parts = prob.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        # Check operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check digits only
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check length
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # width = max operand length + 2 (for operator + space)
        width = max(len(first), len(second)) + 2

        # Format each part
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dashes_line.append("-" * width)

        if show_answers:
            if operator == "+":
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            answers_line.append(result.rjust(width))

    # Join with 4 spaces
    arranged = "    ".join(first_line) + "\n" \
               + "    ".join(second_line) + "\n" \
               + "    ".join(dashes_line)

    if show_answers:
        arranged += "\n" + "    ".join(answers_line)

    return arranged
