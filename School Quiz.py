class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "1. In an arithmetic sequence, u1 = -5 and d = 3. Find the 8th term\n",
     "2. Let f(x) = x^2 + x - 6. Write down the y-intercept of the graph of f\n",
     "3. Find the zeros (roots, solutions)\n",
     '4. h controls the horizontal translation\n(a)True\n(b)False\n',
     '5. Let y=5+2f(3(x-1))\nFind the number that represents the vertical translation\n',
     '6. What about the horizontal stretch?\n',
     '7. Or the vertical stretch?\n',
     '8. Fully describe the transformations which map y=f(x) onto: y=-f(x+1) + 3\nI. Is it a a reflection in the x-axis\nII. A horizontal translation of -1\nIII. A vertical translation of 3\n\n(a)I only\n(b)I and II\n(c)I, II and III\n',
     '9. Find the 4th term in the expansion of (4y+x)^4\n',
     '10. The speed of light is 300,000 kilometres per second.\nThe average distance from the Sun to the Earth is 149.6 million km.\nCalculate the time, in minutes, it takes for light from the Sun to reach the Earth.\n',
]

questions = [
     Question(question_prompts[0], "16"),
     Question(question_prompts[1], "-6"),
     Question(question_prompts[2], "2,-3"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], '5'),
     Question(question_prompts[5], '1/3'),
     Question(question_prompts[6], '2'),
     Question(question_prompts[7], 'c'),
     Question(question_prompts[8], '16yx^3'),
     Question(question_prompts[9], '8 minutes and 31 seconds'),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
