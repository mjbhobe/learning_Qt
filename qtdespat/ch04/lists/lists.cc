// lists.cc - using QStringList
#include <QtCore>    // all core classes

QTextStream cout(stdout, QIODevice::WriteOnly);
QTextStream cerr(stderr, QIODevice::WriteOnly);
QTextStream cin(stdin, QIODevice::ReadOnly);

void recurseDir(QDir& d, bool recursive=false, bool symlinks=false);

int main(void)
{
  QString winter = "December, January, February";
  QString spring = "March, April, May";
  QString summer = "June, July, August";
  QString fall = "September, October, November";

  QStringList months;
  months << winter;        // add string to list
  months += spring;        // another way
  months.append(summer);   // yet another way
  months << fall;

  cout << "Spring months are: " << months[1] << Qt::endl;
  // convert contents of a QStringList to a QString, with each
  // element separated with ,
  QString allMonths = months.join(", ");
  cout << "All months: " << allMonths << Qt::endl;

  // split the QString into individual strings on , separator
  QStringList list2 = allMonths.split(", ");
  Q_ASSERT(list2.size() == 12);

  // now let's iterate over the months in list2
  cout << "Iteration using foreach: " << Qt::endl << "   ";
  foreach(auto& mon, list2)
    cout << mon << " - ";
  cout << Qt::endl;

  // using C++ iterator style iteration
  cout << "Iteration using begin()/end() iterator: " << Qt::endl << "   ";
  for (auto iter = list2.begin(); iter != list2.end(); ++iter)
    cout << *iter << " ~ ";
  cout << Qt::endl;

  // using Java style iterator
  cout << "Using Java style iterators: " << Qt::endl << "   ";
  QListIterator<QString> iter2(list2);
  while (iter2.hasNext())
    cout << iter2.next() << " | ";
  cout << Qt::endl;

  // ---------------------------------------------------------------------
  // Iterating over directories: QDir, QFileInfo and QDirIterator
  // ---------------------------------------------------------------------
  QDir codeDir("c:/Dev/Code/C++/Qt");
  recurseDir(codeDir, true, false);

  return 0;
}

void recurseDir(QDir& d, bool recursive/*=false*/, bool symlinks/*=false*/)
{
  d.setSorting(QDir::Name);
  QDir::Filters df = QDir::Files | QDir::NoDotAndDotDot;
  if (recursive) df |= QDir::Dirs;
  if (not symlinks) df |= QDir::NoSymLinks;

  QStringList contents = d.entryList(df, QDir::Name | QDir::DirsFirst);
  // iterate over contents
  foreach(const auto& entry, contents) {
    QFileInfo fileInfo(d, entry);   // get info on entry
    if (fileInfo.isDir()) {
      // recurse through dir
      QDir dir(fileInfo.absoluteFilePath());
      recurseDir(dir, recursive, symlinks);
    } 
    else {
      if (fileInfo.completeSuffix() == "cpp" || fileInfo.completeSuffix() == "cc")
        // display C++ code files
        cout << fileInfo.absoluteFilePath() << Qt::endl;
    }
  }
}


