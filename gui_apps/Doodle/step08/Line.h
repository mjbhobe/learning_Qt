// Line.h - declares the Line class
#ifndef __Line_h__
#define __Line_h__

#include <QtGui>
#include <QList>
#include <QDataStream>

class Line  : public QObject {
    Q_OBJECT
  public:
    Line(int penWidth = 2, const QColor& penColor = qRgb(0,0,255));
    ~Line();

    int penWidth() const { return _penWidth; }
    QColor penColor() const { return _penColor; }
    // helper functions
    int  numPoints() const;
    void addPoint(const QPoint& pt);
    void draw(QPainter& painter);
    void saveToStream(QDataStream& ds) const;
    void loadFromStream(QDataStream& ds);

    friend QDataStream& operator << (QDataStream& ds, const Line& l);
    friend QDataStream& operator >> (QDataStream& ds, Line& l);
    friend QDataStream& operator << (QDataStream& ds, const Line *l);
    friend QDataStream& operator >> (QDataStream& ds, Line *l);
  public slots:  
    void setPenWidth(int newWidth);
    void setPenColor(const QColor& newColor);
  signals:
    void penWidthChanged(int newWidth);
    void penColorChanged(const QColor& newColor);
  private:
    int _penWidth;
    QColor _penColor;
    QList<QPoint> *_points;
};

#endif  // __Line_h__
