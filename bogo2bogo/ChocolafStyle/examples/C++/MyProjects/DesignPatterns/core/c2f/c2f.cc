// c2f.cc = temperature conversion
#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(int argc, char **argv)
{
    float celcius {0.0f};
    float farenheit {0.0f};
    QString data;
    bool ok, repeat {true};

    do {
        cout << "Enter celcius temp (Enter to quit): " << Qt::flush;
        data = cin.readLine();
        if (data.trimmed().length() != 0) {
            celcius = data.toFloat(&ok);
            if (ok)  {
                farenheit = (celcius * 9.0f/5.0f) + 32.0f;
                cout << celcius << " C = " << farenheit << " F" << Qt::endl;
            } else {
                cerr << "Error: " << data << " is not numeric" << Qt::endl;
            }
        } else {
            repeat = false;
        }
    } while (repeat);
    
    return EXIT_SUCCESS;
}
