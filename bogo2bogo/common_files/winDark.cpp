// winDark.cpp - Windows dark theme functions
//
#include <QTextStream>
#include <QtCore>
#include <QtGui>
#include <QtWidgets>
#include <QPalette>

#ifdef Q_OS_WINDOWS
// for black colored titlebars in Windows dark theme
#include <dwmapi.h>
#include <windows.h>
#ifdef _MSC_VER
   #pragma comment(lib, "Dwmapi.lib")
#endif
#endif
#include "winDark.h"

namespace winDark {

   QColor getPaletteColor(QPalette::ColorRole colorRole, QPalette::ColorGroup colorGroup /*= QPalette::Active*/)
   {
      QPalette pal = qApp->palette();
      QColor color = pal.color(colorGroup, colorRole);
      return color;
   }

   void _setDarkTitlebar(HWND hwnd, bool dark /*= true*/)
   {
   #ifdef Q_OS_WINDOWS
      HMODULE hUxtheme = LoadLibraryExW(L"uxtheme.dll", NULL, LOAD_LIBRARY_SEARCH_SYSTEM32);
      HMODULE hUser32 = GetModuleHandleW(L"user32.dll");
      fnAllowDarkModeForWindow AllowDarkModeForWindow = reinterpret_cast<fnAllowDarkModeForWindow>(
         GetProcAddress(hUxtheme, MAKEINTRESOURCEA(133)));
      fnSetPreferredAppMode SetPreferredAppMode = reinterpret_cast<fnSetPreferredAppMode>(
         GetProcAddress(hUxtheme, MAKEINTRESOURCEA(135)));
      fnSetWindowCompositionAttribute SetWindowCompositionAttribute
         = reinterpret_cast<fnSetWindowCompositionAttribute>(
            GetProcAddress(hUser32, "SetWindowCompositionAttribute"));

      SetPreferredAppMode(AllowDark);
      BOOL Dark = (dark ? TRUE : FALSE);
      AllowDarkModeForWindow(hwnd, Dark);
      WINDOWCOMPOSITIONATTRIBDATA data = {WCA_USEDARKMODECOLORS, &Dark, sizeof(Dark)};
      SetWindowCompositionAttribute(hwnd, &data);
   #endif
      // if not Windows, do nothing!!
   }

   // --------------------------------------------------------------------------------------------
   // ThemeSwitcher class implementation
   //
   QPalette *ThemeSwitcher::_darkPalette = nullptr;
   QPalette *ThemeSwitcher::_lightPalette = nullptr;

   // @see: https://github.com/statiolake/neovim-qt/commit/da8eaba7f0e38b6b51f3bacd02a8cc2d1f7a34d8

   // static
   void ThemeSwitcher::setDarkTitlebar(WId wid, bool dark /*=true*/)
   {
#ifdef Q_OS_WINDOWS
      _setDarkTitlebar(reinterpret_cast<HWND>(wid), dark);
   #endif
      // else do nothing - does not apply to other OSes
   }

   // static
   void ThemeSwitcher::setDarkTheme(QWidget *widget)
   {
      if (ThemeSwitcher::_darkPalette == nullptr) {
         _darkPalette = new QPalette();
         _darkPalette->setColor(QPalette::Window, QColor(36, 36, 36)); //QColor(53, 53, 53));
         _darkPalette->setColor(QPalette::WindowText, Qt::white);
         _darkPalette->setColor(QPalette::Disabled, QPalette::WindowText, QColor(127, 127, 127));
         _darkPalette->setColor(QPalette::Base, QColor(46, 46, 46)); //QColor(42, 42, 42));
         _darkPalette->setColor(QPalette::AlternateBase, QColor(66, 66, 66));
         _darkPalette->setColor(QPalette::ToolTipBase, Qt::white);
         _darkPalette->setColor(QPalette::ToolTipText, QColor(53, 53, 53));
         _darkPalette->setColor(QPalette::Text, Qt::white);
         _darkPalette->setColor(QPalette::Disabled, QPalette::Text, QColor(127, 127, 127));
         _darkPalette->setColor(QPalette::Dark, QColor(35, 35, 35));
         _darkPalette->setColor(QPalette::Shadow, QColor(20, 20, 20));
         _darkPalette->setColor(QPalette::Button, QColor(53, 53, 53));
         _darkPalette->setColor(QPalette::ButtonText, Qt::white);
         _darkPalette->setColor(QPalette::Disabled, QPalette::ButtonText, QColor(127, 127, 127));
         _darkPalette->setColor(QPalette::BrightText, Qt::red);
         _darkPalette->setColor(QPalette::Link, QColor(42, 130, 218));
         _darkPalette->setColor(QPalette::Highlight, QColor(42, 130, 218));
         _darkPalette->setColor(QPalette::Disabled, QPalette::Highlight, QColor(80, 80, 80));
         _darkPalette->setColor(QPalette::HighlightedText, Qt::white);
         _darkPalette->setColor(QPalette::Disabled, QPalette::HighlightedText, QColor(127, 127, 127));
      }
      widget->setPalette(*(ThemeSwitcher::_darkPalette));
   #ifdef Q_OS_WINDOWS
      // only on Windows!
      setDarkTitlebar(widget->winId(), true);
   #endif

      QGuiApplication *app = reinterpret_cast<QGuiApplication*>(QCoreApplication::instance());
      Q_ASSERT(app != nullptr);
      app->setPalette(*(ThemeSwitcher::_darkPalette));
   }

   // static
   void ThemeSwitcher::setLightTheme(QWidget *widget)
   {
      if (ThemeSwitcher::_lightPalette == nullptr) {
         _lightPalette = new QPalette();
         _lightPalette->setColor(QPalette::Window, QColor(240, 240, 240));
         _lightPalette->setColor(QPalette::WindowText, Qt::black);
         _lightPalette->setColor(QPalette::Disabled, QPalette::WindowText, QColor(240, 240, 240));
         _lightPalette->setColor(QPalette::Base, Qt::white);
         _lightPalette->setColor(QPalette::AlternateBase, QColor(233, 231, 227));
         _lightPalette->setColor(QPalette::ToolTipBase, QColor(255, 255, 220));
         _lightPalette->setColor(QPalette::ToolTipText, Qt::black);
         _lightPalette->setColor(QPalette::Text, Qt::black);
         _lightPalette->setColor(QPalette::Disabled, QPalette::Text, QColor(120, 120, 120));
         _lightPalette->setColor(QPalette::Dark, QColor(160, 160, 160));
         _lightPalette->setColor(QPalette::Shadow, QColor(105, 105, 105));
         _lightPalette->setColor(QPalette::Button, QColor(240, 240, 240));
         _lightPalette->setColor(QPalette::ButtonText, Qt::black);
         _lightPalette->setColor(QPalette::Disabled, QPalette::ButtonText, QColor(78, 78, 78));
         _lightPalette->setColor(QPalette::BrightText, Qt::white);
         _lightPalette->setColor(QPalette::Link, QColor(0, 0, 255));
         _lightPalette->setColor(QPalette::Highlight, QColor(0, 120, 215));
         _lightPalette->setColor(QPalette::Disabled, QPalette::Highlight, QColor(0, 120, 215));
         _lightPalette->setColor(QPalette::HighlightedText, Qt::white);
         _lightPalette->setColor(QPalette::Disabled, QPalette::HighlightedText, Qt::white);
      }
      widget->setPalette(*_lightPalette);
   #ifdef Q_OS_WINDOWS
      // only on fnSetWindowCompositionAttribute
      setDarkTitlebar(widget->winId(), false);
   #endif
      QGuiApplication *app = reinterpret_cast<QGuiApplication *>(QCoreApplication::instance());
      Q_ASSERT(app != nullptr);
      app->setPalette(*_lightPalette);
   }

}  // namespace winDark
