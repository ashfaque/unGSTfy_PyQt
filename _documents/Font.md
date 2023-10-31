To include custom fonts in your PyQt6 application so that they are available regardless of whether the system has them installed, you can embed the fonts as resources. Here's a detailed guide:

**1. Prepare Your Fonts:**

First, collect the font files you want to include in your application. Let's assume you have a custom font named `MyFont.ttf`. Place the font file in a folder within your project directory, similar to how you organized assets:

```
project_directory/
    └── your_app/
        ├── assets/
        │   ├── image.png
        │   ├── video.mp4
        │   └── document.pdf
        ├── fonts/
        │   └── MyFont.ttf
```

**2. Create a `.qrc` File for Fonts:**

Just like you did for assets, you need to create a `.qrc` file to include fonts. Create a file named `fonts.qrc`:

```xml
<!DOCTYPE RCC>
<RCC version="1.0">
    <qresource>
        <file>fonts/MyFont.ttf</file>
    </qresource>
</RCC>
```

**3. Compile the Resource File:**

Compile the `.qrc` file into a Python module using the `pyrcc6` command. Run this in your terminal:

```bash
pyrcc6 -o resources.py fonts.qrc
```

This generates a `resources.py` file that contains your fonts.

**4. Use the Resource File in Your Code:**

In your PyQt6 application code, import the resource module and load the fonts as follows:

```python
from PyQt6.QtCore import QResource, QFile, QByteArray
from PyQt6.QtGui import QFontDatabase

# Initialize the QResource
QResource.registerResource("resources.rcc")

# Access a font
font_path = QFile(":/fonts/MyFont.ttf")
if font_path.open(QIODevice.OpenMode.ReadOnly):
    font_data = QByteArray(font_path.readAll())
    # Register the font with QFontDatabase
    QFontDatabase.addApplicationFontFromData(font_data)
    
# Now, you can use the font in your application
font = QFont("MyFont", 12)  # Use the font with a suitable family name
```

**5. Build the Executable:**

After configuring your fonts using Qt's `QResource`, build the executable as described in the previous guide.

By following these steps, you can ensure that your PyQt6 application includes the custom fonts and makes them available to the application, even if the target system does not have those fonts installed. This way, your fonts will display correctly on any system where your application is deployed.