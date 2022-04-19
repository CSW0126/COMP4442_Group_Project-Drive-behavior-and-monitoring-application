CREATE DATABASE IF NOT EXISTS `comp4442-group-project`;
USE `comp4442-group-project`;

CREATE TABLE IF NOT EXISTS `DrivingRecords`(
    RecordID                INT             NOT NULL        AUTO_INCREMENT,
    DriverID                VARCHAR(40)     NOT NULL,
    CarPlateNumber          VARCHAR(40)     NOT NULL,
    recordDAY               DATETIME        NOT NULL,
    recordHour              TIME            NOT NULL,
    isRapidlySpeedup        DOUBLE          DEFAULT NULL,
    isRapidlySlowdown       DOUBLE          DEFAULT NULL,
    isNeutralSlide          DOUBLE          DEFAULT NULL,
    isNeutralSlideFinished  DOUBLE          DEFAULT NULL,
    neutralSlideTime        DOUBLE          DEFAULT NULL,
    isOverspeed             DOUBLE          DEFAULT NULL,
    isOverspeedFinished     DOUBLE          DEFAULT NULL,
    overspeedTime           DOUBLE          DEFAULT NULL,
    isFatigueDriving        DOUBLE          DEFAULT NULL,
    isHthrottleStop         DOUBLE          DEFAULT NULL,
    isOilLeak               DOUBLE          DEFAULT NULL,  
    PRIMARY KEY (RecordID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;