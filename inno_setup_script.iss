; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "unGSTfy"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Ashfaque Alam"
#define MyAppURL "https://ashfaque.co.in/"
#define MyAppExeName "unGSTfy.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{6F459C5E-A93A-46EE-BF6F-D9E3F0A0FE5B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=E:\NO_BACKUP\DjangoProjects\unGSTfy_PyQt\LICENSE.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=E:\NO_BACKUP\DjangoProjects\unGSTfy_PyQt\_temp
OutputBaseFilename=ungstfy_setup
SetupIconFile=E:\NO_BACKUP\DjangoProjects\unGSTfy_PyQt\assets\icons\setup_logo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "E:\NO_BACKUP\DjangoProjects\unGSTfy_PyQt\dist\unGSTfy\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\NO_BACKUP\DjangoProjects\unGSTfy_PyQt\dist\unGSTfy\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
