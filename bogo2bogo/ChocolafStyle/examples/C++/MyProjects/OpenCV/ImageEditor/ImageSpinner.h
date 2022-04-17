#ifndef __ImageSpinner_h__
#define __ImageSpinner_h__

#include <QDir>
#include <QStringList>

class ImageSpinner : public QObject
{
public:
  ImageSpinner(const QString &imagePath);
  QString nextImage();
  QString prevImage();
  bool atFirst() const;
  bool atLast() const;

protected:
  int m_currIndex;
  QDir m_dir;
  QStringList m_fileNames;
};

#endif // __ImageSpinner_h__
