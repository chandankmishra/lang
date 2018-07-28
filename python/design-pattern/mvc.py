@app.route('/')
def example_page():
    db = get_db()
    queury = db.execute('select * from entries order by id desc')
    entries = query.fetchall()
    return render_template('example_page.html', entries=entries)
