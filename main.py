from speach import speach
from flask import Flask, render_template


@app.route('/voice')
def voices():
    try:
        text = speach()
    except:
        text = "Что-то пошло не так..."
    return render_template('create_card.html', text=text)