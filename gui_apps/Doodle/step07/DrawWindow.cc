// DrawWindow.cc: implements DrawWindow class
#include <QtGui>
#include <QApplication>
#include <QMessageBox>
#include <QInputDialog>
#include <QColorDialog>
#include <QFileDialog>
#include <QMessageBox>
#include <QAction>
#include <QIcon>
#include <QMenu>
#include <QMenuBar>
#include "DrawWindow.h"
#include "Doodle.h"
#include "Line.h"

const QString AppTitle("Qt Scribble");
const QString WindowTitle("Qt Scribble - Step07: Adding Actions + Menus + handlers");

DrawWindow::DrawWindow()
{
  setAttribute(Qt::WA_StaticContents);
  setWindowTitle(WindowTitle);

  createActions();
  createMenus();

  resize(640,480);

  _dragging = false;
  _doodle = new Doodle();
  _currLine = nullptr;
}

DrawWindow::~DrawWindow()
{
  delete _doodle;
}

void DrawWindow::createActions()
{
  fileNewAction = new QAction(QIcon(":/images/fileNew.jpeg"),tr("&New"),this);
  fileNewAction->setShortcut( tr("Ctrl+N"));
  fileNewAction->setStatusTip(tr("Create a new scribble document."));
  QObject::connect(fileNewAction, SIGNAL(triggered()), this, SLOT(fileNew()));

  fileOpenAction = new QAction(QIcon(":/images/fileOpen.jpeg"),tr("&Open..."),this);
  fileOpenAction->setShortcut( tr("Ctrl+O"));
  fileOpenAction->setStatusTip(tr("Open scribble document from disk file."));
  QObject::connect(fileOpenAction, SIGNAL(triggered()), this, SLOT(fileOpen()));

  fileSaveAction = new QAction(QIcon(":/images/fileSave.jpeg"),tr("&Save"),this);
  fileSaveAction->setShortcut( tr("Ctrl+S"));
  fileSaveAction->setStatusTip(tr("Save scribble document to disk file."));
  QObject::connect(fileSaveAction, SIGNAL(triggered()), this, SLOT(fileSave()));

  fileSaveAsAction = new QAction(QIcon(":/images/fileSaveAs.jpeg"),tr("Save &as..."),this);
  fileSaveAsAction->setStatusTip(tr("Save scribble document to disk with different name."));
  QObject::connect(fileSaveAsAction, SIGNAL(triggered()), this, SLOT(fileSaveAs()));

  exitAction = new QAction(tr("E&xit"),this);
  exitAction->setStatusTip(tr("Save all pending changes and quit application."));
  QObject::connect(exitAction, SIGNAL(triggered()), this, SLOT(close()));

  penWidthAction = new QAction(tr("Change pen &width..."),this);
  penWidthAction->setStatusTip(tr("Change the width of default pen."));
  QObject::connect(penWidthAction, SIGNAL(triggered()), this, SLOT(changePenWidth()));

  penColorAction = new QAction(tr("Change pen &color..."),this);
  penColorAction->setStatusTip(tr("Change the color of default pen."));
  QObject::connect(penColorAction, SIGNAL(triggered()), this, SLOT(changePenColor()));

  aboutAction = new QAction(tr("&About..."),this);
  aboutAction->setStatusTip(tr("Display information about program."));
  QObject::connect(aboutAction, SIGNAL(triggered()), this, SLOT(about()));
}

void DrawWindow::createMenus()
{
  fileMenu = new QMenu(tr("&File"), this);
  fileMenu->addAction(fileNewAction);
  fileMenu->addAction(fileOpenAction);
  fileMenu->addAction(fileSaveAction);
  fileMenu->addAction(fileSaveAsAction);
  fileMenu->addSeparator();
  fileMenu->addAction(exitAction);

  optionsMenu = new QMenu(tr("&Options"), this);
  optionsMenu->addAction(penWidthAction);
  optionsMenu->addAction(penColorAction);

  helpMenu = new QMenu(tr("&Help"), this);
  helpMenu->addAction(aboutAction);

  menuBar()->addMenu(fileMenu);
  menuBar()->addMenu(optionsMenu);
  menuBar()->addMenu(helpMenu);
}

bool DrawWindow::canClose()
{
  if (_doodle->modified()) {
    switch(
        QMessageBox::question(this, tr("Qt Scribble Tutorial"),
            tr("The doodle has changed. Save changes to doodle now?"),
            QMessageBox::Yes|QMessageBox::No|QMessageBox::Cancel, QMessageBox::No)
        )
    {
      case QMessageBox::Yes:
        // save doodle & quit
        fileSave();
        return true;
      case QMessageBox::No:
        // quit without saving
        return true;
      default:
        // don't quit yet!
        return false;
    }
  }
  return true;  // doodle not modified. Ok to quit!
}

void DrawWindow::closeEvent(QCloseEvent *event)
{
  if (canClose())
    event->accept();
  else
    event->ignore();
}

void DrawWindow::drawLineTo(const QPoint& pt)
{
  Q_ASSERT(_currLine != nullptr);
  // draw line from _lastPt to pt
  QPainter painter(&_image);
  QPen pen(_currLine->penColor(), _currLine->penWidth());
  painter.setRenderHint(QPainter::Antialiasing);
  painter.setPen(pen);
  painter.drawLine(_lastPt, pt);
  _lastPt = pt;
  update();
}

void DrawWindow::clearImage()
{
  Q_ASSERT(_doodle != nullptr);
  _doodle->clear();
  // TODO: should be filled with window background of
  // user's OS color scheme!!
  _image.fill(qRgb(255,255,255));
  update();
}

void DrawWindow::mousePressEvent(QMouseEvent *event)
{
  Q_ASSERT(_doodle != nullptr);

  // check if Ctrl key is held down as left/right mouse is clicked
  Qt::KeyboardModifiers modifiers  = QApplication::queryKeyboardModifiers();
  bool ctrlKeyIsDown = modifiers.testFlag(Qt::ControlModifier);

  qDebug() << "mousePressEvent() - CTRL key "
    << (ctrlKeyIsDown ? "IS" : "IS **NOT**") << " held down!";

  if (event->button() == Qt::LeftButton) {
    // left mouse button pressed
    if (ctrlKeyIsDown)
      changePenWidth();
    else {
      _currLine = _doodle->newLine();
      _lastPt = event->pos();
      _currLine->addPoint(_lastPt);
      _dragging = true;
      _doodle->setModified(true);
    }
  }
  else if (event->button() == Qt::RightButton) {
    if (ctrlKeyIsDown)
      changePenColor();
    else {
      clearImage();
      _doodle->setModified(false);
    }
  }
}

void  DrawWindow::mouseMoveEvent(QMouseEvent *event)
{
  if ((event->buttons() == Qt::LeftButton) && _dragging) {
    drawLineTo(event->pos());
    _currLine->addPoint(event->pos());
  }
}

void DrawWindow::mouseReleaseEvent(QMouseEvent *event)
{
  if ((event->button() == Qt::LeftButton) && _dragging) {
    drawLineTo(event->pos());
    _currLine->addPoint(event->pos());
    _dragging = false;
  }
}

void DrawWindow::changePenWidth()
{
  Q_ASSERT(_doodle != nullptr);
  // display message box & get width of pen
  bool ok;
  int newPenWidth = QInputDialog::getInt(this, AppTitle,
      QString("Enter new pen width:"), _doodle->penWidth(), 2, 12, 1, &ok);
  if (ok) {
    qDebug() << "New pen width selected: " << newPenWidth;
    _doodle->setPenWidth(newPenWidth);
  }
}

void DrawWindow::changePenColor()
{
  Q_ASSERT(_doodle != nullptr);
  // display standard color dialog & get new pen color
  QColor color = QColorDialog::getColor(_doodle->penColor(), this);
  if (color.isValid())
    _doodle->setPenColor(color);
}

void DrawWindow::resizeEvent(QResizeEvent *event)
{
  if (width() > _image.width() || height() > _image.height()) {
    int newWidth = qMax(width(), _image.width());
    int newHeight = qMax(height(), _image.height());
    resizeImage(QSize(newWidth, newHeight));
    update();
  }
  QWidget::resizeEvent(event);
}

void DrawWindow::paintEvent(QPaintEvent *event)
{
  QPainter painter(this);
  painter.setRenderHint(QPainter::Antialiasing);
  // we just blit the from image to device
  QRect dirtyRect = event->rect();
  painter.drawImage(dirtyRect, _image, dirtyRect);
}

void DrawWindow::resizeImage(const QSize& newSize)
{
  if (_image.size() == newSize)
    return;
  QImage newImage(newSize, QImage::Format_RGB32);
  newImage.fill(qRgb(255,255,255));
  // draw existing image over new image
  QPainter painter(&newImage);
  painter.setRenderHint(QPainter::Antialiasing);
  painter.drawImage(QPoint(0,0), _image);
  _image = newImage;
}

//
// Action response functions
//
void DrawWindow::fileNew()
{
  if (canClose())
    clearImage();
}

void DrawWindow::fileOpen()
{
  QMessageBox::information(this, AppTitle, tr("File|Open clicked!"));
}

void DrawWindow::fileSave()
{
  Q_ASSERT(_doodle != 0);
  if (_doodle->isNew())
    fileSaveAs();
  else {
    // TODO:
  }
}

void DrawWindow::fileSaveAs()
{
  QString currFileName("");
  QString fileName = QFileDialog::getSaveFileName(this, tr("Save As"), currFileName);
  if (!fileName.isEmpty()) {
    QString str;
    QTextStream ostr(&str);
    ostr << tr("Will save file to: ") << fileName;
    QMessageBox::information(this, tr("File Save As..."), str);
  }
}

void DrawWindow::exitApp()
{
  QMessageBox::information(this, AppTitle, tr("File|Exit clicked!"));
}

void DrawWindow::about()
{
  QMessageBox::information(this, AppTitle,
      tr("Qt Scribble\nScribble application developed with the Qt Framework\n"
         "Written by - Manish Bhobe"));
}
