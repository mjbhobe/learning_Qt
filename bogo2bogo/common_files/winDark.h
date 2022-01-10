#ifndef __winDark_h__
#define __winDark_h__

#include <QColor>
#include <QPalette>
#ifdef Q_OS_WINDOWS
#include <dwmapi.h>
#include <windows.h>
#endif

namespace winDark {
   // some common functions
   QColor getPaletteColor(QPalette::ColorRole colorRole,
      QPalette::ColorGroup colorGroup = QPalette::Active);

   class ThemeSwitcher : public QObject
   {
      Q_OBJECT
    public:
      static QPalette *_darkPalette;
      static QPalette *_lightPalette;

      static void setDarkTheme(QWidget *widget);
      static void setDarkTitlebar(WId wid, bool dark = true);
      static void setLightTheme(QWidget *widget);
   };

   #ifdef Q_OS_WINDOWS
   enum PreferredAppMode { Default, AllowDark, ForceDark, ForceLight, Max };

   enum WINDOWCOMPOSITIONATTRIB {
      WCA_UNDEFINED = 0,
      WCA_NCRENDERING_ENABLED = 1,
      WCA_NCRENDERING_POLICY = 2,
      WCA_TRANSITIONS_FORCEDISABLED = 3,
      WCA_ALLOW_NCPAINT = 4,
      WCA_CAPTION_BUTTON_BOUNDS = 5,
      WCA_NONCLIENT_RTL_LAYOUT = 6,
      WCA_FORCE_ICONIC_REPRESENTATION = 7,
      WCA_EXTENDED_FRAME_BOUNDS = 8,
      WCA_HAS_ICONIC_BITMAP = 9,
      WCA_THEME_ATTRIBUTES = 10,
      WCA_NCRENDERING_EXILED = 11,
      WCA_NCADORNMENTINFO = 12,
      WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
      WCA_VIDEO_OVERLAY_ACTIVE = 14,
      WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
      WCA_DISALLOW_PEEK = 16,
      WCA_CLOAK = 17,
      WCA_CLOAKED = 18,
      WCA_ACCENT_POLICY = 19,
      WCA_FREEZE_REPRESENTATION = 20,
      WCA_EVER_UNCLOAKED = 21,
      WCA_VISUAL_OWNER = 22,
      WCA_HOLOGRAPHIC = 23,
      WCA_EXCLUDED_FROM_DDA = 24,
      WCA_PASSIVEUPDATEMODE = 25,
      WCA_USEDARKMODECOLORS = 26,
      WCA_LAST = 27
   };

   struct WINDOWCOMPOSITIONATTRIBDATA {
      WINDOWCOMPOSITIONATTRIB Attrib;
      PVOID pvData;
      SIZE_T cbData;
   };

   using fnAllowDarkModeForWindow =
      BOOL(WINAPI *)(HWND hWnd, BOOL allow);
   using fnSetPreferredAppMode =
      PreferredAppMode(WINAPI *)(PreferredAppMode appMode);
   using fnSetWindowCompositionAttribute =
      BOOL(WINAPI *)(HWND hwnd, WINDOWCOMPOSITIONATTRIBDATA *);
   void _setDarkTitlebar(HWND hwnd, bool dark = true);
#endif
}

#endif  // __winDark_h__
