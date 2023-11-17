from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample tasks list
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if 0 <= task_id < len(tasks):
        if request.method == 'POST':
            tasks[task_id] = request.form['edited_task']
            return redirect(url_for('index'))
        else:
            return render_template('edit.html', task_id=task_id, task=tasks[task_id])
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
