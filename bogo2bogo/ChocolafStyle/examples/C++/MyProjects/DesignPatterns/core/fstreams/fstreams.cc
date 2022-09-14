// fstreans.cc - file streams with Qt
#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);
    int luckyNumber {7};
    float pi {3.14};
    double e {2.71828};
    QString name {"Manish Bhobe"};

    // write values to a string stream
    QString str;
    QTextStream ostr(&str);
    ostr << name << "'s lucky number is " << luckyNumber
        << ". He loves " << pi << " raised to " << e << Qt::endl;
    cout << str;

    // save to file & read from file
    QFile data("./mydata");
    data.open(QIODevice::WriteOnly);
    QTextStream out(&data);
    out << name << "|" << luckyNumber << "|" << pi << "|" << e;
    data.close();

    QString line, str2;
    int luckyNumber2;
    float pi2;
    double e2;
    // lets read string from     
    data.open(QIODevice::ReadOnly);
    QTextStream in(&data);
    line = in.readLine();
    QStringList items = line.split("|");
    if (items.length() != 4)
        cerr << "FATAL: could not read & parse file!" << Qt::endl;
    else {
        str2 = items.at(0);
        luckyNumber2 = items.at(1).toInt();
        pi2 = items.at(2).toFloat();
        e2 = items.at(3).toDouble();
        cout << str2 << "'s lucky number is " << luckyNumber2 
            << ". He loves " << pi2 << " raised to " << e2 << Qt::endl;
        data.close();
    }

    // reading & writing binary streams
    QFile bindata("./mydata2");
    bindata.open(QIODevice::WriteOnly);
    QDataStream out2(&bindata);
    out2 << name << qint32(luckyNumber) << qreal(pi) << qreal(e);
    bindata.close();

    bindata.open(QIODevice::ReadOnly);
    QDataStream in2(&bindata);
    QString name2;
    in2 >> name2;
    qint32 lno;
    in2 >> lno;
    qreal p, ex;
    in2 >> p >> ex;
    cout << "(From binary stream) -> " << name2 << "'s lucky number is " << int(lno)
        << ". He loves " << float(p) << " raised to " << double(ex) << Qt::endl;
    bindata.close();

    return EXIT_SUCCESS;
}