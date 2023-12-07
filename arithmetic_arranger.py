def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for problem in problems:
        num1, op, num2 = problem.split()

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # if op not in ["+", "-", "*", "/"]:
        #     return "Error: Operator must be '+', '-', '*' or '/'."
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        length = max(len(num1), len(num2)) + 2

        if op == "+":
            res = int(num1) + int(num2)
        elif op == "-":
            res = int(num1) - int(num2)
        elif op == "*":
            res = int(num1) * int(num2)
        else:
            if int(num2) == 0:
                return "Error: Division by zero."
            res = int(num1) / int(num2)
            res = round(res, length)

        line1.append(num1.rjust(length))
        line2.append(op + num2.rjust(length - 1))
        line3.append("-" * length)
        line4.append(str(res).rjust(length))

    if display_answers:
        arranged_problems = (
            "    ".join(line1)
            + "\n"
            + "    ".join(line2)
            + "\n"
            + "    ".join(line3)
            + "\n"
            + "    ".join(line4)
        )
    else:
        arranged_problems = (
            "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
        )

    return arranged_problems
