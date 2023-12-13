def arithmetic_arranger(problems, show_answers=False):
  # Check if there are more than 5 problems
  if len(problems) > 5:
      return "Error: Too many problems."

  # Initialize list to store each line of the arranged problems
  arranged_problems = [""] * 4

  for problem in problems:
      try:
          # Split each problem into operands and operator
          operand1, operator, operand2 = problem.split()
      except ValueError:
          return "Error: Invalid problem format."

      # Validate that operands contain only digits
      if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."

      # Validate that operands are not more than four digits
      if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."

      # Validate that operator is either '+' or '-'
      if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."

      # Determine the maximum length of the operands for formatting
      max_length = max(len(operand1), len(operand2)) + 2

      # Format and append the first operand to the first line
      arranged_problems[0] += operand1.rjust(max_length) + "    "
      # Format and append the operator and second operand to the second line
      arranged_problems[1] += operator + operand2.rjust(max_length - 1) + "    "
      # Append the line of dashes to the third line
      arranged_problems[2] += "-" * max_length + "    "

      # If the answers are to be shown, calculate and format the answer
      if show_answers:
          if operator == '+':
              answer = str(int(operand1) + int(operand2))
          elif operator == '-':
              answer = str(int(operand1) - int(operand2))
          # Append the answer to the fourth line
          arranged_problems[3] += answer.rjust(max_length) + "    "

  # Remove extra spaces at the end of each line
  arranged_problems = [line.rstrip() for line in arranged_problems if line.strip() != ""]

  # Combine the lines into a single string separated by newlines
  result = "\n".join(arranged_problems)
  return result