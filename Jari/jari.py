import re
import sys

def interpret_jari(code):
    lines = [line.strip() for line in code.split("\n") if line.strip()]
    variables = {}
    functions = {}
    current_line = 0

    def evaluate_expression(expr, local_vars=None):
        if local_vars is None:
            local_vars = {}
        # Prioritize local variables over globals, and disable built-ins
        combined_vars = {**variables, **local_vars}
        combined_vars["__builtins__"] = {}  # Block access to built-in functions
        try:
            return eval(expr, combined_vars)
        except Exception as e:
            print(f"Error in evaluating expression: {expr}. Error: {e}")
            return None

    def execute_function(func_name, args):
        if func_name not in functions:
            print(f"Error: Function '{func_name}' not defined.")
            return None
        func = functions[func_name]
        if len(args) != len(func['params']):
            print(f"Error: Function '{func_name}' expects {len(func['params'])} arguments, but {len(args)} were provided.")
            return None
        local_vars = {param: arg for param, arg in zip(func['params'], args)}
        for line in func['body']:
            execute_line(line, local_vars)
        return local_vars.get('result', None)

    def execute_line(line, local_vars=None):
        nonlocal current_line
        if local_vars is None:
            local_vars = variables

        # Handle print (boliye) command
        if line.lower().startswith("boliye "):
            parts = line[7:].strip()
            output = []
            in_quote = False
            current_quoted = []
            i = 0
            while i < len(parts):
                if parts[i] == '"':
                    if in_quote:
                        output.append(''.join(current_quoted))
                        current_quoted = []
                        in_quote = False
                    else:
                        in_quote = True
                    i += 1
                elif in_quote:
                    current_quoted.append(parts[i])
                    i += 1
                else:
                    expr = parts[i:].strip()
                    evaluated = evaluate_expression(expr, local_vars)
                    output.append(str(evaluated) if evaluated is not None else "")
                    break
            print(" ".join(output))

        # Handle variable assignment
        elif " : " in line:
            var, value = line.split(" : ", 1)
            var = var.strip().lower()
            value = value.strip()
            evaluated_value = evaluate_expression(value, local_vars)
            if evaluated_value is not None:
                local_vars[var] = evaluated_value
            else:
                print(f"Error: Invalid value assignment for '{var}'.")

        # Handle loops (dohraye jbtk)
        elif line.lower().startswith("dohraye jbtk"):
            condition = line[13:].strip().rstrip(':')
            loop_body = []
            while current_line < len(lines) and lines[current_line].strip() != "{":
                current_line += 1
            current_line += 1  # Skip "{"
            while current_line < len(lines) and lines[current_line].strip() != "}":
                loop_body.append(lines[current_line].strip())
                current_line += 1
            current_line += 1  # Skip "}"
            while evaluate_expression(condition, variables):
                for body_line in loop_body:
                    execute_line(body_line)

        # Handle conditionals (agar)
        elif line.lower().startswith("agar "):
            condition = line[5:].strip().rstrip(':')
            if_body = []
            else_body = []
            in_else = False
            while current_line < len(lines):
                current_line_content = lines[current_line].strip()
                if current_line_content == "nito :":
                    in_else = True
                    current_line += 1
                elif current_line_content == "end":
                    current_line += 1
                    break
                elif in_else:
                    else_body.append(current_line_content)
                    current_line += 1
                else:
                    if_body.append(current_line_content)
                    current_line += 1
            if evaluate_expression(condition, variables):
                for body_line in if_body:
                    execute_line(body_line)
            else:
                for body_line in else_body:
                    execute_line(body_line)

        # Handle function calls
        elif "(" in line and ")" in line:
            func_name = line.split("(")[0].strip().lower()
            args = [evaluate_expression(arg.strip(), variables) for arg in line.split("(")[1].split(")")[0].split(",")]
            execute_function(func_name, args)

        # Skip braces
        elif line in ("{", "}"):
            pass

        else:
            print(f"Unknown command: {line}")

    # Main execution loop
    while current_line < len(lines):
        line = lines[current_line].strip()
        current_line += 1
        if not line or line in ("{", "}"):
            continue

        # Handle function definitions
        if "(" in line and ")" in line and " : " in line:
            func_part, body_part = line.split(" : ", 1)
            func_name = func_part.split("(")[0].strip().lower()
            params = [p.strip().lower() for p in func_part.split("(")[1].split(")")[0].split(",")]
            body = []
            if body_part.startswith("{"):
                while current_line < len(lines):
                    body_line = lines[current_line].strip()
                    if body_line == "}":
                        break
                    body.append(body_line)
                    current_line += 1
            body = [b.strip() for b in body if b.strip()]
            functions[func_name] = {'params': params, 'body': body}

        else:
            execute_line(line)

def main():
    if len(sys.argv) != 2:
        print("Usage: jari_interpreter <filename.jari>")
        return

    filename = sys.argv[1]
    if not filename.endswith(".jari"):
        print("Error: File must have a .jari extension.")
        return

    try:
        with open(filename, "r") as file:
            code = file.read()
        interpret_jari(code)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()