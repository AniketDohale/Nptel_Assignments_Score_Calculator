from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    best_of_scores = []
    text_input = ""
    digit_input = ""
    score_list = []
    sum_scores = 0 

    if request.method == 'POST':
        text_input = request.form.get('text_input')
        digit_input = request.form.get('digit_input')

        try:
            digit_input = int(digit_input) 
        except ValueError:
            return render_template('index.html', score='Invalid digit input', score_list=score_list)

        for line in text_input.split('\n'):
            for word in line.split():
                if word not in ['Week', 'Assignment', ':'] and len(word) > 3:
                    try:
                        score_list.append(float(word))
                    except ValueError:
                        continue

        score_list.sort(reverse=True)
        best_of_scores = score_list[:digit_input]

        for i in range(min(digit_input, len(score_list))):
            sum_scores += score_list[i]

        score = (sum_scores / digit_input) * 25 / 100

    return render_template('index.html', score=score, score_list=best_of_scores)

if __name__ == '__main__':
    app.run(debug=True)
