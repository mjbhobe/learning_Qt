#include <QtCore>
#include <QtGui>
#include <QtWidgets>

QString readFile(const QString& filePath)
{
  QFile file(filePath);
  file.open(QFile::ReadOnly | QFile::Text);
  QTextStream ostr(&file);
  return ostr.readAll();
}

int main(int argc, char **argv)
{
  QApplication app(argc, argv);
  app.setStyle("Fusion");
  app.setFont(QApplication::font("QMenu"));
  QFont mono = QFont("Consolas", 10);

  QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF-8"));
  qDebug() << "QCoreApplication::applicationDirPath() = "
    << QCoreApplication::applicationDirPath();


  QTextEdit *edit1 = new QTextEdit();
  edit1->setFont(mono);
  edit1->setText(readFile("./note_fr.txt"));
  QTextEdit *edit2 = new QTextEdit();
  edit2->setFont(mono);
  edit2->setText(readFile("./note.txt"));
  QTextEdit *edit3 = new QTextEdit();
  edit3->setFont(mono);
  edit3->setText(readFile("./note_de.txt"));

  QSplitter splitter(Qt::Horizontal);
  splitter.setWindowTitle("QSplitter Example");
  splitter.addWidget(edit1);
  splitter.addWidget(edit2);
  splitter.addWidget(edit3);
  splitter.show();

  return app.exec();
}
