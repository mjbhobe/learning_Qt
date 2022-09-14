// factorial.cc - calculate factorial for any number
#include <cstdlib>
#include <gmp.h>
#include <gmpxx.h>
#include <QtCore>
#include <QtGui>
#include <QtWidgets>
#include "common_funcs.h"

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

int main(int argc, char **argv)
{
   QApplication app(argc, argv);

   int answer {0};
   int num = 1;
   bool ok;

   do {
      num = QInputDialog::getInt(nullptr, "Factorial Input", "Enter an int:", /* value=*/ num,
         /* min=*/ 0, /* max=*/ 2147483647, /* step=*/ 1, &ok);
      QString ans;
      QTextStream ostr(&ans);
      if (ok)
         ostr << num << "! = " << mpz_class::factorial(num) << Qt::endl;
      else 
         ostr << "You cancelled the last input!" << Qt::endl;
      answer = QMessageBox::question(nullptr, "Play again?", ans,
         QMessageBox::Yes | QMessageBox::No);
   } while (answer == QMessageBox::Yes);
      

   return EXIT_SUCCESS;
}
