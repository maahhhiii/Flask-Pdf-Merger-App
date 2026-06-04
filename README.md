# Flask PDF Merger

A simple web application built with Flask that allows users to merge multiple PDF files into a single PDF document.

## Features

* Upload multiple PDF files
* Merge PDFs into one document
* Instant download of merged PDF
* Session-based merge history
* Download previously merged files
* Delete files from history
* Responsive and modern UI

## Technologies Used

* Python
* Flask
* SQLAlchemy
* SQLite
* PyPDF2
* HTML
* CSS

## Installation

1. Clone the repository

```bash
git clone https://github.com/maahhhiii/Flask-Pdf-Merger-App.git
cd Flask-Pdf-Merger-App
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the application

```bash
python app.py
```

6. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
Flask-Pdf-Merger-App/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   └── merged_*.pdf
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── merged/
│   └── models.py
│
└── uploads/
```

## Usage

1. Select two or more PDF files.
2. Click "Merge PDFs".
3. Download the merged file.
4. View previous merged files in History.
5. Download or delete files from History.

## Future Improvements

* Drag and drop upload
* PDF page reordering
* PDF compression
* User authentication
* Cloud storage integration

## License

This project is licensed under the MIT License.
