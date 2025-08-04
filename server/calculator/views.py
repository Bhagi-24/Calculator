from django.shortcuts import render
def home_view(request):
    return render(request, 'home.html')
def calculator_view(request):
    return render(request, 'calculator.html')
def result_view(request):
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
            else:
                result = 'Invalid operation'
        except Exception as e:
            result = f"Error: {str(e)}"
        context = {
            'num1': num1,
            'num2': num2,
            'operation': operation,
            'result': result
        }
        return render(request, 'result.html', context)
    else:
        return render(request, 'calculator.html')
