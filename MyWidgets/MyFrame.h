#ifndef MYFRAME_H
#define MYFRAME_H

#include <QFrameWindow>

class MyFrame : public QFrameWindow
{
   Q_OBJECT

      public:
               MyFrame(QWidget *parent = 0);
};

#endif // MYFRAME_H
