// MatOps.cpp - MatOps class implementation
#include "MatOps.h"
#include <QtCore>
#include <QtGui>
#include <QtWidgets>
#include <opencv2/opencv.hpp>

MatOp::MatOp(const QPixmap &pixmap, QObject *parent /*= nullptr*/) : QObject(parent)
{
    m_image = pixmap.toImage();
    m_image = m_image.convertToFormat(QImage::Format_RGB888);
    m_srcMat = cv::Mat(m_image.height(), m_image.width(), CV_8UC3, m_image.bits(),
                       m_image.bytesPerLine());
}

QPixmap MatOp::blur(cv::Size ksize /*= cv::Size(8,8)*/,
                    cv::Point anchor /*=cv::Point(-1,-1)*/, int borderType /*=4*/)
{
    cv::Mat conv;
    cv::blur(m_srcMat, conv, ksize, anchor, borderType);
    QImage blurredImage(conv.data, conv.cols, conv.rows, conv.step,
                        QImage::Format_RGB888);
    return QPixmap::fromImage(blurredImage);
}

QPixmap MatOp::sharpen(int intensity /*= 2*/, cv::Size ksize /*= cv::Size(9, 9)*/,
                       double sigmaX /*= 0.0*/, double sigmaY /*= 0.0*/,
                       int borderType /*= 4*/)
{
    cv::Mat conv;
    cv::GaussianBlur(m_srcMat, conv, ksize, sigmaX, sigmaY, borderType);
    QImage sharpImage(conv.data, conv.cols, conv.rows, conv.step, QImage::Format_RGB888);
    return QPixmap::fromImage(sharpImage);
}

QPixmap
MatOp::erode(cv::Point anchor /*= cv::Point(-1, -1)*/, int iterations /*= 1*/,
             int borderType /*= 0*/,
             const cv::Scalar &borderValue /*= cv::morphologyDefaultBorderValue()*/)
{
    cv::erode(m_srcMat, m_srcMat, cv::Mat(), anchor, iterations, borderType, borderValue);
    QImage erodeImage(m_srcMat.data, m_srcMat.cols, m_srcMat.rows, m_srcMat.step,
                      QImage::Format_RGB888);
    return QPixmap::fromImage(erodeImage);
}
