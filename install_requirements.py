#!/usr/bin/env python3

import subprocess
import sys
import os

def print_colored(text, color):
    """طباعة نص ملون في الطرفية"""
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m',
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['reset']}")

def check_root():
    """التحقق من صلاحيات الروت"""
    if os.geteuid() != 0:
        print_colored("يجب تشغيل السكربت بصلاحيات الروت (sudo)", 'red')
        sys.exit(1)

def install_system_tools():
    """تثبيت أدوات النظام"""
    print_colored("\n[+] جاري تثبيت أدوات النظام...", 'yellow')
    try:
        subprocess.run(['apt', 'update'], check=True)
        tools = ['nikto', 'wpscan', 'maltego', 'spiderfoot']
        for tool in tools:
            print_colored(f"\n[+] جاري تثبيت {tool}...", 'yellow')
            subprocess.run(['apt', 'install', '-y', tool], check=True)
            print_colored(f"[✓] تم تثبيت {tool} بنجاح", 'green')
    except subprocess.CalledProcessError as e:
        print_colored(f"\n[!] خطأ في تثبيت الأدوات: {str(e)}", 'red')
        sys.exit(1)

def install_python_packages():
    """تثبيت حزم Python"""
    print_colored("\n[+] جاري تثبيت حزم Python...", 'yellow')
    try:
        packages = ['colorama']
        for package in packages:
            print_colored(f"\n[+] جاري تثبيت {package}...", 'yellow')
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], check=True)
            print_colored(f"[✓] تم تثبيت {package} بنجاح", 'green')
    except subprocess.CalledProcessError as e:
        print_colored(f"\n[!] خطأ في تثبيت حزم Python: {str(e)}", 'red')
        sys.exit(1)

def main():
    """الدالة الرئيسية"""
    print_colored("\n=== تثبيت متطلبات أداة اختبار الاختراق ===", 'yellow')
    
    # التحقق من صلاحيات الروت
    check_root()
    
    # تثبيت الأدوات
    install_system_tools()
    
    # تثبيت حزم Python
    install_python_packages()
    
    print_colored("\n[✓] تم تثبيت جميع المتطلبات بنجاح!", 'green')
    print_colored("يمكنك الآن استخدام الأداة.", 'green')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print_colored("\n\n[!] تم إيقاف التثبيت", 'red')
        sys.exit(1)
    except Exception as e:
        print_colored(f"\n[!] خطأ غير متوقع: {str(e)}", 'red')
        sys.exit(1)