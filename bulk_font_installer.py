import os
import shutil
import winreg
import ctypes

def install_font_per_user(font_path):
    user_fonts_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Windows', 'Fonts')
    os.makedirs(user_fonts_dir, exist_ok=True)

    font_file = os.path.basename(font_path)
    dest_path = os.path.join(user_fonts_dir, font_file)

    if not os.path.exists(dest_path):
        shutil.copy(font_path, dest_path)

    font_name = os.path.splitext(font_file)[0]

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                        r"Software\Microsoft\Windows NT\CurrentVersion\Fonts",
                        0, winreg.KEY_SET_VALUE) as reg_key:
        winreg.SetValueEx(reg_key, font_name, 0, winreg.REG_SZ, dest_path)

    if ctypes.windll.gdi32.AddFontResourceW(dest_path):
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x001D, 0, 0)
        print(f"Installed {font_file} for current user.")
    else:
        print(f"Failed to install {font_file}.")

def install_all_fonts_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        raise Exception(f"[!] Invalid folder: {folder_path}")

    font_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".ttf")]
    if not font_files:
        raise Exception(f"[!] No .ttf files found in folder: {folder_path}")

    for font_file in font_files:
        font_path = os.path.join(folder_path, font_file)
        install_font_per_user(font_path)
