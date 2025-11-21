from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'portfolio_elevate'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            flash(f'Thank you {name}! Your message has been received.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
