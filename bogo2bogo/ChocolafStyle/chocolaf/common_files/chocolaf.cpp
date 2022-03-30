// ChocolafApp.cpp - ChocolafApp class implementation
#include <QApplication>
#include <QtMessageBox>
#include <QTextStream>
#include <QStyleFactory>
#include <exception>
#include "pyqtapp.h"

namespace Chocolaf {

   ChocolafApp::ChocolafApp(int argc, char **argv)
      : QApplication(argc, argv),
        _palette(nullptr), _styleSheet("")
   {
      this->setFont(QApplication::font("QMenu"));
      _palette = getPalette();
      _styleSheet = loadStyleSheet();
   }

   ChocolafApp::~ChocolafApp()
   {
      delete _palette;
   }

   void ChocolafApp::setStyle(const QString& styleName /*= "Chocolaf" */)
   {
      if (styleName == "Chocolaf") {
         this->setStyleSheet(_styleSheet);
         this->setPalette(*_palette);
      }
      else if (QStyleFactory.keys().count(styleName) > 0) {
         this->setStyle(styleName);
      }
      else {
         QString err = QString("Error: unrecognized style \'%1\'").arg(styleName);
         QMessageBox.critical(this, "FATAL ERROR", err);
         throw std::invalid_argument(err.toStdString().c_str());
      }
   }

   QString ChocolafApp::loadStyleSheet()
   {
      QFile f(":chocolaf/chocolaf.css");

      if (!f.exists()) {
         QMessageBox::critical(this, "FATAL ERROR",
            "Unable to load chocolaf stylesheet from :chocolaf/chocolaf.css");
         return "";
      }
      else {
         f.open(QFile::ReadOnly | QFile::Text);
         QTextStream ts(&f);
         return ts.readAll();
      }
   }

   QPalette* ChocolafApp::getPalette()
   {
      QPalette *palette = new QPalette();

      palette->setColor(QPalette::Window, ChocolafPalette::Window_Color)         // general background color
      palette->setColor(QPalette::WindowText, ChocolafPalette::WindowText_Color) // general foreground color
      palette->setColor(QPalette::Base, ChocolafPalette::Base_Color)        // background for text entry widgets
      // background color for views with alternating colors
      palette->setColor(QPalette::AlternateBase, ChocolafPalette::AlternateBase_Color)
      palette->setColor(QPalette::ToolTipBase, ChocolafPalette::ToolTipBase_Color)  // background for tooltips
      palette->setColor(QPalette::ToolTipText, ChocolafPalette::ToolTipText_Color)
      palette->setColor(QPalette::Text, ChocolafPalette::Text_Color)             // foreground color to use with Base
      palette->setColor(QPalette::Button, ChocolafPalette::Button_Color)         // pushbutton colors
      palette->setColor(QPalette::ButtonText, ChocolafPalette::ButtonText_Color) // pushbutton's text color
      palette->setColor(QPalette::Link, ChocolafPalette::Link_Color)
      palette->setColor(QPalette::LinkVisited, ChocolafPalette::LinkVisited_Color)
      palette->setColor(QPalette::Highlight, ChocolafPalette::Highlight_Color)     // highlight color
      palette->setColor(QPalette::HighlightedText, ChocolafPalette::HighlightedText_Color)
      // colors for disabled elements
      palette->setColor(QPalette::Disabled, QPalette::ButtonText, ChocolafPalette::Disabled_ButtonText_Color)
      palette->setColor(QPalette::Disabled, QPalette::WindowText, ChocolafPalette::Disabled_WindowText_Color)
      palette->setColor(QPalette::Disabled, QPalette::Text, ChocolafPalette::Disabled_Text_Color)
      palette->setColor(QPalette::Disabled, QPalette::Light, ChocolafPalette::Disabled_Light_Color)

      return palette
   }
}  // namespace Chocolaf
