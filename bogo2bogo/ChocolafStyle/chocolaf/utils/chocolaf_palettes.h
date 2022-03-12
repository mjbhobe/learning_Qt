// palettes.h - key color lookup for Chocolaf for C++
#ifndef __Chocolaf_Palettes_h__
#define __Chocolaf_Palettes_h__

#include <QColor>

class ChocolafPalette
{
 public:
   // default background color for all widgets
   const QColor Window_Color = QColor(qRgb(42, 42, 42));
   // default foreground color for text
   const QColor WindowText_Color = QColor(qRgb(220, 220, 220));
   // background for text entry widgets
   const QColor Base_Color = QColor(qRgb(52, 52, 52));
   // foreground color to use with Base
   const QColor Text_Color = QColor(qRgb(220, 220, 220));
   // background color for views with alternating lors
   const QColor AlternateBase_Color = QColor(qRgb(62, 62, 62));
   // background color for tooltips
   const QColor ToolTipBase_Color = QColor(qRgb(224, 227, 176));
   // text color for tooltips
   const QColor ToolTipText_Color = QColor(qRgb(0, 0, 0));
   // pushbutton background color
   const QColor Button_Color = QColor(qRgb(62, 62, 62));
   // button text color
   const QColor ButtonText_Color = QColor(qRgb(220, 220, 220));
   // HTML link color
   const QColor Link_Color = QColor(qRgb(0, 0, 255));
   // visited link color
   const QColor LinkVisited_Color = QColor(qRgb(255, 0, 255));
   // background color of highlight (or selected) text or item
   const QColor Highlight_Color = QColor(qRgb(0, 114, 198));
   // foreground color of highlight (or selected) text or item
   const QColor HighlightedText_Color = QColor(qRgb(220, 220, 220));
   // disabled text foreground color
   const QColor Disabled_Text_Color = QColor(qRgb(127, 127, 127));
   // disabled pushbutton foreground color
   const QColor Disabled_ButtonText_Color = QColor(qRgb(127, 127, 127));
   // disabled window text color
   const QColor Disabled_WindowText_Color = QColor(qRgb(127, 127, 127));
   // faded text color (used for grid line color)
   const QColor Disabled_Light_Color = QColor(qRgb(102, 102, 102));
};

#endif // __Chocolaf_Palettes_h__
