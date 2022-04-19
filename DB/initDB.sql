CREATE DATABASE IF NOT EXISTS `comp4442-group-project`;
USE `comp4442-group-project`;

/* CREATE TABLE IF NOT EXISTS `DrivingRecords`(
    ReportID                INT             NOT NULL        AUTO_INCREMENT,
    DriverID                VARCHAR(40)     NOT NULL,
    CarPlateNumber          VARCHAR(40)     NOT NULL,
    Latitude                DOUBLE          NOT NULL,
    Longtitude              DOUBLE          NOT NULL,
    Speed                   DOUBLE          NOT NULL,
    Direction               DOUBLE          NOT NULL,
    SiteName                VARCHAR(50)     DEFAULT NULL,
    ReportTime              DATETIME        NOT NULL,
    isRapidlySpeedup        BOOLEAN         DEFAULT NULL,
    isRapidlySlowdown       BOOLEAN         DEFAULT NULL,
    isNeutralSlide          BOOLEAN         DEFAULT NULL,
    isNeutralSlideFinished  BOOLEAN         DEFAULT NULL,
    neutralSlideTime        INT             DEFAULT NULL,
    isOverspeed             BOOLEAN         DEFAULT NULL,
    isOverspeedFinished     BOOLEAN         DEFAULT NULL,
    overspeedTime           INT             DEFAULT NULL,
    isFatigueDriving        BOOLEAN         DEFAULT NULL,
    isHthrottleStop         BOOLEAN         DEFAULT NULL,
    isOilLeakage            BOOLEAN         DEFAULT NULL,
    PRIMARY KEY (ReportID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; */