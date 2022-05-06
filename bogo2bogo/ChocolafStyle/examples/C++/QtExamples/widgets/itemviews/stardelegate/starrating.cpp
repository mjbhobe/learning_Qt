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

#include "starrating.h"

#include <QtWidgets>
#include <cmath>

constexpr int PaintingScaleFactor = 20;

//! [0]
StarRating::StarRating(int starCount, int maxStarCount)
    : myStarCount(starCount), myMaxStarCount(maxStarCount)
{
  starPolygon << QPointF(1.0, 0.5);
  for (int i = 1; i < 5; ++i)
    starPolygon << QPointF(0.5 + 0.5 * std::cos(0.8 * i * 3.14),
                           0.5 + 0.5 * std::sin(0.8 * i * 3.14));

  diamondPolygon << QPointF(0.4, 0.5) << QPointF(0.5, 0.4) << QPointF(0.6, 0.5)
                 << QPointF(0.5, 0.6) << QPointF(0.4, 0.5);
}
//! [0]

//! [1]
QSize StarRating::sizeHint() const
{
  return PaintingScaleFactor * QSize(myMaxStarCount, 1);
}
//! [1]

//! [2]
void StarRating::paint(QPainter *painter, const QRect &rect, const QPalette &palette,
                       EditMode mode) const
{
  painter->save();

  painter->setRenderHint(QPainter::Antialiasing, true);
  painter->setPen(Qt::NoPen);
  painter->setBrush(mode == EditMode::Editable ? palette.highlight()
                                               : palette.windowText());

  const int yOffset = (rect.height() - PaintingScaleFactor) / 2;
  painter->translate(rect.x(), rect.y() + yOffset);
  painter->scale(PaintingScaleFactor, PaintingScaleFactor);

  for (int i = 0; i < myMaxStarCount; ++i) {
    if (i < myStarCount)
      painter->drawPolygon(starPolygon, Qt::WindingFill);
    else if (mode == EditMode::Editable)
      painter->drawPolygon(diamondPolygon, Qt::WindingFill);
    painter->translate(1.0, 0.0);
  }

  painter->restore();
}
//! [2]
