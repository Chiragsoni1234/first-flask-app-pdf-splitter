from flask import Flask, render_template, request, redirect, url_for, send_file, session
import pdfsplitter
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route("/")
def upload():
    return render_template("file_upload.html")

@app.route("/success", methods=["POST"])
def success():
    # Retrieve form data
    start_page = int(request.form['start'])
    end_page = int(request.form['end'])
    f = request.files['file']
    file_name = f.filename

    # Save the uploaded file
    f.save(file_name)

    # Store data in session
    session['start_page'] = start_page
    session['end_page'] = end_page
    session['file_name'] = file_name

    return render_template("success.html", start=start_page, end=end_page, name=file_name)

@app.route("/convert")
def cropper():
    # Retrieve data from session
    start_page = session.get('start_page')
    end_page = session.get('end_page')
    file_name = session.get('file_name')

    # Call the cropper function
    pdfsplitter.cropper(start_page, end_page, file_name)

    return redirect(url_for('download'))

@app.route("/download")
def download():
    file_name = session.get('file_name')
    cropped_file_name = file_name.split(".")[0] + "cropped.pdf"
    
    # Check if the file exists before sending it
    if os.path.exists(cropped_file_name):
        return send_file(cropped_file_name, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
