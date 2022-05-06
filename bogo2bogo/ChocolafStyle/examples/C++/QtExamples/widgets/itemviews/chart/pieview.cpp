/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "pieview.h"

#include <QtWidgets>

PieView::PieView(QWidget *parent) : QAbstractItemView(parent)
{
  horizontalScrollBar()->setRange(0, 0);
  verticalScrollBar()->setRange(0, 0);
}

void PieView::dataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight,
                          const QVector<int> &roles)
{
  QAbstractItemView::dataChanged(topLeft, bottomRight, roles);

  if (!roles.contains(Qt::DisplayRole))
    return;

  validItems = 0;
  totalValue = 0.0;

  for (int row = 0; row < model()->rowCount(rootIndex()); ++row) {

    QModelIndex index = model()->index(row, 1, rootIndex());
    double value = model()->data(index, Qt::DisplayRole).toDouble();

    if (value > 0.0) {
      totalValue += value;
      validItems++;
    }
  }
  viewport()->update();
}

bool PieView::edit(const QModelIndex &index, EditTrigger trigger, QEvent *event)
{
  if (index.column() == 0)
    return QAbstractItemView::edit(index, trigger, event);
  else
    return false;
}

/*
    Returns the item that covers the coordinate given in the view.
*/

QModelIndex PieView::indexAt(const QPoint &point) const
{
  if (validItems == 0)
    return QModelIndex();

  // Transform the view coordinates into contents widget coordinates.
  int wx = point.x() + horizontalScrollBar()->value();
  int wy = point.y() + verticalScrollBar()->value();

  if (wx < totalSize) {
    double cx = wx - totalSize / 2;
    double cy = totalSize / 2 - wy; // positive cy for items above the center

    // Determine the distance from the center point of the pie chart.
    double d = std::sqrt(std::pow(cx, 2) + std::pow(cy, 2));

    if (d == 0 || d > pieSize / 2)
      return QModelIndex();

    // Determine the angle of the point.
    double angle = qRadiansToDegrees(std::atan2(cy, cx));
    if (angle < 0)
      angle = 360 + angle;

    // Find the relevant slice of the pie.
    double startAngle = 0.0;

    for (int row = 0; row < model()->rowCount(rootIndex()); ++row) {

      QModelIndex index = model()->index(row, 1, rootIndex());
      double value = model()->data(index).toDouble();

      if (value > 0.0) {
        double sliceAngle = 360 * value / totalValue;

        if (angle >= startAngle && angle < (startAngle + sliceAngle))
          return model()->index(row, 1, rootIndex());

        startAngle += sliceAngle;
      }
    }
  } else {
    double itemHeight = QFontMetrics(viewOptions().font).height();
    int listItem = int((wy - margin) / itemHeight);
    int validRow = 0;

    for (int row = 0; row < model()->rowCount(rootIndex()); ++row) {

      QModelIndex index = model()->index(row, 1, rootIndex());
      if (model()->data(index).toDouble() > 0.0) {

        if (listItem == validRow)
          return model()->index(row, 0, rootIndex());

        // Update the list index that corresponds to the next valid row.
        ++validRow;
      }
    }
  }

  return QModelIndex();
}

bool PieView::isIndexHidden(const QModelIndex & /*index*/) const { return false; }

/*
    Returns the rectangle of the item at position \a index in the
    model. The rectangle is in contents coordinates.
*/

QRect PieView::itemRect(const QModelIndex &index) const
{
  if (!index.isValid())
    return QRect();

  // Check whether the index's row is in the list of rows represented
  // by slices.
  QModelIndex valueIndex;

  if (index.column() != 1)
    valueIndex = model()->index(index.row(), 1, rootIndex());
  else
    valueIndex = index;

  if (model()->data(valueIndex).toDouble() <= 0.0)
    return QRect();

  int listItem = 0;
  for (int row = index.row() - 1; row >= 0; --row) {
    if (model()->data(model()->index(row, 1, rootIndex())).toDouble() > 0.0)
      listItem++;
  }

  switch (index.column()) {
    case 0: {
      const qreal itemHeight = QFontMetricsF(viewOptions().font).height();

      return QRect(totalSize, qRound(margin + listItem * itemHeight), totalSize - margin,
                   qRound(itemHeight));
    }
    case 1:
      return viewport()->rect();
  }
  return QRect();
}

QRegion PieView::itemRegion(const QModelIndex &index) const
{
  if (!index.isValid())
    return QRegion();

  if (index.column() != 1)
    return itemRect(index);

  if (model()->data(index).toDouble() <= 0.0)
    return QRegion();

  double startAngle = 0.0;
  for (int row = 0; row < model()->rowCount(rootIndex()); ++row) {

    QModelIndex sliceIndex = model()->index(row, 1, rootIndex());
    double value = model()->data(sliceIndex).toDouble();

    if (value > 0.0) {
      double angle = 360 * value / totalValue;

      if (sliceIndex == index) {
        QPainterPath slicePath;
        slicePath.moveTo(totalSize / 2, totalSize / 2);
        slicePath.arcTo(margin, margin, margin + pieSize, margin + pieSize, startAngle,
                        angle);
        slicePath.closeSubpath();

        return QRegion(slicePath.toFillPolygon().toPolygon());
      }

      startAngle += angle;
    }
  }

  return QRegion();
}

int PieView::horizontalOffset() const { return horizontalScrollBar()->value(); }

void PieView::mousePressEvent(QMouseEvent *event)
{
  QAbstractItemView::mousePressEvent(event);
  origin = event->pos();
  if (!rubberBand)
    rubberBand = new QRubberBand(QRubberBand::Rectangle, viewport());
  rubberBand->setGeometry(QRect(origin, QSize()));
  rubberBand->show();
}

void PieView::mouseMoveEvent(QMouseEvent *event)
{
  if (rubberBand)
    rubberBand->setGeometry(QRect(origin, event->pos()).normalized());
  QAbstractItemView::mouseMoveEvent(event);
}

void PieView::mouseReleaseEvent(QMouseEvent *event)
{
  QAbstractItemView::mouseReleaseEvent(event);
  if (rubberBand)
    rubberBand->hide();
  viewport()->update();
}

QModelIndex PieView::moveCursor(QAbstractItemView::CursorAction cursorAction,
                                Qt::KeyboardModifiers /*modifiers*/)
{
  QModelIndex current = currentIndex();

  switch (cursorAction) {
    case MoveLeft:
    case MoveUp:
      if (current.row() > 0)
        current = model()->index(current.row() - 1, current.column(), rootIndex());
      else
        current = model()->index(0, current.column(), rootIndex());
      break;
    case MoveRight:
    case MoveDown:
      if (current.row() < rows(current) - 1)
        current = model()->index(current.row() + 1, current.column(), rootIndex());
      else
        current = model()->index(rows(current) - 1, current.column(), rootIndex());
      break;
    default:
      break;
  }

  viewport()->update();
  return current;
}

void PieView::paintEvent(QPaintEvent *event)
{
  QItemSelectionModel *selections = selectionModel();
  QStyleOptionViewItem option = viewOptions();

  QBrush background = option.palette.base();
  QPen foreground(option.palette.color(QPalette::WindowText));

  QPainter painter(viewport());
  painter.setRenderHint(QPainter::Antialiasing);

  painter.fillRect(event->rect(), background);
  painter.setPen(foreground);

  // Viewport rectangles
  QRect pieRect = QRect(margin, margin, pieSize, pieSize);

  if (validItems <= 0)
    return;

  painter.save();
  painter.translate(pieRect.x() - horizontalScrollBar()->value(),
                    pieRect.y() - verticalScrollBar()->value());
  painter.drawEllipse(0, 0, pieSize, pieSize);
  double startAngle = 0.0;
  int row;

  for (row = 0; row < model()->rowCount(rootIndex()); ++row) {
    QModelIndex index = model()->index(row, 1, rootIndex());
    double value = model()->data(index).toDouble();

    if (value > 0.0) {
      double angle = 360 * value / totalValue;

      QModelIndex colorIndex = model()->index(row, 0, rootIndex());
      QColor color = QColor(model()->data(colorIndex, Qt::DecorationRole).toString());

      if (currentIndex() == index)
        painter.setBrush(QBrush(color, Qt::Dense4Pattern));
      else if (selections->isSelected(index))
        painter.setBrush(QBrush(color, Qt::Dense3Pattern));
      else
        painter.setBrush(QBrush(color));

      painter.drawPie(0, 0, pieSize, pieSize, int(startAngle * 16), int(angle * 16));

      startAngle += angle;
    }
  }
  painter.restore();

  int keyNumber = 0;

  for (row = 0; row < model()->rowCount(rootIndex()); ++row) {
    QModelIndex index = model()->index(row, 1, rootIndex());
    double value = model()->data(index).toDouble();

    if (value > 0.0) {
      QModelIndex labelIndex = model()->index(row, 0, rootIndex());

      QStyleOptionViewItem option = viewOptions();
      option.rect = visualRect(labelIndex);
      if (selections->isSelected(labelIndex))
        option.state |= QStyle::State_Selected;
      if (currentIndex() == labelIndex)
        option.state |= QStyle::State_HasFocus;
      itemDelegate()->paint(&painter, option, labelIndex);

      ++keyNumber;
    }
  }
}

void PieView::resizeEvent(QResizeEvent * /* event */) { updateGeometries(); }

int PieView::rows(const QModelIndex &index) const
{
  return model()->rowCount(model()->parent(index));
}

void PieView::rowsInserted(const QModelIndex &parent, int start, int end)
{
  for (int row = start; row <= end; ++row) {
    QModelIndex index = model()->index(row, 1, rootIndex());
    double value = model()->data(index).toDouble();

    if (value > 0.0) {
      totalValue += value;
      ++validItems;
    }
  }

  QAbstractItemView::rowsInserted(parent, start, end);
}

void PieView::rowsAboutToBeRemoved(const QModelIndex &parent, int start, int end)
{
  for (int row = start; row <= end; ++row) {
    QModelIndex index = model()->index(row, 1, rootIndex());
    double value = model()->data(index).toDouble();
    if (value > 0.0) {
      totalValue -= value;
      --validItems;
    }
  }

  QAbstractItemView::rowsAboutToBeRemoved(parent, start, end);
}

void PieView::scrollContentsBy(int dx, int dy) { viewport()->scroll(dx, dy); }

void PieView::scrollTo(const QModelIndex &index, ScrollHint)
{
  QRect area = viewport()->rect();
  QRect rect = visualRect(index);

  if (rect.left() < area.left()) {
    horizontalScrollBar()->setValue(horizontalScrollBar()->value() + rect.left() -
                                    area.left());
  } else if (rect.right() > area.right()) {
    horizontalScrollBar()->setValue(
        horizontalScrollBar()->value() +
        qMin(rect.right() - area.right(), rect.left() - area.left()));
  }

  if (rect.top() < area.top()) {
    verticalScrollBar()->setValue(verticalScrollBar()->value() + rect.top() - area.top());
  } else if (rect.bottom() > area.bottom()) {
    verticalScrollBar()->setValue(
        verticalScrollBar()->value() +
        qMin(rect.bottom() - area.bottom(), rect.top() - area.top()));
  }

  update();
}

/*
    Find the indices corresponding to the extent of the selection.
*/

void PieView::setSelection(const QRect &rect, QItemSelectionModel::SelectionFlags command)
{
  // Use content widget coordinates because we will use the itemRegion()
  // function to check for intersections.

  QRect contentsRect =
      rect.translated(horizontalScrollBar()->value(), verticalScrollBar()->value())
          .normalized();

  int rows = model()->rowCount(rootIndex());
  int columns = model()->columnCount(rootIndex());
  QModelIndexList indexes;

  for (int row = 0; row < rows; ++row) {
    for (int column = 0; column < columns; ++column) {
      QModelIndex index = model()->index(row, column, rootIndex());
      QRegion region = itemRegion(index);
      if (region.intersects(contentsRect))
        indexes.append(index);
    }
  }

  if (indexes.size() > 0) {
    int firstRow = indexes.at(0).row();
    int lastRow = firstRow;
    int firstColumn = indexes.at(0).column();
    int lastColumn = firstColumn;

    for (int i = 1; i < indexes.size(); ++i) {
      firstRow = qMin(firstRow, indexes.at(i).row());
      lastRow = qMax(lastRow, indexes.at(i).row());
      firstColumn = qMin(firstColumn, indexes.at(i).column());
      lastColumn = qMax(lastColumn, indexes.at(i).column());
    }

    QItemSelection selection(model()->index(firstRow, firstColumn, rootIndex()),
                             model()->index(lastRow, lastColumn, rootIndex()));
    selectionModel()->select(selection, command);
  } else {
    QModelIndex noIndex;
    QItemSelection selection(noIndex, noIndex);
    selectionModel()->select(selection, command);
  }

  update();
}

void PieView::updateGeometries()
{
  horizontalScrollBar()->setPageStep(viewport()->width());
  horizontalScrollBar()->setRange(0, qMax(0, 2 * totalSize - viewport()->width()));
  verticalScrollBar()->setPageStep(viewport()->height());
  verticalScrollBar()->setRange(0, qMax(0, totalSize - viewport()->height()));
}

int PieView::verticalOffset() const { return verticalScrollBar()->value(); }

/*
    Returns the position of the item in viewport coordinates.
*/

QRect PieView::visualRect(const QModelIndex &index) const
{
  QRect rect = itemRect(index);
  if (!rect.isValid())
    return rect;

  return QRect(rect.left() - horizontalScrollBar()->value(),
               rect.top() - verticalScrollBar()->value(), rect.width(), rect.height());
}

/*
    Returns a region corresponding to the selection in viewport coordinates.
*/

QRegion PieView::visualRegionForSelection(const QItemSelection &selection) const
{
  int ranges = selection.count();

  if (ranges == 0)
    return QRect();

  QRegion region;
  for (int i = 0; i < ranges; ++i) {
    const QItemSelectionRange &range = selection.at(i);
    for (int row = range.top(); row <= range.bottom(); ++row) {
      for (int col = range.left(); col <= range.right(); ++col) {
        QModelIndex index = model()->index(row, col, rootIndex());
        region += visualRect(index);
      }
    }
  }
  return region;
}
