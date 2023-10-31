Creating installers for different platforms (macOS, Linux, Windows) with a proper user-friendly installation process is a complex task and often requires different tools and procedures for each platform. Here's a high-level guide to get you started, but note that you may need to dive deeper into platform-specific installer creation for a robust solution:

**1. Create the Executable:**

Before creating installers, make sure you have successfully built the executable for each platform (macOS, Linux, Windows) as described earlier.

**2. Platform-Specific Installer Tools:**

For each platform, you'll need to use platform-specific installer tools. Here are some options:

- **macOS**: Use `pkgbuild` to create a macOS package (.pkg). You can also use third-party tools like `Packages` for a more user-friendly installer.

- **Linux**: Linux distributions have different packaging formats. Common ones include `.deb` (Debian/Ubuntu) and `.rpm` (Red Hat/Fedora). You can use tools like `dpkg-deb` or `rpmbuild` to create packages.

- **Windows**: Use `Inno Setup` or `NSIS (Nullsoft Scriptable Install System)` to create Windows installers (.exe files). Both of these tools allow you to create user-friendly installers with terms and conditions.

**3. Create the Installer Scripts:**

For each platform, you need to create installer scripts that define the installation process. These scripts should include:

- Specify installation location.
- Include the executable and necessary assets.
- Define shortcuts or icons on the desktop/start menu.
- Display terms and conditions.
- Estimate the disk space required.
- Allow for uninstallation.
- Customize user interface (optional).

Here's a simple example of an Inno Setup script for Windows:

```innosetup
[Setup]
AppName=Your Application Name
AppVersion=1.0
DefaultDirName={pf}\YourApplication
OutputDir=Output
OutputBaseFilename=Installer
Compression=lzma2
SolidCompression=yes

[Tasks]
Name: desktopicon; Description: Create a desktop icon; GroupDescription: Additional icons:

[Files]
Source: "your_executable.exe"; DestDir: "{app}"
; Include other necessary files/assets

[Icons]
Name: "{group}\Your Application"; Filename: "{app}\your_executable.exe"
Name: "{commondesktop}\Your Application"; Filename: "{app}\your_executable.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\your_executable.exe"; Description: "Launch Your Application"

[Messages]
LicenseText=Your terms and conditions here.
```

**4. Build the Installers:**

Use the installer tools mentioned above to compile your scripts into installers for each platform. Follow the documentation of the specific tool to do this correctly.

**5. Distribute the Installers:**

After building the installers, you can distribute them through your website, email, or other distribution channels.

Please note that creating platform-specific installers can be a complex task, especially if you want a highly polished and user-friendly installation experience. You may consider using third-party tools or services that simplify the installer creation process and provide cross-platform support, such as WiX (for Windows), Install4j, or electron-builder for Electron-based applications.

Remember to review and comply with the licensing terms of the installer tools you use and ensure that you follow the guidelines and best practices for installer creation on each platform.