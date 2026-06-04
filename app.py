from flask import Flask, render_template, request, redirect, url_for, send_file, session, send_from_directory
from PyPDF2 import PdfMerger
from config import Config
from merged.models import db, History
import os
import uuid
import time

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

with app.app_context():
    db.create_all()


# =========================
# SESSION TRACKING
# =========================
def get_session_id():
    if "sid" not in session:
        session["sid"] = str(uuid.uuid4())
    return session["sid"]


# =========================
# HOME PAGE
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# MERGE PDFs
# =========================
@app.route("/merge", methods=["POST"])
def merge():
    files = request.files.getlist("files")

    if not files or len(files) < 2:
        return render_template(
        "index.html",
        error="Please select at least 2 PDF files."
    )

    merger = PdfMerger()

    valid_files = 0

    for file in files:
        if file and file.filename.lower().endswith(".pdf"):
            merger.append(file)
            valid_files += 1

    if valid_files < 2:
        return render_template(
        "index.html",
        error="Please upload at least 2 valid PDF files."
    )

    # Generate unique filename
    output_name = f"merged_{int(time.time())}_{uuid.uuid4().hex[:6]}.pdf"

    # Save inside static folder
    output_path = os.path.join(app.static_folder, output_name)

    merger.write(output_path)
    merger.close()

    # Save history
    record = History(
        session_id=get_session_id(),
        filename=output_name
    )

    db.session.add(record)
    db.session.commit()

    # Download immediately
    return send_file(output_path, as_attachment=True)


# =========================
# HISTORY PAGE
# =========================
@app.route("/history")
def history():
    sid = get_session_id()

    data = History.query.filter_by(session_id=sid)\
        .order_by(History.timestamp.desc())\
        .all()

    return render_template("history.html", history=data)


# =========================
# DOWNLOAD FILE
# =========================
@app.route("/download/<path:filename>")
def download_file(filename):
    file_path = os.path.join(app.static_folder, filename)

    if not os.path.exists(file_path):
        return f"File not found: {filename}", 404

    return send_from_directory(
        app.static_folder,
        filename,
        as_attachment=True
    )


# =========================
# DELETE FILE
# =========================
@app.route("/delete/<int:id>")
def delete(id):
    item = History.query.get_or_404(id)

    file_path = os.path.join(app.static_folder, item.filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("history"))


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)