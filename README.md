# Flask Headless CMS - Schulungsbeispiel

Dieses Projekt demonstriert die Erstellung eines einfachen Headless CMS mit Flask als Backend und einem Tkinter-Client zur Anzeige der Produkte. Es enthält Funktionen zum Hinzufügen, Abrufen und Anzeigen von Produkten mit Bildern.

## Inhaltsverzeichnis
- [Überblick](#überblick)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
  - [Backend starten](#backend-starten)
  - [Produkte hinzufügen](#produkte-hinzufügen)
  - [Produkte anzeigen](#produkte-anzeigen)
- [Projektstruktur](#projektstruktur)

## Überblick
Dieses Projekt besteht aus drei Hauptkomponenten:
1. **Backend (Flask)**: Stellt eine REST-API zur Verwaltung von Produkten bereit.
2. **Datenpflege-Tool (Tkinter)**: Eine GUI-Anwendung zum Hinzufügen neuer Produkte.
3. **Benutzer-Client (Tkinter)**: Eine GUI-Anwendung zum Anzeigen der Produkte.

## Voraussetzungen
- Python 3.12
- Folgende Python-Bibliotheken:
  - Flask
  - Flask-SQLAlchemy
  - Pillow
  - Requests

## Installation
1. **Repository klonen**
   ```bash
   git clone https://github.com/benutzername/flask-headless-cms.git
   cd flask-headless-cms
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

### Backend starten
1. **Flask-Anwendung starten**
   ```bash
   python app.py
   ```

2. **Überprüfen Sie die Konsole**
   - Stellen Sie sicher, dass der Server unter `http://127.0.0.1:5000` läuft.

### Produkte hinzufügen
1. **Datenpflege-Tool starten**
   ```bash
   python datenpflege.py
   ```

2. **Produktinformationen eingeben und Bild auswählen**
   - Füllen Sie die Felder `Name`, `Price` und `Description` aus.
   - Klicken Sie auf `Browse`, um ein Bild auszuwählen.
   - Klicken Sie auf `Add Product`, um das Produkt hinzuzufügen.

### Produkte anzeigen
1. **Benutzer-Client starten**
   ```bash
   python client.py
   ```

2. **Produkte anzeigen**
   - Die Anwendung zeigt eine Liste aller hinzugefügten Produkte an, einschließlich der Bilder.

## Projektstruktur
```plaintext
flask-headless-cms/
│
├── app.py                    # Flask Backend
├── datenpflege.py            # Datenpflege-Tool zum Hinzufügen von Produkten
├── client.py                 # Benutzer-Client zur Anzeige von Produkten
├── requirements.txt          # Abhängigkeiten
├── static/
│   └── images/               # Verzeichnis für gespeicherte Bilder
└── templates/
    └── admin.html            # Admin-Seite für das Hinzufügen von Produkten über das Web
```

## Beispiel-Befehle

- **Backend starten**:
  ```bash
  python app.py
  ```

- **Datenpflege-Tool starten**:
  ```bash
  python datenpflege.py
  ```

- **Benutzer-Client starten**:
  ```bash
  python client.py
  ```

## Hinweise
- Stellen Sie sicher, dass der Ordner `static/images` existiert. Wenn nicht, erstellen Sie ihn manuell.
- Dieses Projekt ist als Schulungsbeispiel gedacht und kann nach Belieben erweitert werden.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.
