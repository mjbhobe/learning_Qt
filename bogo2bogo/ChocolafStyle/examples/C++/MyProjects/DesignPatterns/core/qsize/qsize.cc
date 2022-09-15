// qsize.cc - sizeof common data types
#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);

int main() {
    QTextStream cout(stdout);
    char array1[34] = "This is a dreaded C array of char";
    char array2[] = "if not for main, we could avoid it entirely.";
    char* charp = array1;
    QString qstring = "This is a unicode QString. Much preferred." ;
    // Q_ASSERT (sizeof(i) == sizeof(int));
    cout << " C++ type sizes: \n";
    cout << "  sizeof(char) = " << sizeof(char) << Qt::endl;
    cout << "  sizeof(wchar_t) = " << sizeof(wchar_t) << Qt::endl;
    cout << "  sizeof(int) = " << sizeof(int) << Qt::endl;
    cout << "  sizeof(long) = " << sizeof(long) << Qt::endl;
    cout << "  sizeof(float) = " << sizeof(float) << Qt::endl;
    cout << "  sizeof(double) = " << sizeof(double) << Qt::endl;
    cout << "  sizeof(double*) = " << sizeof(double*) << Qt::endl;
    cout << "  sizeof(array1) = " << sizeof(array1) << Qt::endl;
    cout << "  sizeof(array2) = " << sizeof(array2) << Qt::endl;
    cout << "  sizeof(char*) = " << sizeof(charp) << Qt::endl;
    cout << " Qt type sizes: \n";
    cout << "  sizeof(QString) = " << sizeof(QString) << Qt::endl;
    cout << "  sizeof(qint32) = " << sizeof (qint32) << Qt::endl;
    cout << "  sizeof(qint64) = " << sizeof(qint64) << Qt::endl;
    cout << "  sizeof(QChar) = " << sizeof (QChar) << Qt::endl;
    cout << "  sizeof(QDate) = " << sizeof(QDate) << Qt::endl;
    cout << "  sizeof(QDateTime) = " << sizeof(QDateTime) << Qt::endl;
    cout << "  qstring.length() = " << qstring.length() << Qt::endl;

    return EXIT_SUCCESS;
}
