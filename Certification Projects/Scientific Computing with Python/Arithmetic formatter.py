def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, operator, right = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left), len(right)) + 2

        top_line.append(left.rjust(width))
        bottom_line.append(operator + right.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))

    arranged_problems = (
        '    '.join(top_line) + '\n' +
        '    '.join(bottom_line) + '\n' +
        '    '.join(dashes)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems


# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

